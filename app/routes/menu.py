from GourmetBurgers import models
from flask import Blueprint, render_template, request

site = Blueprint(__name__, __name__)

@site.route('/menu')
def viewMenu():
   return render_template('menu.html')

@site.route('/menu/customise/<menuID>', methods=["GET","POST"])
def customise(menuID):
   menuItem = models.MenuItem(menuID)
   print("hello")
   if not menuItem.can_customise:
      return render_template('customise.html', can_customise = menuItem.can_customise)
  
   components = menuItem.components
   if request.method == "POST":
      print("hello")
      quantities = {}
      for item in components:
         quantities[item.id] = request.form[f'quantity{item.id}']
         decrease = f'decrease{item.id}'
         increase = f'increase{item.id}'
         if decrease in request.form:
            #update quantity
            quantities[item.id] = str(int(quantities[item.id]) - 1)
         elif increase in request.form:
            #update quantity
            quantities[item.id] = str(int(quantities[item.id]) + 1)
      
      return render_template('customise.html', can_customise = menuItem.can_customise, components = components, quantities = quantities)

   return render_template('customise.html', can_customise = menuItem.can_customise, components = components)