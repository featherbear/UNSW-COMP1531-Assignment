from lib import util
from flask import Blueprint, render_template, request, redirect, g, current_app as app

site = Blueprint(__name__, __name__)


@site.route('/staff/inventory/')
def view_inventory():
    return render_template('staff_inventory.html', inventory = app.GB.getInventoryMap())


@site.route('/staff/inventory/update', methods=['POST'])
def update_inventory():
	ingredient = app.GB.getIngredient(request.form['id'])
	ingredient.updateStock(int(request.form['new_stock']))

	return redirect("/staff/inventory/")

@site.route('/staff/inventory/availability', methods=['POST'])
def update_avalaibility():
	ingredient = app.GB.getIngredient(request.form['available'])
	if ingredient.available() == True:
		ingredient.available(False)
	else:
		ingredient.available(True)
	return redirect("/staff/inventory/")