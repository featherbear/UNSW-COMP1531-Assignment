from flask import Blueprint, render_template

site = Blueprint(__name__, __name__)

@site.route('/menu')
def viewMenu():
   return render_template('menu.html')