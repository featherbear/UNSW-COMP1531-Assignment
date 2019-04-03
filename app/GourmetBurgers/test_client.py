readOnly = True
db = './GourmetBurgers/test_db.sqlite3'

from .system import *
import pytest

if readOnly:
  # https://stackoverflow.com/a/4019182
  print("READ ONLY MODE - CLONING DB..")
  
  import sqlite3
  
  with sqlite3.connect(db) as _db:
    queries = list(_db.iterdump())
  # print(queries)
    
  sys = GBSystem(':memory:')
  for line in queries:
    try:
      sys._db._conn.executescript(line)
    except sqlite3.OperationalError as e:
      pass
      # print(f"Skipped line - {line} - {e}")
else:
  sys = GBSystem(db)


# 
inventory = sys.inventory
inventory = list(inventory)
assert len(inventory) == 5

#
inventoryMap = sys.getInventoryMap()
assert len(inventoryMap) == 5

#
id = list(inventoryMap.keys())[0]
assert inventoryMap[id].id == id

#
ingredient = sys.getIngredient(id)
# assert ingredient.name == "InventoryOne"
# assert inventory.price == 1
# assert inventory
assert ingredient.id == id

#
with pytest.raises(Exception) as e:
  sys.getIngredient(None)

#
assert sys.getIngredient(id).available == True
sys.updateIngredientAvailability(id, False)
assert sys.getIngredient(id).available == False

sys.updateIngredientAvailability(id, True)

#
assert sys.getIngredient(id).quantity == 1
assert sys.getIngredient(id).available == True
sys.updateIngredientStock(id, 25)
assert sys.getIngredient(id).quantity == 25
assert sys.getIngredient(id).available == True

'''
'''
sys.updateIngredientStock(id, 1)

'''
'''
#
assert sys.getIngredient(id).quantity == 1
assert sys.getIngredient(id).available == True
sys.updateIngredientStock(id, -1)
assert sys.getIngredient(id).quantity == 0
assert sys.getIngredient(id).available == False

# 
sys.updateIngredientStock(id, 25)
assert sys.getIngredient(id).checkLowStock() == False
sys.updateIngredientStock(id, 5)
assert sys.getIngredient(id).checkLowStock() == True

#
menu = sys.menu
menu = list(menu)
assert len(menu) == 5

#
menuMap = sys.getMenuMap()
assert len(menuMap) == 5

#
id = list(menuMap.keys())[0]
assert menuMap[id].id == id

#
menuItem = sys.getMenuItem(id)
assert menuItem.id == id

#
with pytest.raises(Exception) as e:
  sys.getMenuItem(None)

#
categories = sys.categories
categories = list(categories)
assert len(categories) == 5

#
orders = sys.getOrders()
orders = list(orders)
assert len(orders) == 1

#
orders = sys.getOrders(True)
orders = list(orders)
assert len(orders) == 2

#
orderID = orders[0].id
order = sys.getOrder(orderID)
assert order.id == orderID

#
with pytest.raises(Exception) as e:
  sys.getOrder(None)

# TODO: Create Order


# Update order

sys.updateOrder(1)
orders = sys.getOrders()
orders = list(orders)
assert len(orders) == 0
orders = sys.getOrders(True)
orders = list(orders)
assert len(orders) == 2

with pytest.raises(Exception) as e:
  sys.updateOrder(None)



'''
order = sys.createOrder([
  dict(
    id = 3,
    qty = 1,
    
  ),
  
  dict(
  id = 5,
  qty = 1,
  custom = True,
  items = {
  5: 1
  })
])

'''
'''
print(f"Order {order.id} created: ${order.price/100}")

sys.updateOrder(1)

#for item in sys.inventory:
#  print(item)

next(sys.inventory).available = False
next(sys.inventory).available = True
'''

if readOnly:
  _dump = list(sys._db._conn.iterdump())
  _dump_file = "output.db"
  with open(_dump_file, "w"):
    pass
  with sqlite3.connect(_dump_file) as f:
    f.executescript("".join(_dump))
  # [print(line) for line in _dump]
    
