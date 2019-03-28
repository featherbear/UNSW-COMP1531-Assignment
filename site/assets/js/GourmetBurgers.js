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

    cart: {
      calulate: () => {
        throw undefined;
      },

      placeOrder: async () => {
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
              self.cart._data = {};
              self.cart.updateOrder();
              return json.orderID;
            } else {
              return false;
            }
          });
      },

      _data: (() => {
        try {
          return JSON.parse(localStorage.getItem("_gbOrder")) || {};
        } catch {
          return {};
        }
      })(),

      updateOrder: function() {
        localStorage.setItem("_gbOrder", JSON.stringify(this._data));
      }
    }
  };
  self = GourmetBurgers;

  typeof ready === "function" && ready();
})();
