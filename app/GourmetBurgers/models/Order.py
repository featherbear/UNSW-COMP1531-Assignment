from .Exceptions import NoItemError
from .MenuItem import MenuItem, HistoricalMenuItem
from ._SQLBase import SQLBase


class Order(SQLBase):
    def __init__(self, orderID):
        # Fetch data from database
        query = self._db.fetchOne(self._SQL.ORDERS.GET_ORDER_RAW, (orderID,))
        if not query:
            raise NoItemError(f"No order with id: {orderID}")

        self._id = orderID
        self._date, self._status = query
        self._price = 0

        self._items = []

        # Add food items of the order
        for foodItem in self._db.fetchAll(self._SQL.ORDERS.ORDER_ITEMS_0, (orderID,)):
            is_custom, customID, menuID, quantity, price = foodItem
            # TODO: BUG? quantiy -- price
            print("Fetch:", customID, menuID, quantity, price)
            self._items.append(HistoricalMenuItem(
                customID if is_custom else menuID, is_custom, price, quantity))

            # Update price
            self._price += price * quantity

        # Validate price
        # total = self._db.fetchOne(self._SQL.ORDERS.ORDER_TOTAL, (orderID,))[0]
        # assert total == self._price

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def status(self):
        return self._status

    @property
    def price(self):
        return self._price

    @property
    def items(self):
        return self._items

    # Complete the order
    def completeOrder(self):
        self._status = True
        self._db.update(self._SQL.ORDERS.COMPLETE_ORDER, (self.id,))

    # Serialise object into a dict
    def toDict(self):
        return dict(
            id=self._id,
            date=self._date,
            status=self._status,
            price=self._price,
            items=[menuItem.toDict() for menuItem in self._items]
        )
