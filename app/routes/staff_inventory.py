from lib import util
from flask import Blueprint, render_template, request, redirect, g, current_app as app

site = Blueprint(__name__, __name__)


@site.route('/staff/inventory/')
def view_inventory():
	inventory = app.GB.getInventoryMap()
    return render_template('staff_inventory.html', inventory = inventory)


@site.route('/staff/inventory/update',methods = ['POST'])
def update_inventory():
	ingredient = app.GB.getIngredient(request.form['id']
	ingredient.updateStock(request.form['new_stock'])

	return redirect("/staff/inventory/")