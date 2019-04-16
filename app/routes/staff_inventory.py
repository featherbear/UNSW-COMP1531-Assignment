from lib import util
from flask import Blueprint, render_template, request, redirect, g, current_app as app

site = Blueprint(__name__, __name__)


@site.route('/staff/inventory/')
def view_inventory():
	inventory = app.GB.getInventory
    return render_template('staff_inventory.html', inventory = inventory)
