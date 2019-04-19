from GourmetBurgers import models
from flask import Blueprint, render_template, request

site = Blueprint(__name__, __name__)

@site.route('/menu')
def viewMenu():
   return render_template('menu.html')

@site.route('/menu/customise/<menuID>', methods=["GET","POST"])
def customise(menuID):
   menuItem = models.MenuItem(menuID)
   if not menuItem.can_customise:
      return render_template('customise.html', can_customise = menuItem.can_customise)
  
   components = menuItem.components
   if request == "POST":
      for item in components:
         decrease = 'decrease' + f'{item.id}'
         increase = 'increase' + f'{item.id}'
         if decrease in request.form:
            #update quantity
            pass
         elif increase in request.form:
            #update quantity
            pass

   return render_template('customise.html', can_customise = menuItem.can_customise, components = components)