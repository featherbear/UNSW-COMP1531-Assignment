readOnly = False
# db = 'test_db.sqlite3'
db = 'database.sqlite3'

from .system import *

if readOnly:
  # https://stackoverflow.com/a/4019182
  print("READ ONLY MODE - CLONING DB..")
  
  import sqlite3
  
  with sqlite3.connect(db) as _db:
    queries = _db.iterdump()
    
  sys = GBSystem(':memory:')
  for line in queries:
    try:
      sys._db._conn.executescript(line)
    except sqlite3.OperationalError as e:
      pass
      # print(f"Skipped line - {line} - {e}")
else:
  sys = GBSystem(db)


order = sys.createOrder([
  dict(
    id = 4,
    qty = 1,
    custom = False,
    items = {
      "4": 2
    }
    
    
  )
])
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
  _dump_file = "output_" + db + ".db"
  with open(_dump_file, "w"):
    pass
  with sqlite3.connect(_dump_file) as f:
    f.executescript("".join(_dump))
  [print(line) for line in _dump]
    
