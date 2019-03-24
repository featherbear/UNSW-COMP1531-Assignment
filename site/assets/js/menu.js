function ready() {
  let categoryMenu = document.querySelector(".categories ul");
  let grid = document.getElementById("menu-grid");

  let menu = GourmetBurgers._menu;

  let iso;

  // Element creators

  function createMenuElem(menuID) {
    let item = menu[menuID];

    let elem = document.createElement("div");
    elem.classList.add("menu-item");
    elem.menuID = menuID;
    elem.innerText = item.name;

    let price = document.createElement("span");
    price.classList.add("price");
    price.innerText = item.price / 100;
    elem.appendChild(price);

    return elem;
  }

  const getFilterFunction = categoryID => elem =>
    menu[elem.menuID].categories.hasOwnProperty(0) &&
    menu[elem.menuID].categories[0].indexOf(categoryID) > -1;

  function createCategoryElem(categoryID) {
    let elem = document.createElement("li");
    elem.categoryID = categoryID;
    elem.innerText = GourmetBurgers._categories[categoryID];

    let filterFunction = getFilterFunction(categoryID);
    elem.addEventListener("click", function() {
      iso.arrange({
        filter: filterFunction
      });
    });

    return elem;
  }

  //

  menuCategories = [];

  Object.values(menu).forEach(menuItem => {
    // Add level 0 categories of the current item to `menuCategories`
    if (menuItem.categories.hasOwnProperty(0))
      menuCategories.push(...menuItem.categories[0]);

    // Add element to DOM
    grid.appendChild(createMenuElem(menuItem.id));
  });

  // Extract unique categoryIDs from `menuCategories`
  menuCategories = Array.from(new Set(menuCategories));

  // Populate category list
  {
    let elem = document.createElement("li");
    elem.addEventListener("click", function() {
      iso.arrange({ filter: () => true });
    });
    elem.innerText = "All Items";
    categoryMenu.appendChild(elem);

    // Add other categories
    menuCategories.forEach(categoryID =>
      categoryMenu.appendChild(createCategoryElem(categoryID))
    );
  }

  // Initialise Isotope
  iso = new Isotope(grid, {
    getSortData: {
      nameAsc: elem => menu[elem.menuID].name,
      nameDesc: elem => menu[elem.menuID].name,
      priceAsc: elem => menu[elem.menuID].price,
      priceDesc: elem => menu[elem.menuID].price
    },
    sortAscending: {
      nameAsc: true,
      nameDesc: false,
      priceAsc: true,
      priceDesc: false
    }
  });
}
