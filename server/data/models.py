from lib import database
from . import sql_GourmetBurgers as SQL


class NoItemError(Exception):
    pass


class InventoryStock():
    def __init__(self, inventoryID):
        query = database.fetchOne(
            SQL.INVENTORY.GET_INVENTORY_ITEM, (inventoryID,))
        if not query:
            raise NoItemError(f"No inventory item with id: {inventoryID}")

        self._id = inventoryID
        self._name, self._suffix, self._price, self._quantity, self._quantity_max = query
        self._is_low_stock = self._quantity / \
            self._quantity_max <= 0.3 if self._quantity_max else False

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def suffix(self):
        return self._suffix

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    @property
    def quantity_max(self):
        return self._quantity_max

    def toDict(self):
        resp = dict(
            id=self._id,
            name=self._name,
            suffix=self._suffix,
            price=self._price,
            quantity=self._quantity,
            
        )

        if self._quantity_max is not None:
            resp["quantity_max"] = self._quantity_max

        return resp


class MenuComponent(InventoryStock):
    def __init__(self, inventoryID, quantity, quantity_max = None):
        super().__init__(inventoryID)
        self._quantity = quantity
        self._quantity_max = quantity_max


class MenuItem():
    def __init__(self, menuID, price=None, custom=False):
        query = database.fetchOne(SQL.MENU.GET_MENU_ITEM, (menuID,))
        if not query:
            raise NoItemError(f"No menu item with id: {menuID}")

        self._id = menuID
        self._name, self._price, self._can_customise, self._is_available = query

        if price:
            self._price = price

        query = database.fetchAll(SQL.MENU.GET_CATEGORIES, (menuID,))
        
        self._categories = {}
        for categoryRecord in query:
            categoryID, level = categoryRecord
            if level not in self._categories:
                self._categories[level] = [categoryID]
            else:
                self._categories[level].append(categoryID)

        self._components = []

        if not custom:
            for item in database.fetchAll(SQL.MENU.GET_MAIN_COMPONENTS, (menuID,)):
                component = MenuComponent(*item)
                self._components.append(component)

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
    def can_customise(self):
        return self._can_customise

    @property
    def is_available(self):
        return "TODO: IMPLEMENT ME"

        if not self._is_available:
            return False

        # Check all the components, if there are not enough items in the stock for all of the components, return False
        for component in self._components:
            if somethingBad:
                return False
        return True

    @property
    def categories(self):
        return self._categories

    @property
    def components(self):
        return self._components

    def disable(self):
        database.update(SQL.MENU.DISABLE_ITEM, (self._id,))

    def enable(self):
        database.update(SQL.MENU.ENABLE_ITEM, (self._id,))

    def toMenuDict(self):
        components = []

        for item in self._components:
            components.append(dict(
                id=item.id,
                quantity=item.quantity,
                quantity_max=item.quantity_max
            ))

        return dict(
            id=self._id,
            name=self._name,
            price=self._price,
            can_customise=not not self._can_customise,
            is_available=self.is_available,
            #is_available=not not self._is_available,
            components=components,
            categories=self._categories
        )

    def toHistoricalDict(self):
        components = {}

        for item in self._components:
            components[item.id] = item.quantity

        return dict(
            id=self._id,
            name=self._name,
            price=self._price,
            components=components
        )


class CustomMenuItem(MenuItem):
    def __init__(self, customID, price=None):
        menuID = database.fetchOne(SQL.MENU.RESOLVE_CUSTOM_TO_MENU, (customID,))
        if not menuID:
            raise NoItemError(f"No custom menu item with id: {customID}")

        super().__init__(menuID[0], price, custom=True)
        
        if price:
            self._price = price

        for item in database.fetchAll(SQL.MENU.GET_CUSTOM_COMPONENTS, (customID,)):
            inventoryID = item[0]
            quantity = item[1]
            self._components.append(MenuComponent(inventoryID, quantity))

        # self._components
        # determineCustomDifference(customID)
    def toHistoricalDict(self):
        resp = super().toHistoricalDict()
        resp["custom"] = True
        return resp


class Order:
    def __init__(self, orderID):
        query = database.fetchOne(SQL.ORDERS.GET_ORDER_RAW, (orderID,))
        if not query:
            raise NoItemError(f"No order with id: {orderID}")

        self._id = orderID
        self._date, self._status = query
        self._price = 0

        self._items = []

        for foodItem in database.fetchAll(SQL.ORDERS.ORDER_ITEMS_0, (orderID,)):
            is_custom, customID, menuID, price = foodItem

            if is_custom:
                self._items.append(CustomMenuItem(customID, price))
            else:
                self._items.append(MenuItem(menuID, price))

            self._price += price

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

    def toDict(self):
        return dict(
            id=self._id,
            date=self._date,
            status=self._status,
            price=self._price,
            items=[menuItem.toHistoricalDict() for menuItem in self._items]
        )
