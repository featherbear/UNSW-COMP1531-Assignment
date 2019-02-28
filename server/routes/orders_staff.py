from flask import Blueprint, render_template, request

site = Blueprint(__name__, __name__)

@site.route('/staff/orders/')
def view_staffOrder():
   return render_template('orders_staff.html')

@site.route('/staff/orders/update', methods = ['POST'])
def update_order():
   return request.form.get('test')

