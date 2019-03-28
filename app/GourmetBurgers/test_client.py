readOnly = True


from system import *

if readOnly:
  # https://stackoverflow.com/a/4019182
  print("READ ONLY MODE - CLONING DB..")
  
  import sqlite3
  
  with sqlite3.connect('test_db.sqlite3') as _db:
    queries = _db.iterdump()
    
  sys = GBsystem(':memory:')
  for line in queries:
    try:
      sys._db._conn.executescript(line)
    except sqlite3.OperationalError as e:
      pass
      # print(f"Skipped line - {line} - {e}")
else:
  sys = GBsystem('test_db.sqlite3')


sys.createOrder([
dict(
id = 1,
qty = 5
),

dict(
id = 5,
custom = True,
qty= 1,
items = {"1": 2}
)

]

)

if False:
  print("Inventory")
  for item in sys.inventory:
    print(item)
    
  print("---")
  inv2 = list(sys.inventory)[1]
  inv2.updateStock(30)
  print("---")

  for item in sys.inventory:
    print(item)



print("\n".join(sys._db._conn.iterdump()))