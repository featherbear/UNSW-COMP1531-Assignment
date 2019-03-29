from . import SQL, models, utils

class GBsystem:
    def __init__(self, db: str = None):
        print("=== Initialising GourmetBurgers System ===")

        # Initialise db
        self._db = SQL.Database(db)
        print(f"Database: {self._db._db_file}")

        models._SQLBase.SQLBase._db = self._db = SQL.Database(db)
        models._SQLBase.SQLBase._SQL = self._SQL = SQL

        # Create SQL tables
        for value in SQL.TableQueries.values():
            self._db.create_table(value)

    @property
    def db(self):
        return self._db
    
    SQL = SQL

    @property
    def inventory(self):
        for inventoryItem in self._db.fetchAll(SQL.INVENTORY.GET_INVENTORY_IDS):
            yield models.Ingredient(inventoryItem[0])

    def getInventoryMap(self):
        inventory = {}
        for item in self.inventory:
            inventory[item.id] = item
        return inventory

    @property
    def menu(self):
        for menuItem in self._db.fetchAll(SQL.MENU.GET_MENU_ID):
            yield models.MenuItem(menuItem[0])

    def getMenuMap(self):
        menu = {}
        for item in self.menu:
            menu[item.id] = item
        return menu

    @property
    def categories(self):
        data = {}

        for categoryRecord in self._db.fetchAll(SQL.MENU.GET_CATEGORY_DATA):
            id, name = categoryRecord
            data[id] = name

        return data

    def getStaffOrders(self, fetchAll=False):
        if fetchAll:
            query = self._db.fetchAll(SQL.ORDERS.STAFF_GET_ALL_ORDERS)
        else:
            query = self._db.fetchAll(SQL.ORDERS.STAFF_GET_ORDERS)

        for order in query:
            yield models.Order(order[0])

    def getOrder(self, orderID):
        return models.Order(orderID)

    def createOrder(self, orderData):
        """
        # orderData 
        [
            {
                id: <id: int>,
                qty: <quantity: int>,
                custom: <isCustom: true/false>
                items: {
                    ingredientID: <quantity: int>
                }
            }
        ]

        """

        _inventoryMap = self.getInventoryMap()
        _menuMap = self.getMenuMap()

        price = 0

        # Validation
        _inventoryLevels = {}
        for ingredient in _inventoryMap.values():
            _inventoryLevels[ingredient.id] = ingredient.quantity

        for foodItem in orderData:
            menuID = int(foodItem["id"])
            quantity = int(foodItem.get("qty", 1))
            custom = bool(foodItem.get("custom", 0))

            ingredients = foodItem.get("items", {})
            ingredients = dict([(int(key), val)
                                for key, val in ingredients.items()])

            # Check that menuID exists
            if int(menuID) not in _menuMap:
                raise models.NoItemError(menuID)

            # Check that the item is available
            if not _menuMap[menuID].available:
                raise Exception("Unavailable")

            mainIngredients = _menuMap[menuID].getComponentUsage()
            # Check validity for custom items
            if custom:
                # Check if it is customisable
                if not self._db.fetchOne(SQL.MENU.CAN_CUSTOMISE, (menuID,)):
                    raise Exception(f"Menu ID {menuID} not customisable")
                # Check that there are ingredients
                if len(ingredients) is 0:
                    raise Exception("No ingredients in custom order item")

                # Calculate menu delta
                delta = {}
                for id, qty in mainIngredients.items():
                    delta[id] = ingredients.get(id, 0) - qty

                for id, quantity in delta.items():
                    # Only consider additional items
                    if quantity > 0:
                        price += models.Ingredient(id).price * quantity
            else:
                ingredients = mainIngredients

            price += _menuMap[menuID].price

            # Check that each ingredient exists, and has enough stock
            for ingredientID in ingredients:
                # Check if it exists
                if int(ingredientID) not in _inventoryLevels:
                    raise models.NoItemError(ingredientID)

                # Check there is enough stock for all orders
                _inventoryLevels[int(ingredientID)
                                 ] -= ingredients[ingredientID] * quantity
                if _inventoryLevels[int(ingredientID)] < 0:
                    raise Exception("Not enough stock")

        # Transaction
        ts = utils.getTime()

        orderID = self._db.insert(SQL.ORDERS.CREATE_ORDER, (ts,))
        for foodItem in orderData:
            menuID = int(foodItem["id"])
            quantity = int(foodItem.get("qty", 1))

            custom = bool(foodItem.get("custom", 0))
            ingredients = foodItem.get(
                "items", {}) if custom else _menuMap[menuID].getComponentUsage()

            for ingredientID, qty in ingredients.items():
                _inventoryMap[int(ingredientID)
                              ].updateStock(-1 * quantity * qty)

            if custom:
                customID = self._db.insert(
                    SQL.ORDERS.CREATE_CUSTOM_MAIN, (menuID,))
                print(f"Created custom {customID}")
                for ingredientID in ingredients:
                    self._db.insert(SQL.ORDERS.CREATE_LINK_CUSTOM_MAINS,
                                    (customID, ingredientID, ingredients[ingredientID]))
                self._db.insert(SQL.ORDERS.CREATE_LINK_ORDER__CUSTOM,
                                (orderID, customID, quantity, price))

            else:
                self._db.insert(SQL.ORDERS.CREATE_LINK_ORDER,
                                (orderID, menuID, quantity, price))

        print(f"Order {orderID} created at {ts}")
        return models.Order(orderID)

        """
        CREATE_ORDER
        for each item:
            if custom:
                CREATE_CUSTOM_MAIN
                for each ingredient:
                    CREATE_LINK_CUSTOM_ORDERS
                CREATE_LINK_ORDER__CUSTOM
            else:
                CREATE_LINK_ORDER
        """

    def updateOrder(self, orderID):
        self._db.update(self._SQL.ORDERS.COMPLETE_ORDER, (orderID,))
