from abc import ABC, abstractmethod
from .Exceptions import NoItemError
from ._SQLBase import SQLBase


class IngredientBase(SQLBase, ABC):
    @abstractmethod
    def __init__(self, inventoryID):
        query = self._db.fetchOne(
            self._SQL.INVENTORY.GET_INVENTORY_ITEM, (inventoryID,))
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
        resp = super().toDict()
        resp.update(dict(quantity_max=self._quantity_max))
        return resp


class HistoricalIngredient(IngredientBase):
    def __init__(self, inventoryID, quantity):
        super().__init__(inventoryID)
        self._quantity = quantity
        self._quantity_max = None


class Ingredient(IngredientBase):
    def __init__(self, inventoryID):
        super().__init__(inventoryID)

        query = self._db.fetchOne(
            self._SQL.INVENTORY.GET_STATUS, (inventoryID,))
        self._is_available = query[0]

    @property
    def available(self):
        return self._is_available

    @available.setter
    def available(self, state):
        state = bool(state)
        self._is_available = state
        self._db.update(
            self._SQL.INVENTORY.ENABLE_ITEM if state else self._SQL.INVENTORY.DISABLE_ITEM, (self._id,))

    def updateStock(self, change):
        if change < 0:
            change = abs(change)
            self._quantity -= change
            self._db.update(self._SQL.INVENTORY.DECREMENT_INVENTORY, (change, self._id))
        else:
            self._quantity = change
            self._is_available = True
            self._db.update(self._SQL.INVENTORY.SET_INVENTORY,
                            (change, self._id))

    def checkLowStock(self):
        return self._quantity / self._quantity_max <= 0.3 if self._quantity_max else False

    def toDict(self):
        resp = super().toDict()
        resp.update(dict(quantity=self._quantity if self._is_available else 0))
        return resp

    def __str__(self):
        return f"[Ingredient:{self.id} - {self.name} - {self.quantity}/{self.quantity_max}{' LOW' if self.checkLowStock() else ''} {'Available' if self.available else 'Unavailable'}]"
