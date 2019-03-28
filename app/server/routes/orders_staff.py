from flask import Blueprint, render_template, request

site = Blueprint(__name__, __name__)

from lib import util
from GourmetBurgers import methods

@site.route('/staff/orders/')
def view_staffOrder():
   return render_template('orders_staff.html')

@site.route('/staff/orders/update', methods = ['POST'])
def update_order():
   pass

@site.route('/staff/orders.json')
def get_customerOrder():
   data = []
   for order in methods.getStaffOrders():
      data.append(order.toDict())
   return util.createJSON(True, dict(data=data))

@site.route('/staff/ordersAll.json')
def get_customerOrderAll():
   data = []
   for order in methods.getStaffOrders(True):
      data.append(order.toDict())
   return util.createJSON(True, dict(data=data))
