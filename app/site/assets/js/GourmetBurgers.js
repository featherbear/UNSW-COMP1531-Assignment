let GourmetBurgers;
(async () => {
  const fetchGET = async url =>
    fetch(url)
      .then(resp => resp.json())
      .then(res => {
        if (res.status) return res.data;
      });

  let self;
  GourmetBurgers = {
    _menu: await fetchGET("/data/menu.json"),
    _categories: await fetchGET("/data/categories.json"),
    _inventory: await fetchGET("/data/inventory.json"),

    // Promise: Get the order data for `orderID`
    // Returns a `dict` if the order exists, otherwise _null_
    getOrder: async orderID =>
      fetch("/order/json", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ orderID: orderID })
      })
        .then(resp => resp.json())
        .then(json => (json.status ? json.data : null)),

    // Calculate order total
    cart: {
      calulate: () => {
        let sum = 0;
        for (let item of self.cart._data) {
          console.log("Looking at", item);
          if (!item.custom) {
            sum += self._menu[item.id].price * item.qty;
            continue;
          }

          if (typeof item.items !== "object") throw Error("Bad item.items");

          // Custom items
          let delta = {};

          let defaults = self._menu[item.id].components;
          for (let ingredient of defaults) {
            delta[ingredient.id] =
              (item.items[ingredient.id] || 0) - ingredient.quantity;
          }

          let customPrice = 0;

          for (let id in delta) {
            //Only consider additional items
            if (delta[id] > 0) {
              customPrice += self._inventory[id].price * quantity;
            }
          }
          sum += customPrice * item.qty;
        }

        return sum;
      },

      // Submit order
      submitOrder: async () => {
        return fetch("/order/new", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            order: self.order._data
          })
        })
          .then(resp => resp.json())
          .then(json => {
            if (json.status) {
              self.cart._data = [];
              self.cart._updateOrder();
              return json.orderID;
            } else {
              return false;
            }
          });
      },

      // Add `id` into the order
      // If `data` is present, the order is a custom order
      addToOrder: function(id, data) {
        self.cart.__addToOrder(id, data);
        self.cart._updateOrder();
        console.log(self.cart.calulate());
      },
      __addToOrder: function(id, data) {
        // Validate `id` and `data`
        if (!(id in self._menu)) throw Error(`Invalid id ${id}`);
        if (data && !self._menu[id].can_customise)
          throw Error(`Cannot customise id ${id}`);

        // TODO: Check if there are enough ingredients

        // Check if the menu item has been added before, if so increase the quantity
        for (let item of self.cart._data) {
          if (item.id !== id) continue;
          if (data && !item.custom) continue;
          if (data && item.items.toSource() != data.toSource()) continue;

          item.qty += 1;
          return;
        }

        // New menu item into the order
        let orderEntry = {
          id: id,
          qty: 1
        };

        // Check if custom
        if (data) {
          orderEntry.custom = true;
          orderEntry.items = data;
        }

        // Add to order
        self.cart._data.push(orderEntry);
      },

      // On init, load localStorage into _data
      _data: (() => {
        try {
          return JSON.parse(localStorage.getItem("_gbOrder")) || [];
        } catch {
          return [];
        }
      })(),

      // Store _data into localStorage
      _updateOrder: function() {
        localStorage.setItem("_gbOrder", JSON.stringify(this._data));
      }
    }
  };

  // Reference
  self = GourmetBurgers;

  // Execute callback when the system loads
  typeof ready === "function" && ready();
})();
