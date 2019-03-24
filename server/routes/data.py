from flask import Blueprint, render_template
from lib import util
from data import methods

site = Blueprint(__name__, __name__)


@site.route('/data/inventory.json')
def getInventoryJSON():
    inventory = {}
    for item in methods.getInventory():
        inventory[item.id] = item.toDict()

    return util.createJSON(True, dict(data=inventory))


@site.route('/data/menu.json')
def getMenuJSON():
    menu = {}
    for item in methods.getMenu():
        menu[item.id] = item.toMenuDict()

    return util.createJSON(True, dict(data=menu))


@site.route('/data/categories.json')
def getCategoriesJSON():
    categories = methods.getCategories()
    return util.createJSON(True, dict(data=categories))
