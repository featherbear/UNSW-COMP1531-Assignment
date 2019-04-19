from GourmetBurgers import models
from flask import Blueprint, render_template

site = Blueprint(__name__, __name__)

@site.route('/menu')
def viewMenu():
   return render_template('menu.html')

@site.route('/menu/customise/<menuID>')
def customise(menuID):
   menuItem = models.MenuItem(menuID)
   components = menuItem.components
   return render_template('customise.html', can_customise = menuItem.can_customise, components = components)