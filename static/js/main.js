//https://www.w3schools.com/howto/howto_js_navbar_sticky.asp
const adjustHeight = () => {
  const fadeHeight = document.querySelector("#fade-height");
  fadeHeight.classList.remove("hidden");
}

const tab = document.querySelector("#myTab")
tab.addEventListener("click", (event)=> {
  if (event.srcElement.getAttribute("data-toggle")==="tab") {
    adjustHeight();
  }
})

