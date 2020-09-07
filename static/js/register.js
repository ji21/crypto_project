
const userNameField = document.querySelector('#username')
const passwordField = document.querySelector("#password")
const confirmField = document.querySelector("#confirm")
const emailField = document.querySelector("#email")
const toggle = document.querySelector("#toggle")
const submit = document.querySelector("#submit")
const form = document.querySelector("form")



const validateUsername = (value, element) => {
  // console.log(value.length)
  const load = document.querySelector('#username-load')
  const errorMsg = document.querySelector('#username-feedback')
  const submit = document.querySelector("#submit")
  console.log(value.length)
  if (value.length > 0) {
    console.log(submit)
    submit.removeAttribute("disabled")
    // console.log(load.classList)
    load.classList.remove('hide')
    // console.log(load.classList)
    fetch("/authenticate/validate-username/", {
      body: JSON.stringify({username: value}),
      method: "POST",
    }).then(res=> res.json()).then(data=> {
      load.classList.add('hide')
      console.log("data", data)
      if (data.username_error) {
        element.classList.remove("valid")
        element.classList.add("is-invalid")
        errorMsg.style.display = "block";
        errorMsg.innerText = `${data.username_error}`
      } else {
        element.classList.remove("is-invalid")
        element.classList.add("valid")
        errorMsg.style.display = "none";
      }
    });
  } else {
    submit.setAttribute("disabled", "true")
    element.classList.remove("is-invalid", "valid")
    errorMsg.style.display = "none";
  };
};


const validatePassword = (value, element) => {
  const errorMsg = document.querySelector("#password-feedback")
  const confirm = document.querySelector("#confirm")
  const confirmFeedback = document.querySelector("#confirm-feedback")
  // console.log(value.length)
  if (value.length === 0) {
    element.classList.remove("valid")
    element.classList.add("is-invalid")
    errorMsg.innerText = "Please fill out your password."
    errorMsg.style.display = "block"
    confirm.value = ""
    confirm.placeholder = "Please fill out password above"
    confirm.classList.remove("is-invalid", "valid")
    confirmFeedback.style.display = "none"
  } else if (value.length < 7) {
    element.classList.remove("valid")
    element.classList.add("is-invalid")
    errorMsg.innerText = "Password must be more than 6 characters long."
    errorMsg.style.display = "block"
    confirm.value = ""
    confirm.placeholder = "Please fill out password above"
    confirm.classList.remove("is-invalid", "valid")
    confirmFeedback.style.display = "none"
  } else {
    // console.log("value", value)
    // console.log("confirm.value", confirm.value)
    if (value === confirm.value) {
      confirmFeedback.style.display = "none"
      confirm.classList.remove("is-invalid")
      confirm.classList.add("valid")
    } else if (confirm.value.length >0) {
      confirmFeedback.style.display = "block"
      confirm.classList.remove("valid")
      confirm.classList.add("is-invalid")
    }
    element.classList.remove("is-invalid")
    element.classList.add("valid")
    errorMsg.style.display = "none"
    confirm.placeholder = ""
  }
}



const confirmPassword = (value, element)=> {
  const password = document.querySelector("#password")
  const errorMsg = document.querySelector("#confirm-feedback")
  // console.log("password", password.value)
  // console.log("value", value)
  if (password.value === value) {
    element.classList.remove("is-invalid")
    element.classList.add("valid")
    errorMsg.style.display = "none"
  } else {
    element.classList.remove("valid")
    element.classList.add("is-invalid")
    errorMsg.style.display = "block"
    errorMsg.innerText = "Passwords do not match. (check if capitalisation is correct)"
  }
}




const validateEmail = (value, element) => {
  const submit = document.querySelector("#submit")
  const errorMsg = document.querySelector("#email-feedback")
  const load = document.querySelector("#email-load")
  load.classList.remove('hide')
  fetch("/authenticate/validate-email/", {
    body: JSON.stringify({email: value}),
    method: "POST",
  }).then(res=>
    res.json()
    // load.classList.add('hide')
  ).then(data=> {
    console.log(data)
    load.classList.add('hide')
    if (data.email_error) {
      errorMsg.style.display = "block"
      errorMsg.innerText = `${data.email_error}`
      element.classList.add("is-invalid")
      element.classList.remove("valid")
    } else {
      errorMsg.style.display = "none"
      element.classList.remove("is-invalid")
      element.classList.add("valid")
    }
  })
}



const togglePw = (element, e) => {
  console.log(e)
  if (element.innerText === "(show)") {
    element.innerText = "(hide)"
    e.type = "text"
    confirmField.type ="text"
  } else {
    element.innerText = "(show)"
    e.type = "password"
    confirmField.type ="password"
  }
}


form.addEventListener("submit", (event)=> {
})
toggle.addEventListener("click", ()=> togglePw(toggle, passwordField))
passwordField.addEventListener("keyup", (event)=>validatePassword(event.target.value, passwordField))
userNameField.addEventListener("keyup", (event)=> validateUsername(event.target.value, userNameField))
emailField.addEventListener("keyup", (event)=>validateEmail(event.target.value, emailField))
confirmField.addEventListener("keyup", (event)=> confirmPassword(event.target.value, confirmField))
