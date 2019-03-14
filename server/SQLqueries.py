"""
CREATE TABLE IF NOT EXISTS orders (
  orderID   INTEGER PRIMARY KEY AUTOINCREMENT,
  orderCode TEXT NOT NULL,
  date      DATETIME NOT NULL,
  status    INTEGER NOT NULL
);
"""

"""
CREATE TABLE IF NOT EXISTS quantity_types (
  quantityType INTEGER PRIMARY KEY AUTOINCREMENT,
  suffix TEXT
);
"""

"""
CREATE TABLE IF NOT EXISTS inventory (
  ID            INTEGER PRIMARY KEY AUTOINCREMENT,
  name          TEXT NOT NULL,
  price         REAL NOT NULL,
  quantity_type INTEGER NOT NULL,
  quantity      INTEGER NOT NULL,
  stock_max     INTEGER NOT NULL,

  FOREIGN KEY (quantity_type) REFERENCES quantity_types (quantityType)
);
"""

"""
CREATE TABLE IF NOT EXISTS custom_mains (
  customID INTEGER PRIMARY KEY AUTOINCREMENT,
  mainID   INTEGER NOT NULL,

  FOREIGN KEY (mainID) REFERENCES inventory (ID)
);
"""

"""
CREATE TABLE IF NOT EXISTS link_orders (
  orderID   INTEGER NOT NULL,
  is_custom INTEGER NOT NULL,
  itemID    INTEGER,
  customID  INTEGER,
  price     REAL NOT NULL,

  FOREIGN KEY (orderID)  REFERENCES orders (orderID),
  FOREIGN KEY (itemID)   REFERENCES inventory (ID),
  FOREIGN KEY (customID) REFERENCES custom_mains (customID)
);
"""

"""
CREATE TABLE IF NOT EXISTS link_custom_orders (
  mealID       INTEGER NOT NULL,
  ingredientID INTEGER NOT NULL,
  quantity     INTEGER,

  FOREIGN KEY (mealID) REFERENCES custom_mains (customID),
  FOREIGN KEY (ingredientID) REFERENCES inventory (ID)
);
"""

"""
CREATE TABLE IF NOT EXISTS default_mains (
  mainID       INTEGER NOT NULL,
  ingredientID INTEGER NOT NULL,
  quantity     INTEGER NOT NULL,
  max          INTEGER NOT NULL,

  FOREIGN KEY (mainID) REFERENCES inventory (ID),
  FOREIGN KEY (ingredientID) REFERENCES inventory (ID)
)
"""

