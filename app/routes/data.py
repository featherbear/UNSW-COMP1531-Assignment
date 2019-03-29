from flask import Blueprint, render_template, g, current_app as app

from lib import util


site = Blueprint(__name__, __name__)


@site.route('/data/inventory.json')
def getInventoryJSON():
    # print(current_app.GB)

    inventory = {}

    for item in app.GB.inventory:
        inventory[item.id] = item.toDict()

    return util.createJSON(True, dict(data=inventory))


@site.route('/data/menu.json')
def getMenuJSON():

    menu = {}

    for item in app.GB.menu:
        menu[item.id] = item.toMenuDict()

    return util.createJSON(True, dict(data=menu))


@site.route('/data/categories.json')
def getCategoriesJSON():
    return util.createJSON(True, dict(data=app.GB.categories))
