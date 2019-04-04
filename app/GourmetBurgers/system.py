from . import SQL, models, utils


class GBSystem:
    def __init__(self, db: str = None):
        print("=== Initialising GourmetBurgers System ===")

        # Initialise database
        models._SQLBase.SQLBase._db = self._db = SQL.Database(db)
        models._SQLBase.SQLBase._SQL = self._SQL = SQL
        print(f"Database: {self._db._db_file}")

        # Create SQL tables
        for value in SQL.TableQueries.values():
            self._db.create_table(value)

    """ Ingredients / Inventory """
    # Get all ingredients
    @property
    def inventory(self):
        for inventoryItem in self._db.fetchAll(SQL.INVENTORY.GET_INVENTORY_IDS):
            yield models.Ingredient(inventoryItem[0])

    # Get ingredient dictionary (key: ID)
    def getInventoryMap(self):
        inventory = {}
        for item in self.inventory:
            inventory[item.id] = item
        return inventory

    def getIngredient(self, ingredientID):
        return models.Ingredient(ingredientID)

    def updateIngredientAvailability(self, ingredientID, status):
        self.getIngredient(ingredientID).available = status

    def updateIngredientStock(self, ingredientID, change):
        self.getIngredient(ingredientID).updateStock(change)

    """ Menu """
    # Get all menu items
    @property
    def menu(self):
        for menuItem in self._db.fetchAll(SQL.MENU.GET_MENU_ID):
            yield models.MenuItem(menuItem[0])

    # Get menu dictionary (key: ID)
    def getMenuMap(self):
        menu = {}
        for item in self.menu:
            menu[item.id] = item
        return menu

    def getMenuItem(self, menuID):
        return models.MenuItem(menuID)

    """ Categories """
    # Get category name mapping dictionary
    @property
    def categories(self):
        data = {}

        for categoryRecord in self._db.fetchAll(SQL.MENU.GET_CATEGORY_DATA):
            id, name = categoryRecord
            data[id] = name

        return data

    """ Orders """
    # Get all past orders

    def getOrders(self, fetchAll=False):
        if fetchAll:
            query = self._db.fetchAll(SQL.ORDERS.GET_ALL_ORDERS)
        else:
            query = self._db.fetchAll(SQL.ORDERS.GET_ORDERS)

        for order in query:
            yield models.Order(order[0])

    # Get order by orderID
    def getOrder(self, orderID):
        return models.Order(orderID)

    # Create an order
    def createOrder(self, orderData: list):
        """
        # orderData structure
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
        if type(orderData) is not list:
            raise models.IntegrityError("Bad input data")

        if len(orderData) == 0:
            raise models.IntegrityError("No order items")
                    
        _inventoryMap = self.getInventoryMap()
        _menuMap = self.getMenuMap()

        price = 0

        """
        VALIDATION
        """

        # Get inventory stock levels
        _inventoryLevels = {}
        for ingredient in _inventoryMap.values():
            _inventoryLevels[ingredient.id] = ingredient.quantity

        # Validate each food item
        for foodItem in orderData:
            menuID = int(foodItem["id"])
            quantity = int(foodItem.get("qty", 1))
            custom = bool(foodItem.get("custom", 0))

            ingredients = foodItem.get("items", {})
            # Convert key from str to int
            ingredients = dict([(int(key), val)
                                for key, val in ingredients.items()])

            # Check that menuID exists
            if int(menuID) not in _menuMap:
                raise models.NoItemError(menuID)

            # Check that the item is available
            if not _menuMap[menuID].available:
                raise models.OutOfStockError(menuID)

            mainIngredients = _menuMap[menuID].getComponentUsage()
            # Check validity for custom items
            if custom:
                # Check if it is customisable
                if not self._db.fetchOne(SQL.MENU.CAN_CUSTOMISE, (menuID,)):
                    raise models.IntegrityError(
                        f"Menu item {menuID} not customisable")

                # Check that there are ingredients
                if len(ingredients) is 0:
                    raise models.IntegrityError(
                        "No ingredients in custom order item")

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
                    raise models.OutOfStockError(
                        f"Not enough stock for ingredient {ingredientID}")

        """
        TRANSACTION
        """

        # Get timestamp (epoch)
        ts = utils.getTime()

        # Create SQL rows
        orderID = self._db.insert(SQL.ORDERS.CREATE_ORDER, (ts,))
        for foodItem in orderData:
            menuID = int(foodItem["id"])
            quantity = int(foodItem.get("qty", 1))

            custom = bool(foodItem.get("custom", 0))
            ingredients = foodItem.get(
                "items", {}) if custom else _menuMap[menuID].getComponentUsage()

            # Decrease inventory stock
            for ingredientID, qty in ingredients.items():
                _inventoryMap[int(ingredientID)
                              ].updateStock(-1 * quantity * qty)

            # Create custom order data
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

    # Complete an order
    def updateOrder(self, orderID):
        self.getOrder(orderID).completeOrder()
