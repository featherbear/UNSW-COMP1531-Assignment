from lib import database

class ORDERS:
    # Get orders in the queue
    STAFF_GET_ORDERS = "SELECT orderID FROM orders WHERE status = 0"

    # Get all orders
    STAFF_GET_ALL_ORDERS = "SELECT orderID FROM orders"

    # Get basic order information (and price)
    # GET_ORDER = "SELECT * FROM orders WHERE orderCode = ?"
    GET_ORDER = "SELECT date, status, SUM(price) FROM orders INNER JOIN link_orders ON (orders.orderID = link_orders.orderID) WHERE orders.orderID = ? GROUP BY orders.orderID"

    GET_ORDER_RAW = "SELECT date, status FROM orders WHERE orderID = ?"

    # Get order status
    ORDER_STATUS = "SELECT status FROM orders WHERE orderID = ?"

    # Get order price
    ORDER_TOTAL = "SELECT SUM (price) FROM link_orders WHERE orderID = ?"

    # Get level 0 items of order
    ORDER_ITEMS_0 = "SELECT is_custom, customID, menuID, price FROM link_orders WHERE orderID = ?"

    # Get level 1 items of order (ie custom items)
    ORDER_ITEMS_1 = "SELECT inventoryID, quantity FROM link_custom_mains WHERE customID = ?"

    # Set an order as completed
    COMPLETE_ORDER = "UPDATE orders SET status = 1 WHERE orderID = ?"

    # Place an order
    CREATE_ORDER = "INSERT INTO orders (date, status) VALUES (?, 0)"
    CREATE_CUSTOM_MAIN = "INSERT INTO custom_mains (mainID) VALUES (?)"
    CREATE_LINK_CUSTOM_MAINS = "INSERT INTO link_custom_mains (customID, ingredientID, quantity) VALUES (?, ?, ?)"
    CREATE_LINK_ORDER__CUSTOM = "INSERT INTO link_orders (orderID, is_custom, customID, price) VALUES (?, 1, ?, ?)"
    CREATE_LINK_ORDER = "INSERT INTO link_orders (orderID, is_custom, itemID, price) VALUES (?, 0, ?, ?)"
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


class MENU:
    DISABLE_ITEM = "UPDATE menu SET is_available = 0 WHERE menuID = ?"
    ENABLE_ITEM = "UPDATE menu SET is_available = 1 WHERE menuID = ?"

    GET_MENU = "SELECT menuID, name, price, can_customise, is_available FROM menu"
    GET_MENU_ID = "SELECT menuID FROM menu"
    GET_MENU_ITEM_BASE = "SELECT name, price FROM menu WHERE menuID = ?"
    GET_MENU_ITEM_OPTIONS = "SELECT can_customise, is_available FROM menu WHERE menuID = ?"

    GET_MENU_ITEM = "SELECT name, price, can_customise, is_available FROM menu WHERE menuID = ?"

    # Get menuID of a custom meal
    RESOLVE_CUSTOM_TO_MENU = "SELECT menuID, name, price FROM menu, custom_mains WHERE customID = ? AND mainID = menuID"

    GET_CUSTOM_COMPONENTS = "SELECT inventoryID, quantity FROM link_custom_mains WHERE customID = ?"
    GET_MAIN_COMPONENTS = "SELECT inventoryID, quantity, max FROM link_menu WHERE menuID = ?"

    GET_CATEGORY_DATA = "SELECT categoryID, name from categories"
    GET_CATEGORY_LINK = "SELECT menuID, categoryID, level FROM link_categories"
    GET_CATEGORIES = "SELECT categoryID, level FROM link_categories WHERE menuID = ?"


class INVENTORY:
    # GET_INVENTORY = "SELECT * FROM inventory"
    GET_INVENTORY = "SELECT inventoryID, name, suffix, price, quantity, stock_max FROM inventory, quantity_types WHERE inventory.quantity_type = quantity_types.quantityID"
    GET_INVENTORY_IDS = "SELECT inventoryID FROM inventory"

    GET_INVENTORY_ITEM = "SELECT name, suffix, price, quantity, stock_max FROM inventory, quantity_types WHERE inventory.quantity_type = quantity_types.quantityID AND inventory.inventoryID = ?"

    DECREMENT_INVENTORY = "UPDATE inventory SET quantity = quantity - ? WHERE inventoryID = ?"
    SET_INVENTORY = "UPDATE inventory SET quantity = ? WHERE inventoryID = ?"

    DISABLE_ITEM = "UPDATE inventory SET is_available = 0 WHERE inventoryID = ?"
    ENABLE_ITEM = "UPDATE inventory SET is_available = 1 WHERE inventoryID = ?"  
    # GET_FOOD_ITEMS = "SELECT * FROM inventory INNER JOIN categories ON inventory.category = categories.categoryID "
    # GET_ITEMS_OF_CATEGORY = "SELECT  FROM category WHERE category = ?"
    # GET_ITEMS_OF_CATEGORY_LEVEL = "SELECT * FROM inventory WHERE category = ?"
    # CHECK_STOCK = "SELECT * FROM inventory WHERE ID = ?"


# def createOrder():
#   orderCreated = time()
#   orderComplete = False
#   orderID = database.insert(ORDERS.CREATE_ORDER, orderCreated, orderComplete, commit = False)
