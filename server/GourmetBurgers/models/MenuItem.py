from lib import database
from .. import sql_GourmetBurgers as SQL
from .Exceptions import NoItemError
from .Ingredient import MenuIngredient, HistoricalIngredient, Ingredient


class MenuItemBase:
    def __init__(self, menuID, price=None):
        query = database.fetchOne(SQL.MENU.GET_MENU_ITEM_BASE, (menuID,))
        if not query:
            raise NoItemError(f"No menu item with id: {menuID}")
        self._id = menuID
        self._name, self._price = query

        query = database.fetchAll(SQL.MENU.GET_CATEGORIES, (menuID,))
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
        query = database.fetchOne(SQL.MENU.GET_MENU_ITEM_OPTIONS, (menuID,))
        self._can_customise, self._is_available, self._description = query

        for item in database.fetchAll(SQL.MENU.GET_MAIN_COMPONENTS, (menuID,)):
            component = MenuIngredient(*item)
            self._components.append(component)

    @property
    def can_customise(self):
        return self._can_customise

    def getComponentUsage(self):
        usage = {}
        for component in self._components:
            if component.id not in usage:
                usage[component.id] = 0
            usage[component.id] += component.quantity
        return usage

    @property
    def available(self):
        # Check all the components, if there are not enough items in the stock for all of the components, return False
        if not self._is_available:
            return False
        componentUsage = self.getComponentUsage()
        for componentID in componentUsage:
            print(
                f"{Ingredient(componentID).quantity} < {componentUsage[componentID]}")
            if Ingredient(componentID).quantity < componentUsage[componentID]:
                return False
        return True

    @available.setter
    def available(self, state):
        state = bool(state)
        self._is_available = state
        database.update(
            SQL.MENU.ENABLE_ITEM if state else SQL.MENU.DISABLE_ITEM, (self._id,))

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
            description = self._description,
            price=self._price,
            can_customise=not not self._can_customise,
            available=self.available,
            categories=self._categories,
            components=components
        )


class HistoricalMenuItem(MenuItemBase):
    def __init__(self, menuID, custom: bool, price):
        self._is_custom = custom

        if custom:
            customID = menuID
            menuID = database.fetchOne(
                SQL.MENU.RESOLVE_CUSTOM_TO_MENU, (customID,))
            if not menuID:
                raise NoItemError(f"No custom menu item with id: {customID}")

        super().__init__(menuID[0])
        self._price = price

        for item in database.fetchAll(SQL.MENU.GET_CUSTOM_COMPONENTS if custom else SQL.MENU.GET_MAIN_COMPONENTS, (customID,)):
            inventoryID = item[0]
            quantity = item[1]
            self._components.append(
                HistoricalIngredient(inventoryID, quantity))

    def toDict(self):
        components = {}

        for item in self._components:
            components[item.id] = item.quantity

        return dict(
            id=self._id,
            name=self._name,
            price=self._price,
            components=components,
            custom=self._is_custom
        )
