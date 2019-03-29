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
