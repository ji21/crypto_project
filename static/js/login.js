const signinPassword = document.querySelector("#signin-password")
const signinToggle = document.querySelector("#signin-toggle")


const togglePw = (element, e) => {
  console.log(e)
  if (element.innerText === "(show)") {
    element.innerText = "(hide)"
    e.type = "text"
  } else {
    element.innerText = "(show)"
    e.type = "password"
  }
}

signinToggle.addEventListener("click", ()=>togglePw(signinToggle, signinPassword))
