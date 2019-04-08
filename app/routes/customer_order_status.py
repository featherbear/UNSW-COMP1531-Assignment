from System i
from flask import Blueprint, render_template, request, g, current_app as app
from lib import util

site = Blueprint(__name__, __name__)

@site.route('/customer_order_status')
def customer_order_status(orderID):

