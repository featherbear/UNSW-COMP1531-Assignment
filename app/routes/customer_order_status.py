from GourmetBurgers import models
from flask import Blueprint, render_template, request, g, current_app as app
from lib import util

site = Blueprint(__name__, __name__)

@site.route('/status/<orderID>')
def customer_order_status(orderID):
    order = models.Order(orderID)
    date = order.date
    status = order.status
    price = order.price
    items = order.items
    return render_template("customer_order_status.html",orderID = orderID, date = date, status = status, price = price, items = items)
   