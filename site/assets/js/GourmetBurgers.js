let GourmetBurgers;
(() => {
  let self;
  GourmetBurgers = {
    _menu: undefined /* Promise */,
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
        .then(json => json.status ? json.data : null),
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
          return ({});
        }
      })(),

      updateOrder: function() {
        localStorage.setItem("_gbOrder", JSON.stringify(this._data));
      }
    }
  };
  self = GourmetBurgers;

  fetch("/data/menu.json")
    .then(resp => resp.json())
    .then(json => {
      if (!json.status) throw false;
      GourmetBurgers._menu = json.data;
    })
    .catch(e => console.error("Could not fetch menu"));
})();
