import pytest
from .Exceptions import NoItemError
from .Ingredient import Ingredient
from ..system import GBSystem
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


#check if the inventory dictionary has right length
def test_getInventoryMap(sys):
    inventoryMap = sys.getInventoryMap()
    assert len(inventoryMap) == 5

#check if the dictionary's keys are the inventory ids
def test_ingredient_ID(sys):
    inventoryMap = sys.getInventoryMap()
    ID = list(inventoryMap.keys())[1]
    assert ID == inventoryMap[ID].id

#check if the property of ingredient is right
def test_ingredient_property(sys):
    ingredient = sys.getIngredient(3)
    assert ingredient.name == "InventoryThree"
    assert ingredient.price == 3
    assert ingredient.quantity == 3
    assert ingredient.quantity_max == 80
    assert ingredient.available == False

#check if the exception raised when try to get a non exist ingredient
def test_getNoneExistIngredient(sys):
    with pytest.raises(NoItemError):
        sys.getIngredient(None)

#check if the updateIngredientAvailability function set the availability correctly
def test_updateAvailability(sys):
    assert sys.getIngredient(1).available == True
    sys.updateIngredientAvailability(1, False)
    assert sys.getIngredient(1).available == False
    sys.updateIngredientAvailability(1, True)

#check if the updateIngredientStock function set the stock correctly,
#also check if it changes the availability automatically
def test_updateStock(sys):
    #test case 1
    assert sys.getIngredient(5).quantity == 5
    assert sys.getIngredient(5).available == True
    sys.updateIngredientStock(5, -5)
    assert sys.getIngredient(5).quantity == 0
    assert sys.getIngredient(5).available == False
    sys.updateIngredientStock(5, 5)

#check if the updateIngredientStock works well with another test case
def test_updateStock2(sys):
    assert sys.getIngredient(5).quantity == 5
    assert sys.getIngredient(5).available == True
    sys.updateIngredientStock(5, 25)
    assert sys.getIngredient(5).quantity == 25
    assert sys.getIngredient(5).available == True
    sys.updateIngredientStock(5, 5)


#check if the low stock checking returns correct status of the ingredient
def test_lowStockCheck(sys):
    assert sys.getIngredient(5).checkLowStock() == True
    sys.updateIngredientStock(5, 40)
    assert sys.getIngredient(5).checkLowStock() == False
    sys.updateIngredientStock(5, 5)
