// Preloader
if (sessionStorage.getItem("loaded") != "true") {
  document.getElementById("loading").classList.add("active");
  window.addEventListener("load", () => {
    setTimeout(() => {
      sessionStorage.setItem("loaded", "true");
      document.getElementById("loading").classList.remove("active");
    }, 1500);
  });
}

// Update element slug
{
  let elemSlug = document.querySelector(
    `header .menu a[href="/${location.pathname.split("/", 2)[1]}"]`
  );
  elemSlug && elemSlug.classList.add("active");
}

// Display the order total
function updateTotal() {
  if (GourmetBurgers.cart._data) {
    document.querySelector('.cart [name=orderTotal]').innerText = priceToDecimal(GourmetBurgers.cart.calculate());
    document.querySelector('.cart').classList.add('active');
  } else {
    document.querySelector('.cart').classList.remove('active');
  }
}

const priceToDecimal = price => parseFloat(price/100).toFixed(2);

let resetState = document.createElement('div');
resetState.innerHTML = '<button style="position:fixed;left:0;top:0" onclick="localStorage.clear();location.reload();">Click here to reset demo state</button>'
document.body.appendChild(resetState);
