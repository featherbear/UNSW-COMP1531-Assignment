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
	c = MenuItem(4)
	# a._components[1] = 3
	# a._components[2] = 3
	# b = MenuItem(3,3,2,5)
	assert a._name == "MenuTwo"
	assert b._name == "MenuThree"
	assert c._name == "MenuFour"
	assert a._description == "MenuTwo"
	assert b._description == "MenuThree"
	assert c._description == "MenuFour"
	assert a._price == 2
	assert b._price == 3
	assert a._id == 2
	assert b._id == 3


def test_can_custom(sys):
	item_a = MenuItem(1)
	item_b = MenuItem(2)
	item_c = MenuItem(5)

	assert item_a.can_custome == True
	assert item_b.can_custome == False
	assert item_c.can_custome == True

# def test_component_usage(sys):
# 	item_a = MenuItem(1)
# 	item_b = MenuItem(2)
# 	item_c = MenuItem(5)


def test_available(sys):
	item_a = MenuItem(1)
	item_b = MenuItem(2)
	item_c = MenuItem(3)
	item_d = MenuItem(4)
	item_e = MenuItem(5)

	assert item_a.available == True
	assert item_b.available == False
	assert item_c.available == True
	assert item_d.available == True
	assert item_e.available == True


def item_not_found_error(sys):
	with pytest.raises(Exceptions.NoItemError):
		c = MenuItem(6)

# def test_usage()

