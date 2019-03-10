from flask import Blueprint, render_template, request
from lib import util

site = Blueprint(__name__, __name__)

@site.route('/status/')
def view_customerOrder():
   return render_template('orders_customer.html')

@site.route('/order/json', methods = ["POST"])
def get_customerOrder():
   return util.createJSON(True, {
      # ...
   })

@site.route('/order/new', methods = ["POST"])
def placeOrder():

   
   import string, random
   orderID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
   print(f"New order created: {orderID}")

   print(request.get_json())
   return util.createJSON(True, orderID = 3)
