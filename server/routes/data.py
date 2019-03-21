from flask import Blueprint, render_template
from lib import util
from data import methods

site = Blueprint(__name__, __name__)


@site.route('/data/inventory.json')
def getInventoryJSON():
    data = {}
    for item in methods.getInventory():
        data[item.id] = item.toDict()

    return util.createJSON(True, dict(data=data))


@site.route('/data/menu.json')
def getMenuJSON():
    menu = {}
    for item in methods.getMenu():
        menu[item.id] = item.toMenuDict()

    categories = methods.getCategories()

    return util.createJSON(True, dict(menu=menu, categories=categories))


@site.route('/data/categories.json')
def getCategoriesJSON():
    categories = methods.getCategories()
    return util.createJSON(True, dict(categories=categories))
