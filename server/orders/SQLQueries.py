from lib import database

class ORDERS:
    STAFF_GET_ORDERS = "SELECT * FROM orders WHERE status = 0"
    STAFF_GET_ALL_ORDERS = "SELECT * FROM orders"

    # GET_ORDER = "SELECT * FROM orders WHERE orderCode = ?"
    GET_ORDER = "SELECT * FROM orders INNER JOIN (SELECT SUM (price) FROM link_orders WHERE link_orders.orderID = 1) orderID WHERE orders.orderID = 1 SELECT * FROM orders INNER JOIN (SELECT SUM(price) FROM link_orders WHERE link_orders.orderID = 1) orderID WHERE orders.orderID = 1"
    
    ORDER_TOTAL = "SELECT SUM (price) FROM link_orders WHERE orderID = ?"

    COMPLETE_ORDER = "UPDATE orders SET status = 1 WHERE orderID = ?"


    # Place an order
    """
    CREATE_ORDER = "INSERT INTO orders (date, status) VALUES (?, 0)"
    for each item:
        if custom:
            CREATE_CUSTOM_ORDER = "INSERT INTO custom_mains (mainID) VALUES (?)"
            for each ingredient:
                CREATE_LINK_CUSTOM_ORDERS = "INSERT INTO link_custom_orders (customID, ingredientID, quantity) VALUES (?, ?, ?)"
            CREATE_LINK_ORDER = "INSERT INTO link_orders (orderID, is_custom, customID, price) VALUES (?, 1, ?, ?)"
        else:
            CREATE_LINK_ORDER = "INSERT INTO link_orders (orderID, is_custom, itemID, price) VALUES (?, 0, ?, ?)"
    """


class INVENTORY:
    # GET_INVENTORY = "SELECT * FROM inventory"
    GET_INVENTORY = "SELECT inventoryID, name, suffix, price, quantity, stock_max FROM inventory, quantity_types WHERE inventory.quantity_type = quantity_types.quantityType"
    
    DISABLE_ITEM = "UPDATE inventory SET available = 0 WHERE inventoryID = ?"
    ENABLE_ITEM = "UPDATE inventory SET available = 1 WHERE inventoryID = ?"

    # GET_FOOD_ITEMS = "SELECT * FROM inventory INNER JOIN categories ON inventory.category = categories.categoryID "
    # GET_ITEMS_OF_CATEGORY = "SELECT  FROM category WHERE category = ?"
    # GET_ITEMS_OF_CATEGORY_LEVEL = "SELECT * FROM inventory WHERE category = ?"
    # CHECK_STOCK = "SELECT * FROM inventory WHERE ID = ?"

class MAINS:
    GET_DEFAULTS = "SELECT ingredientID, quantity, max FROM default_mains WHERE mainID = ?"

# from time import time

# def createOrder():
#   orderCreated = time()
#   orderComplete = False
#   orderID = database.insert(ORDERS.CREATE_ORDER, orderCreated, orderComplete, commit = False)

  