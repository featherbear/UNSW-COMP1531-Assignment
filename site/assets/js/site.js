document.getElementById("loading").classList.remove("active");
{
  let elemSlug = document.querySelector(`header .menu a[href="/${location.pathname.split("/", 2)[1]}"]`);
  elemSlug && elemSlug.classList.add('active');
}
