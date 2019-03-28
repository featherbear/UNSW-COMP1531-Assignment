from ..lib import database
from . import models, sql_GourmetBurgers as SQL


def getInventory():
    for inventoryItem in database.fetchAll(SQL.INVENTORY.GET_INVENTORY_IDS):
        yield models.Ingredient(inventoryItem[0])


def getMenu():
    for menuItem in database.fetchAll(SQL.MENU.GET_MENU_ID):
        yield models.MenuItem(menuItem[0])


def getCategories():
    data = {}

    for categoryRecord in database.fetchAll(SQL.MENU.GET_CATEGORY_DATA):
        id, name = categoryRecord
        data[id] = name

    return data


def getStaffOrders(fetchAll=False):

    if fetchAll:
        query = database.fetchAll(SQL.ORDERS.STAFF_GET_ALL_ORDERS)
    else:
        query = database.fetchAll(SQL.ORDERS.STAFF_GET_ORDERS)

    for order in query:
        yield models.Order(order[0])


# def determineCustomDifference(customID):
#     deltas = {}

#     customComponents = getCustom_components(customID)

#     mainID = resolveCustomToMain(customID)
#     if mainID is None:
#         return None

#     mainComponents = getMain_components(mainID)

#     for id in customComponents:
#         qtyCustom = customComponents[id]["quantity"]
#         qtyMain = mainComponents[id]["quantity"]
#         if qtyCustom is not qtyMain:
#             deltas[id] = qtyCustom - qtyMain

#     return deltas
