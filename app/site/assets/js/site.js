if (sessionStorage.getItem("loaded") != "true") {
  console.log("showing preloader");
  document.getElementById("loading").classList.add("active");
  window.addEventListener("load", () => {
    setTimeout(() => {
      sessionStorage.setItem("loaded", "true");
      document.getElementById("loading").classList.remove("active");
    }, 1500);
  });
} else {
  console.log("not showing preloader");
}

{
  let elemSlug = document.querySelector(
    `header .menu a[href="/${location.pathname.split("/", 2)[1]}"]`
  );
  elemSlug && elemSlug.classList.add("active");
}

function updateTotal() {
  if (GourmetBurgers.cart._data) {
    document.querySelector('.cart [name=orderTotal]').innerText = (GourmetBurgers.cart.calculate()/100).toFixed(2);
    document.querySelector('.cart').classList.add('active');
  } else {
    document.querySelector('.cart').classList.remove('active');
  }
}