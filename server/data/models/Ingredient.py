from abc import ABC, abstractmethod
from ...lib import database
from .. import sql_GourmetBurgers as SQL
from .Exceptions import NoItemError


class IngredientBase(ABC):
    @abstractmethod
    def __init__(self, inventoryID):
        query = database.fetchOne(
            SQL.INVENTORY.GET_INVENTORY_ITEM, (inventoryID,))
        if not query:
            raise NoItemError(f"No inventory item with id: {inventoryID}")

        self._id = inventoryID
        self._name, self._suffix, self._price, self._quantity, self._quantity_max = query

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def suffix(self):
        return self._suffix

    @property
    def quantity(self):
        return self._quantity

    @property
    def quantity_max(self):
        return self._quantity_max

    def toDict(self):
        return dict(
            id=self._id,
            name=self._name,
            suffix=self._suffix,
            price=self._price,
            quantity=self._quantity,
        )


class MenuIngredient(IngredientBase):
    def __init__(self, inventoryID, quantity, quantity_max):
        super().__init__(inventoryID)
        self._quantity = quantity
        self._quantity_max = quantity_max

    def toDict(self):
        return dict(**super().toDict(), quantity_max=self._quantity_max)


class HistoricalIngredient(IngredientBase):
    def __init__(self, inventoryID, quantity):
        super().__init__(inventoryID)
        self._quantity = quantity
        self._quantity_max = None


class Ingredient(IngredientBase):
    def __init__(self, inventoryID):
        super().__init__(inventoryID)
        self._is_available = True

    @property
    def available(self):
        return self._is_available

    @available.setter
    def available(self, state):
        state = bool(state)
        self._is_available = state
        database.update(
            SQL.MENU.ENABLE_ITEM if state else SQL.MENU.DISABLE_ITEM, (self._id,))

    def updateStock(self, change):
        if change < 0:
            change = abs(change)
            self._quantity -= change
            database.update(SQL.INVENTORY.DECREMENT_INVENTORY,
                            (change, self._id))
        else:
            self._quantity = change
            self._is_available = True
            database.update(SQL.INVENTORY.SET_INVENTORY, (change, self._id))

    def checkLowStock(self):
        return self._quantity / self._quantity_max <= 0.3 if self._quantity_max else False

    def toDict(self):
        return dict(**super().toDict(), quantity=self._quantity if self._is_available else 0)
