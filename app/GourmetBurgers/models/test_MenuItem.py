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

def test_item(sys):

	a = MenuItem(2)
	b = MenuItem(3)
	# a._components[1] = 3
	# a._components[2] = 3

	# b = MenuItem(3,3,2,5)
	assert a._name == "MenuTwo"
	assert b._name == "MenuThree"

	assert a._description == "MenuTwo"
	assert b._description == "MenuThree"

	assert a._price == 2
	assert b._price == 3

	assert a._id == 2
	assert b._id == 3


def test_usage(sys):


def test_available(sys):
	item_a = MenuItem(1)
	item_b = MenuItem(2)

	assert item_a.available == True
	assert item_b.available == False


def unavailable_item(sys):
	c = MenuItem(6)
	with pytest.raises(Exceptions.NoItemError):



def test_usage()

