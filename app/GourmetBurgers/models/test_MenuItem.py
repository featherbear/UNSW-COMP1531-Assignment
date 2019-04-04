import pytest

# from GourmetBurgers import system
from ..system import GBSystem
from .MenuItem import *
from .Exceptions import NoItemError
import sqlite3

@pytest.fixture
def sys():
    with sqlite3.connect("../test_db.sqlite3") as _db:
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
	assert a.name == "MenuTwo"
	assert b.name == "MenuThree"
	assert c.name == "MenuFour"
	assert a.description == "MenuTwo"
	assert b.description == "MenuThree"
	assert c.description == "MenuFour"

def test_attributes(sys):
	a = MenuItem(2)
	b = MenuItem(3)
	c = MenuItem(4)
	assert a.price == 2
	assert b.price == 3
	assert c.price == 4
	assert a.id == 2
	assert b.id == 3
	assert c.id == 4


def test_can_custom(sys):
	item_a = MenuItem(1)
	item_b = MenuItem(2)
	item_c = MenuItem(5)

	assert item_a.can_customise == True
	assert item_b.can_customise == False
	assert item_c.can_customise == True

def test_components(sys):
	item_a = MenuItem(1)
	for component in item_a.components:
		assert type(component) is MenuIngredient

	assert item_a.components[0].id == 1


def test_available(sys):
	item_a = MenuItem(1)
	item_b = MenuItem(2)
	item_c = MenuItem(3)
	item_d = MenuItem(4)
	item_e = MenuItem(5)
	# m = MenuItem(6)

	# ID is available but there are not enough ingredients
	assert item_a.available == False
	assert item_b.available == False
	assert item_c.available == True
	assert item_d.available == True
	assert item_e.available == True


def test_item_not_found_error(sys):
	with pytest.raises(NoItemError):
		m = MenuItem(6)

# def test_usage()

