function ready() {
  let categoryMenu = document.querySelector(".categories ul");
  let grid = document.getElementById("menu-grid");

  let menu = GourmetBurgers._menu;

  let iso;

  let currentCategory = undefined;
  let menuCategories = [];
  let menuCategoriesMap = {};

  // Element creators

  function createMenuElem(menuID) {
    let item = menu[menuID];

    let container = document.createElement("div");
    container.classList.add("menu-container");
    container.menuID = menuID;

    let elem = document.createElement("div");
    elem.classList.add("menu-item");
    elem.innerText = item.name;

    let price = document.createElement("span");
    price.classList.add("price");
    price.innerText = item.price / 100;
    elem.appendChild(price);

    if (item.can_customise) {
      // TODO: Add customise
    }

    // Disable item if not available
    if (!item.available) elem.classList.add("disabled");

    let addToCart = document.createElement("div");
    addToCart.classList.add("add");
    addToCart.innerText = "Add to cart";
    elem.appendChild(addToCart);

    container.appendChild(elem);

    return container;
  }

  // Return a filter function for Isotope
  const getFilterFunction = categoryID => elem =>
    menu[elem.menuID].categories.hasOwnProperty(0) &&
    menu[elem.menuID].categories[0].indexOf(categoryID) > -1;

  // Select category
  function selectCategory(categoryID, fromSearch) {
    if (currentCategory != categoryID) {
      menuCategoriesMap[currentCategory].classList.remove("active");

      menuCategoriesMap[categoryID].classList.add("active");
      iso.arrange({
        filter: categoryID ? getFilterFunction(categoryID) : ""
      });
      currentCategory = categoryID;

      if (!fromSearch) {
        document.querySelector(".search .search-bar").value = "";
      }
    }
  }

  // Create category list element
  function createCategoryElem(categoryID) {
    let elem = document.createElement("li");
    elem.categoryID = categoryID;
    elem.innerText = GourmetBurgers._categories[categoryID];

    elem.addEventListener("click", () => selectCategory(categoryID));

    return elem;
  }

  //

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
    // Add `All Items`
    let elem = document.createElement("li");
    elem.addEventListener("click", () => selectCategory(undefined));
    elem.innerText = "All Items";
    elem.classList.add('active');
    menuCategoriesMap[undefined] = elem;
    categoryMenu.appendChild(elem);

    // Add other categories
    menuCategories.forEach(categoryID => {
      let elem = createCategoryElem(categoryID);
      menuCategoriesMap[categoryID] = elem;
      categoryMenu.appendChild(elem);
    });
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

  // Handle sorting
  document
    .querySelector(".search select")
    .addEventListener("change", function() {
      iso.arrange({ sortBy: this.value });
    });

  // Handle searching
  document.querySelector(".search input").addEventListener("input", function() {
    // TODO: Fuzzy search maybe?
    selectCategory(undefined, true);
    let needle = this.value.toLowerCase();
    iso.arrange({
      filter: elem => menu[elem.menuID].name.toLowerCase().indexOf(needle) > -1
    });
  });
}
