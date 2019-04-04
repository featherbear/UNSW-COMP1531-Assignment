import pytest

from .MenuItem import HistoricalMenuItem
from .models import Exceptionsa
import sqlite3

@pytest.fixture
def sys():
    with sqlite3.connect(db) as _db:
        queries = list(_db.iterdump())
    sys = GBSystem(':memory:')
    for line in queries:
        try:
            sys._db._conn.executescript(line)
        except sqlite3.OperationalError as e:
            pass
    return sys

# menu = sys.menu
# menu = list(menu)
# assert len(menu) == 5

# menuMap = sys.getMenuMap()
# assert len(menuMap) == 5

# id = list(menuMap.keys())[0]
# assert menuMap[id].id == id

# menuItem = sys.getMenuItem(id)
# assert menuItem.id == id

# with pytest.raises(Exceptions.NoItemError):
#     sys.getMenuItem(None)

def test_available(sys)

	a = MenuItem(2)
	# a._components[1] = 3
	# a._components[2] = 3

	# b = MenuItem(3,3,2,5)

	assert a.id == 2
	assert b.id == 3

	assert a.available == True

def unavailable_item(sys)
	c = MenuItem(6)
	with pytest.raises(Exceptions.NoItemError):



def test_usage()

