from lib import database
from . import sql_GourmetBurgers as SQL

# TODO: Use OOP?


def getInventory():
    result = {}

    for inventoryItem in database.fetchAll(SQL.INVENTORY.GET_INVENTORY):
        obj = dict(
            zip(["id", "name", "suffix", "price", "quantity"], inventoryItem))
        result[obj["id"]] = obj

    return result


def getMenu():
    result = {}

    for menuItem in database.fetchAll(SQL.MENU.GET_MENU):
        obj = dict(
            zip(["id", "name", "price", "can_customise", "is_available"], menuItem))

        components = getMain_components(obj["id"])
        inventory = getInventory()

        limit = 1
        for component in components:
            limit = min(limit, int(
                inventory[component]["quantity"] / components[component]["quantity"]))
            if limit < 1:  # limit == 0
                obj["is_available"] = 0

        obj["components"] = components
        result[obj["id"]] = obj

    return result


def getStaffOrders(fetchAll=False):
    result = {}

    if fetchAll:
        for order in database.fetchAll(SQL.ORDERS.STAFF_GET_ALL_ORDERS):
            obj = dict(zip(["id", "date", "status"], order))
            result[obj["id"]] = obj

    else:
        for order in database.fetchAll(SQL.ORDERS.STAFF_GET_ORDERS):
            obj = dict(zip(["id", "date"], order))
            result[obj["id"]] = obj

    return result


def getCustom_components(customID):
    result = {}

    for component in database.fetchAll(SQL.MENU.GET_DEFAULTS, (customID)):
        obj = dict(zip(["id", "quantity"], component))
        result[obj["id"]] = obj

    return result


def getMain_components(mainID):
    result = {}

    for component in database.fetchAll(SQL.MENU.GET_MAIN_COMPONENTS, (mainID)):
        obj = dict(zip(["id", "quantity", "max"], component))
        result[obj["id"]] = obj

    return result


def resolveCustomToMain(customID):
    query = database.fetchOne(SQL.MENU.RESOLVE_CUSTOM_TO_MENU, (customID,))
    return query[0] if query else None


def determineCustomDifference(customID):
    deltas = {}

    customComponents = getCustom_components(customID)

    mainID = resolveCustomToMain(customID)
    if mainID is None:
        return None

    mainComponents = getMain_components(mainID)

    for id in customComponents:
        qtyCustom = customComponents[id]["quantity"]
        qtyMain = mainComponents[id]["quantity"]
        if qtyCustom is not qtyMain:
            deltas[id] = qtyCustom - qtyMain

    return deltas


def getOrder(orderID):
    query = database.fetchOne(SQL.ORDERS.GET_ORDER_RAW, (orderID,))
    if not query:
        return None

    result = dict(zip(["date", "status"], query))

    priceSum = 0

    items = []

    for foodItem in database.fetchAll(SQL.ORDERS.ORDER_ITEMS_0, (orderID,)):
        foodItemObj = dict(
            zip(["is_custom", "customID", "menuID", "price"], foodItem))

        customID = foodItemObj["customID"]
        itemID = resolveCustomToMain(
            customID) if foodItemObj["is_custom"] else foodItemObj["menuID"]

        item = dict(
            id=itemID,
            price=foodItemObj["price"]
        )

        if foodItemObj["is_custom"]:
            # Custom
            item["delta"] = determineCustomDifference(customID)

        items.append(item)
        priceSum += foodItemObj["price"]

    result["items"] = items
    result["price"] = priceSum

    return result
