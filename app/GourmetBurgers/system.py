import SQL
import models
import utils

class GBsystem:
    def __init__(self, db: str = None):
        print("=== Initialising GourmetBurgers System ===")
        print(f"Database: {db}")

        # Initialise db
        models._SQLBase.SQLBase._db = self._db = SQL.Database(db)
        models._SQLBase.SQLBase._SQL = self._SQL = SQL

        # Create SQL tables
        for value in SQL.TableQueries.values():
            self._db.create_table(value)

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
        self._db.fetchOne
    
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
        ts = utils.getTime()

        # Validate all menuID and ingredientIDs

        orderID = self._db.insert(SQL.ORDERS.CREATE_ORDER, (ts,))

        for foodItem in orderData:
            menuID = foodItem["id"]
            quantity = foodItem.get("qty", 1)
            custom = foodItem.get("custom", 0) # False
            ingredients = foodItem.get("items", {})

            _inventoryMap = self.getInventoryMap()
            _menuMap = self.getMenuMap()

            # Check that menuID exists
            if int(menuID) not in _menuMap:
                raise models.NoItemError(menuID)
            
            # (for custom orders) Check that all the ingredientID entries exist
            if custom:
                # Check that the item is customisable
                if not self._db.fetchOne(SQL.MENU.CAN_CUSTOMISE, (menuID,)):
                    raise Exception(menuID)

                if len(ingredients) is 0:
                    raise Exception("No items in order")

                for ingredientID in ingredients:
                    if int(ingredientID) not in _inventoryMap:
                        raise models.NoItemError(ingredientID)

            price = 9999

            # Ingredient count check
            pass

            # Add
            if custom:
                customID = self._db.insert(SQL.ORDERS.CREATE_CUSTOM_MAIN, (menuID,))
                print(f"Created custom {customID}")
                for ingredientID in ingredients:
                    self._db.insert(SQL.ORDERS.CREATE_LINK_CUSTOM_MAINS, (customID, ingredientID, ingredients[ingredientID]))
                self._db.insert(SQL.ORDERS.CREATE_LINK_ORDER__CUSTOM, (orderID, customID, quantity, price))

            else:
                self._db.insert(SQL.ORDERS.CREATE_LINK_ORDER, (orderID, menuID, quantity, price))
                
        print(f"Order {orderID} created at {ts}")

        
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
        pass
    
    def updateOrder(self, orderID):
        pass
    
    