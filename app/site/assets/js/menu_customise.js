let openCustomise;

(() => {
  let container = document.getElementById("customiseContainer");
  let modal = document.getElementById("modal");
  let tableBody = modal.querySelector(".content tbody");

  //

  const closeCustomise = function() {
    document.body.classList.remove("show-modal");
    for (let elem of document.querySelectorAll("[name=itemTotal]"))
      elem.innerText = "";
  };

  //

  window.addEventListener("click", evt => {
    if (evt.target == container) closeCustomise();
  });

  //
  function createIngredientElem(component, cb) {
    let elem = document.createElement("tr");

    let ingredient = GourmetBurgers._inventory[component.id];
    elem.ingredientID = ingredient.id;

    let name = document.createElement("td");
    name.innerText = `${ingredient.name} ($${priceToDecimal(
      ingredient.price
    )})`;
    elem.appendChild(name);

    let selectorCell = document.createElement("td");
    let selectorGroup = document.createElement("div");
    selectorGroup.classList.add("selector");

    let btnDecrement = document.createElement("button");
    btnDecrement.innerText = "-";
    btnDecrement.onclick = function() {
      if (selector.value > selector.min) selector.value--;
      updateAppearance();
      cb && cb();
    };

    let btnIncrement = document.createElement("button");
    btnIncrement.innerText = "+";
    btnIncrement.onclick = function() {
      if (selector.value < selector.max) selector.value++;
      updateAppearance();
      cb && cb();
    };

    const updateAppearance = function() {
      btnDecrement.disabled = selector.value == 0;
      btnDecrement.classList.toggle("disabled", btnDecrement.disabled);
      btnIncrement.disabled = selector.value == selector.max;
      btnIncrement.classList.toggle("disabled", btnIncrement.disabled);
    };

    let selector = document.createElement("input");
    selector.value = component.quantity;
    selector.min = 0;
    selector.max = component.quantity_max;
    selector.readOnly = true;

    selectorGroup.appendChild(btnDecrement);
    selectorGroup.appendChild(selector);
    selectorGroup.appendChild(btnIncrement);

    selectorCell.appendChild(selectorGroup);
    elem.appendChild(selectorCell);

    updateAppearance();

    return elem;
  }

  //

  const getData = function() {
    let data = {
      id: modal.menuID,
      quantity: 1,
      custom: true,
      items: {}
    };

    for (let componentElem of tableBody.querySelectorAll("tbody tr")) {
      data.items[componentElem.ingredientID] =  parseInt(componentElem.querySelector("input").value);
    }

    return data;
  };

  const updateItemTotal = function() {
    let priceString = priceToDecimal(GourmetBurgers.cart._calculate(getData()));
    for (let elem of document.querySelectorAll("[name=itemTotal]")) {
      elem.innerText = priceString;
    }
  };

  openCustomise = function(item) {
    document.body.classList.add("show-modal");
    modal.menuID = item.id;
    modal.querySelector(".header").innerText = item.name;

    tableBody.innerText = "";
    for (let component in item.components) {
      tableBody.appendChild(
        createIngredientElem(item.components[component], updateItemTotal)
      );
    }

    updateItemTotal();

    modal.querySelector("button[name=submit]").onclick = function() {
      try {
        GourmetBurgers.cart.addToOrder(modal.menuID, getData().items);
      } catch (err) {
        alert(err);
      }
      closeCustomise();
      updateTotal();
    };
  };
})();
