from System import GBSystem
from flask import Blueprint, render_template, request, g, current_app as app
from lib import util

site = Blueprint(__name__, __name__)

@site.route('/customer_order_status')
def customer_order_status(orderID):
    order = GBSystem.getOrder(orderID)
    datetime = order.datetime
    status = order.status
    price = order.price
    return render_template("customer_order_status.html",orderID = orderID, datetime = datetime, status = status, price = price)