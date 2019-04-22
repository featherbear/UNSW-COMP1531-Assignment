/*
  GourmetBurgers system object
*/

// Demo menu
let __menu = {"1": {"id": 1, "name": "The Lot", "description": "We overimagined this item and realised that it will never come into actualisation because we never have the right ingredients.", "price": 895, "can_customise": true, "available": false, "categories": {"0": [1]}, "components": {"1": {"id": 1, "quantity": 2, "quantity_max": 2}, "2": {"id": 2, "quantity": 0, "quantity_max": 2}, "4": {"id": 4, "quantity": 0, "quantity_max": 2}, "6": {"id": 6, "quantity": 2, "quantity_max": 2}, "7": {"id": 7, "quantity": 2, "quantity_max": 2}, "8": {"id": 8, "quantity": 2, "quantity_max": 2}, "9": {"id": 9, "quantity": 0, "quantity_max": 1}, "10": {"id": 10, "quantity": 1, "quantity_max": 1}, "11": {"id": 11, "quantity": 0, "quantity_max": 1}, "12": {"id": 12, "quantity": 1, "quantity_max": 2}, "13": {"id": 13, "quantity": 1, "quantity_max": 2}}}, "2": {"id": 2, "name": "The Lil", "description": "We give you, a single slice of cheese in a box. Perfection.", "price": 2500, "can_customise": false, "available": true, "categories": {"0": [1]}, "components": {"12": {"id": 12, "quantity": 1, "quantity_max": 1}}}, "3": {"id": 3, "name": "The Small Cam", "description": "Not a maccas burger. We promise.", "price": 895, "can_customise": true, "available": true, "categories": {"0": [1]}, "components": {"1": {"id": 1, "quantity": 0, "quantity_max": 2}, "2": {"id": 2, "quantity": 2, "quantity_max": 2}, "4": {"id": 4, "quantity": 0, "quantity_max": 2}, "5": {"id": 5, "quantity": 0, "quantity_max": 2}, "6": {"id": 6, "quantity": 1, "quantity_max": 2}, "7": {"id": 7, "quantity": 1, "quantity_max": 2}, "8": {"id": 8, "quantity": 0, "quantity_max": 1}, "9": {"id": 9, "quantity": 0, "quantity_max": 1}, "10": {"id": 10, "quantity": 0, "quantity_max": 1}, "11": {"id": 11, "quantity": 1, "quantity_max": 1}, "12": {"id": 12, "quantity": 1, "quantity_max": 1}, "13": {"id": 13, "quantity": 0, "quantity_max": 1}}}, "4": {"id": 4, "name": "nuggs (24 pc)", "description": "Reduce your lifespan by a factor of 24!", "price": 995, "can_customise": false, "available": false, "categories": {"0": [2]}, "components": {"14": {"id": 14, "quantity": 24, "quantity_max": 24}}}, "5": {"id": 5, "name": "nuggs (12 pc)", "description": "A little on the excessive side", "price": 600, "can_customise": false, "available": false, "categories": {"0": [2]}, "components": {"14": {"id": 14, "quantity": 12, "quantity_max": 12}}}, "6": {"id": 6, "name": "nuggs (6 pc)", "description": "Delightful chicken nuggets", "price": 400, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"14": {"id": 14, "quantity": 6, "quantity_max": 6}}}, "7": {"id": 7, "name": "The Vegan", "description": "Veggies veggies veggies", "price": 795, "can_customise": false, "available": true, "categories": {"0": [1]}, "components": {"1": {"id": 1, "quantity": 0, "quantity_max": 2}, "2": {"id": 2, "quantity": 2, "quantity_max": 2}, "5": {"id": 5, "quantity": 2, "quantity_max": 4}, "7": {"id": 7, "quantity": 2, "quantity_max": 2}, "8": {"id": 8, "quantity": 2, "quantity_max": 3}, "9": {"id": 9, "quantity": 1, "quantity_max": 1}}}, "8": {"id": 8, "name": "Fries (Small)", "description": "ur a smol fry", "price": 200, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"15": {"id": 15, "quantity": 100, "quantity_max": 100}}}, "9": {"id": 9, "name": "Fries (Medium)", "description": "The same as Small Fries but with an increased price tag", "price": 450, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"15": {"id": 15, "quantity": 150, "quantity_max": 150}}}, "10": {"id": 10, "name": "Fries (Large)", "description": "Enough to last you the week", "price": 550, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"15": {"id": 15, "quantity": 250, "quantity_max": 250}}}, "11": {"id": 11, "name": "Coke (600mL bottle)", "description": "Comes with additional toilet cleaning functionality", "price": 450, "can_customise": false, "available": true, "categories": {"0": [3]}, "components": {"16": {"id": 16, "quantity": 600, "quantity_max": 600}}}, "12": {"id": 12, "name": "Coke (Cup)", "description": "60% Coke, 100% Ice. Wait what.", "price": 300, "can_customise": false, "available": true, "categories": {"0": [3]}, "components": {"16": {"id": 16, "quantity": 500, "quantity_max": 500}}}, "13": {"id": 13, "name": "Orange Juice (350mL)", "description": "Coloured water with artificial sweetener and citric acid", "price": 350, "can_customise": false, "available": true, "categories": {"0": [3]}, "components": {"17": {"id": 17, "quantity": 350, "quantity_max": 350}}}, "14": {"id": 14, "name": "Orange Juice (Cup)", "description": "Juice with all the nutrients filtered out", "price": 300, "can_customise": false, "available": true, "categories": {"0": [3]}, "components": {"17": {"id": 17, "quantity": 500, "quantity_max": 500}}}, "15": {"id": 15, "name": "Milk (400mL bottle)", "description": "The possibly only healthy thing in our menu", "price": 200, "can_customise": false, "available": true, "categories": {"0": [3]}, "components": {"18": {"id": 18, "quantity": 400, "quantity_max": 400}}}, "16": {"id": 16, "name": "The Gourmet", "description": "Our flagship burger", "price": 1550, "can_customise": true, "available": true, "categories": {"0": [1]}, "components": {"1": {"id": 1, "quantity": 1, "quantity_max": 2}, "2": {"id": 2, "quantity": 1, "quantity_max": 2}, "4": {"id": 4, "quantity": 2, "quantity_max": 3}, "5": {"id": 5, "quantity": 0, "quantity_max": 3}, "6": {"id": 6, "quantity": 2, "quantity_max": 3}, "7": {"id": 7, "quantity": 2, "quantity_max": 4}, "8": {"id": 8, "quantity": 1, "quantity_max": 1}, "10": {"id": 10, "quantity": 1, "quantity_max": 1}, "11": {"id": 11, "quantity": 0, "quantity_max": 1}, "12": {"id": 12, "quantity": 2, "quantity_max": 2}, "13": {"id": 13, "quantity": 2, "quantity_max": 2}}}, "17": {"id": 17, "name": "Potato Roll", "description": "TBH I didn't even know this thing existed - Andrew", "price": 750, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {}}, "18": {"id": 18, "name": "Strawberry Sundae (Small)", "description": "Fake strawberries with two scoops of homebrand icecream", "price": 350, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"19": {"id": 19, "quantity": 70, "quantity_max": 70}, "20": {"id": 20, "quantity": 10, "quantity_max": 10}}}, "19": {"id": 19, "name": "Strawberry Sundae (Medium)", "description": "We give you half an extra strawberry, but then again it's sauce so you don't know", "price": 430, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"19": {"id": 19, "quantity": 140, "quantity_max": 140}, "20": {"id": 20, "quantity": 20, "quantity_max": 20}}}, "20": {"id": 20, "name": "Strawberry Sundae (Large)", "description": "Please buy me, no one buys me.", "price": 510, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"19": {"id": 19, "quantity": 210, "quantity_max": 210}, "20": {"id": 20, "quantity": 30, "quantity_max": 30}}}, "21": {"id": 21, "name": "Chocolate Sundae (Small)", "description": "Cocoa essence mixed with flour", "price": 350, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"19": {"id": 19, "quantity": 70, "quantity_max": 70}, "21": {"id": 21, "quantity": 10, "quantity_max": 10}}}, "22": {"id": 22, "name": "Chocolate Sundae (Medium)", "description": "The chocolate sauce is probably made of Nutella", "price": 430, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"19": {"id": 19, "quantity": 140, "quantity_max": 140}, "21": {"id": 21, "quantity": 20, "quantity_max": 20}}}, "23": {"id": 23, "name": "Chocolate Sundae (Large)", "description": "Chocolate is the superior flavour.", "price": 510, "can_customise": false, "available": true, "categories": {"0": [2]}, "components": {"19": {"id": 19, "quantity": 210, "quantity_max": 210}, "21": {"id": 21, "quantity": 30, "quantity_max": 30}}}};
let __categories = {"1": "Mains", "2": "Sides", "3": "Drinks"};
let __inventory = {"1": {"id": 1, "name": "Sesame Bun", "suffix": "pc(s)", "price": 100, "quantity": 150}, "2": {"id": 2, "name": "Kaiser Roll", "suffix": "pc(s)", "price": 100, "quantity": 60}, "3": {"id": 3, "name": "Potato Roll", "suffix": "pc(s)", "price": 100, "quantity": 50}, "4": {"id": 4, "name": "Chicken Patty", "suffix": "pc(s)", "price": 500, "quantity": 20}, "5": {"id": 5, "name": "Vegetarian Patty", "suffix": "pc(s)", "price": 300, "quantity": 40}, "6": {"id": 6, "name": "Beef Patty", "suffix": "pc(s)", "price": 600, "quantity": 10}, "7": {"id": 7, "name": "Tomato", "suffix": "pc(s)", "price": 200, "quantity": 46}, "8": {"id": 8, "name": "Lettuce", "suffix": "pc(s)", "price": 100, "quantity": 40}, "9": {"id": 9, "name": "Tomato Sauce", "suffix": "pc(s)", "price": 100, "quantity": 20}, "10": {"id": 10, "name": "Barbecue Sauce", "suffix": "pc(s)", "price": 100, "quantity": 10}, "11": {"id": 11, "name": "Small Cam Sauce", "suffix": "pc(s)", "price": 100, "quantity": 18}, "12": {"id": 12, "name": "Cheddar Cheese", "suffix": "pc(s)", "price": 200, "quantity": 17}, "13": {"id": 13, "name": "Swiss Cheese", "suffix": "pc(s)", "price": 200, "quantity": 30}, "14": {"id": 14, "name": "Chicken Nugget", "suffix": "pc(s)", "price": "", "quantity": 8}, "15": {"id": 15, "name": "Potato Fry", "suffix": "g", "price": "", "quantity": 9150}, "16": {"id": 16, "name": "Coke", "suffix": "mL", "price": "", "quantity": 9000}, "17": {"id": 17, "name": "Orange Juice", "suffix": "mL", "price": "", "quantity": 0}, "18": {"id": 18, "name": "Milk", "suffix": "mL", "price": "", "quantity": 10000}, "19": {"id": 19, "name": "Icecream", "suffix": "mL", "price": 1, "quantity": 1790}, "20": {"id": 20, "name": "Strawberry Sauce", "suffix": "mL", "price": 10, "quantity": 1800}, "21": {"id": 21, "name": "Chocolate Sauce", "suffix": "mL", "price": 10, "quantity": 1770}};

let GourmetBurgers;
(async () => {
  // JSON Fetch Promise
  const fetchGET = async url =>
    fetch(url)
      .then(resp => resp.json())
      .then(res => {
        if (res.status) return res.data;
      });

  // Self-reference
  let self;

  GourmetBurgers = {
    // Get system data
    _menu: __menu,
    _categories: __categories,
    _inventory: __inventory,

    // Promise: Get the order data for `orderID`
    // Returns a `dict` if the order exists, otherwise _null_
    getOrder: async orderID => {
     if (orderID == 1) {
       return {"id": "1", "date": 1555837574, "status": 0, "price": 3510, "items": [{"id": 23, "name": "Chocolate Sundae (Large)", "quantity": 1, "price": 510}, {"id": 12, "name": "Coke (Cup)", "quantity": 1, "price": 300}, {"id": 6, "name": "nuggs (6 pc)", "quantity": 1, "price": 400}, {"id": 17, "name": "Potato Roll", "quantity": 1, "price": 750},{"id": 16, "name": "The Gourmet", "quantity": 1, "price": 1550, "components": {"1": 1, "2": 1, "4": 0, "5": 0, "6": 2, "7": 2, "8": 0, "10": 1, "11": 0, "12": 2, "13": 0}, "custom": 1}]}
     }
     return null;
    },
    // Calculate order total
    cart: {
      calculate: () => {
        let sum = 0;

        for (let item of self.cart._data) {
          sum += self.cart._calculate(item) * item.qty;
        }

        return sum;
      },

      // Calculate the price of an individual order item
      // Does not account for quantity
      _calculate: item => {
        let price = self._menu[item.id].price;

        // If the item is not a custom item, then return the base price
        if (!item.custom) {
          return price;
        }

        // Structure check
        if (typeof item.items !== "object") throw Error("Bad item.items");

        // For custom items, calculate the ingredient delta
        let delta = {};
        let defaults = Object.values(self._menu[item.id].components);
        for (let ingredient of defaults) {
          delta[ingredient.id] =
            (item.items[ingredient.id] || 0) - ingredient.quantity;
        }

        // For added ingredients, add the price of each ingredient
        for (let id in delta) {
          if (delta[id] > 0) {
            price += self._inventory[id].price * delta[id];
          }
        }
        return price;
      },

      // Submit order
      submitOrder: async () => {
        self.cart._data = [];
        self.cart._updateOrder();
        return {url: "../order/complete/1"}
      },

      // Add `id` into the order
      // If `data` is present, the order is a custom order
      addToOrder: function(id, data) {
        self.cart.__addToOrder(id, data);
        self.cart._updateOrder();
      },

      __addToOrder: function(id, data) {
        // Validate `id` and `data`
        if (!(id in self._menu)) throw Error(`Invalid id ${id}`);
        if (data && !self._menu[id].can_customise)
          throw Error(`Cannot customise id ${id}`);

        // Check if there are enough ingredients
        let componentUsage = {};

        // Calculate component usage of current items
        for (let orderItem of self.cart._data) {
          if (orderItem.custom) {
            components = orderItem.items;
          } else {
            components = {};
            for (let component of Object.values(
              self._menu[orderItem.id].components
            )) {
              components[component.id] = component.quantity;
            }
          }
          for (let componentID in components) {
            componentUsage[componentID] =
              ((componentUsage[componentID] || 0) + components[componentID]) *
              orderItem.qty;
          }
        }

        // Add the component usage for the current item
        if (data) {
          components = data;
        } else {
          components = {};
          for (let component of Object.values(self._menu[id].components)) {
            components[component.id] = component.quantity;
          }
        }

        for (let componentID in components) {
          componentUsage[componentID] =
            (componentUsage[componentID] || 0) + components[componentID];
        }

        // Check that there is enough stock for the component usage
        for (let componentID in componentUsage) {
          if (!(componentID in self._inventory)) {
            throw Error(`No ingredient ${componentID} found`);
          }
          if (
            self._inventory[componentID].quantity < componentUsage[componentID]
          ) {
            throw Error(
              "Your order uses too many ingredients which we don't have enough of :'("
            );
          }
        }

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
