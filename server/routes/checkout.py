from flask import Blueprint, render_template

site = Blueprint(__name__, __name__)

@site.route('/')
def viewCheckout():
   return render_template('checkout.html')