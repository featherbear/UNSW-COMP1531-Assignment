from flask import Blueprint, render_template

site = Blueprint(__name__, __name__)

@site.route('/')
def viewCart():
   return render_template('cart.html')