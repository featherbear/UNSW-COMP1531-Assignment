import pytest

# from GourmetBurgers import system
from ..system import GBSystem
from .Order import *
from .Exceptions import NoItemError
import sqlite3

@pytest.fixture
def sys():
    with sqlite3.connect("../test_db.sqlite3") as _db:
        queries = list(_db.iterdump())
        [print(line) for line in queries]
    sys = GBSystem(':memory:')
    for line in queries:
        try:
            sys._db._conn.executescript(line)
        except sqlite3.OperationalError as e:
            pass
    return sys


def test_orders_id(sys):
	a = Order(1)
	b = Order(2)

	assert a._id == 1
	assert b._id == 2

def test_orders_status(sys):
	a = Order(1)
	b = Order(2)
	assert a._status == False
	assert b._status == True
	# assert a._date == 

def test_orders_price(sys):
	a = Order(1)
	b = Order(2)
	assert a._price == 16
	assert b.price == 1

def test_orders_items(sys):
	a = Order(1)
	b = Order(2)

	assert len(a.items) == 2
	assert len(b.items) == 1


	print([x.name for x in a.items])
	MenuItem_a1 = a.items[0]

	# print("AAAAA",MenuItem_a1.id)
	assert MenuItem_a1.price == 8
	assert MenuItem_a1.quantity == 1
	assert MenuItem_a1.is_custom ==False

	MenuItem_a2 = a.items[1]

	assert MenuItem_a2.price == 8
	assert MenuItem_a2.quantity == 1
	assert MenuItem_a2.is_custom == True


def test_complete_order(sys):
	a = Order(1)
	assert a.status == False

	a.completeOrder()
	assert a.status == True

def test_no_order(sys):
	with pytest.raises(NoItemError):
		a = Order(3)





# def test_orders_