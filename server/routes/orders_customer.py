from flask import Blueprint, render_template

site = Blueprint(__name__, __name__)

@site.route('/status/')
def view_customerOrder():
   return render_template('orders_customer.html')

@site.route('/status/<orderID>')
def view_customerOrderID(orderID):
   return render_template('orders_customer_view.html', orderID = orderID)