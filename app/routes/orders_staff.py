from lib import util
from flask import Blueprint, render_template, request, redirect, g, current_app as app

site = Blueprint(__name__, __name__)


@site.route('/staff/orders/')
def view_staffOrder():
    return render_template('orders_staff.html', orders = sorted(app.GB.getOrders(), key=lambda o: o.date))


@site.route('/staff/orders/update', methods=['POST'])
def update_order():
    order = app.GB.getOrder(request.form['orderID'])
    order.completeOrder()

    return redirect("/staff/orders/")

# @site.route('/staff/orders.json')
# def get_customerOrder():
#     data = []
#     for order in app.GB.getOrders():
#         data.append(order.toDict())
#     return util.createJSON(True, dict(data=data))


# @site.route('/staff/ordersAll.json')
# def get_customerOrderAll():
#     data = []
#     for order in app.GB.getOrders(True):
#         data.append(order.toDict())
#     return util.createJSON(True, dict(data=data))
