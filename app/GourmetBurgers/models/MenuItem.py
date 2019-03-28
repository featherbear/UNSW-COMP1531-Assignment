from .Exceptions import NoItemError
from .Ingredient import MenuIngredient, HistoricalIngredient, Ingredient
from ._SQLBase import SQLBase


class MenuItemBase(SQLBase):
    def __init__(self, menuID, price=None):
        query = self._db.fetchOne(self._SQL.MENU.GET_MENU_ITEM_BASE, (menuID,))
        if not query:
            raise NoItemError(f"No menu item with id: {menuID}")
        self._id = menuID
        self._name, self._price = query

        query = self._db.fetchAll(self._SQL.MENU.GET_CATEGORIES, (menuID,))
        self._categories = {}
        for categoryRecord in query:
            categoryID, level = categoryRecord
            if level not in self._categories:
                self._categories[level] = [categoryID]
            else:
                self._categories[level].append(categoryID)

        self._components = []

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
    def categories(self):
        return self._categories

    @property
    def components(self):
        return self._components


class MenuItem(MenuItemBase):
    def __init__(self, menuID):
        super().__init__(menuID)
        query = self._db.fetchOne(
            self._SQL.MENU.GET_MENU_ITEM_OPTIONS, (menuID,))
        self._can_customise, self._is_available, self._description = query

        for item in self._db.fetchAll(self._SQL.MENU.GET_MAIN_COMPONENTS, (menuID,)):
            component = MenuIngredient(*item)
            self._components.append(component)

    @property
    def can_customise(self):
        return self._can_customise

    def getComponentUsage(self):
        usage = {}
        for component in self._components:
            usage[component.id] = component.quantity
            # if component.id not in usage:
            #     usage[component.id] = 0
            # usage[component.id] += component.quantity
        return usage

    @property
    def available(self):
        # Check all the components, if there are not enough items in the stock for all of the components, return False
        if not self._is_available:
            return False
        componentUsage = self.getComponentUsage()
        for componentID in componentUsage:
            if Ingredient(componentID).quantity < componentUsage[componentID]:
                return False
        return True

    @available.setter
    def available(self, state):
        state = bool(state)
        self._is_available = state
        self._db.update(
            self._SQL.MENU.ENABLE_ITEM if state else self._SQL.MENU.DISABLE_ITEM, (self._id,))

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
            description=self._description,
            price=self._price,
            can_customise=not not self._can_customise,
            available=self.available,
            categories=self._categories,
            components=components
        )


class HistoricalMenuItem(MenuItemBase):
    def __init__(self, menuID, custom: bool, quantity, price):
        self._is_custom = custom
        self._quantity = quantity

        if custom:
            customID = menuID
            menuID = self._db.fetchOne(
                self._SQL.MENU.RESOLVE_CUSTOM_TO_MENU, (customID,))
            if not menuID:
                raise NoItemError(f"No custom menu item with id: {customID}")
            menuID = menuID[0]

        super().__init__(menuID)
        self._price = price

        if custom:

            for item in self._db.fetchAll(self._SQL.MENU.GET_CUSTOM_COMPONENTS, (customID,)):
                inventoryID = item[0]
                quantity = item[1]
                self._components.append(
                    HistoricalIngredient(inventoryID, quantity))
        else:

            for item in self._db.fetchAll(self._SQL.MENU.GET_MAIN_COMPONENTS, (menuID,)):
                inventoryID = item[0]
                quantity = item[1]
                self._components.append(
                    HistoricalIngredient(inventoryID, quantity))

    def toDict(self):
        components = {}

        for item in self._components:
            components[item.id] = item.quantity

        resp = dict(
            id=self._id,
            name=self._name,
            quantity=self._quantity,
            price=self._price,
        )

        if self._is_custom:
            resp.update(dict(
                components=components,
                custom=self._is_custom)
            )
        return resp
