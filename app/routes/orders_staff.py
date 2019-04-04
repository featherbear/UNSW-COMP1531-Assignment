from lib import util
from flask import Blueprint, render_template, request, g, current_app as app

site = Blueprint(__name__, __name__)


@site.route('/staff/orders/')
def view_staffOrder():
    return render_template('orders_staff.html', orders = list(list(app.GB.getOrders()))*2)


@site.route('/staff/orders/update', methods=['POST'])
def update_order():
    return "UPDATED: " + str(request.form['orderID'])


    order = app.GB.getOrder(orderID)
    order.completeOrder()

    pass

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
