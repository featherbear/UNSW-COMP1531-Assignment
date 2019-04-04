import pytest

from .MenuItem import HistoricalMenuItem
from .models import Exceptions
from .system import *
readOnly = True
db = './GourmetBurgers/test_db.sqlite3'


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

	menu = sys.menu
	menu = list(menu)
	assert len(menu) == 5

	menuMap = sys.getMenuMap()
	assert len(menuMap) == 5

	id = list(menuMap.keys())[0]
	assert menuMap[id].id == id

	menuItem = sys.getMenuItem(id)
	assert menuItem.id == id

	with pytest.raises(Exceptions.NoItemError):
	    sys.getMenuItem(None)

def test_available()
	a = MenuItem(2,2,10,8)
	a._components[1] = 3
	a._components[2] = 3

	b = MenuItem(3,3,2,5)

	assert a.id == 2
	assert b.id == 3

def test_usage()
