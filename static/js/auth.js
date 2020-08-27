// particlesJS("particles-js", {"particles":{"number":{"value":210 ,"density":{"enable":true,"value_area":1000.40724038582}},"color":{"value":"#61dafb"},"shape":{"type":"circle","stroke":{"width":2,"color":"#ffffff"},"polygon":{"nb_sides":10},"image":{"src":"img/github.svg","width":100,"height":100}},"opacity":{"value":0.7418002466091246,"random":false,"anim":{"enable":false,"speed":1,"opacity_min":0.1,"sync":false}},"size":{"value":3.945745992601726,"random":true,"anim":{"enable":false,"speed":0,"size_min":0,"sync":true}},"line_linked":{"enable":true,"distance":75,"color":"#61dafb","opacity":0.7696354753851935,"width":1.2827257923086561},"move":{"enable":true,"speed":2.156596794081381,"direction":"none","random":false,"straight":false,"out_mode":"bounce","bounce":false,"attract":{"enable":false,"rotateX":1042.214706250783,"rotateY":1200}}},"interactivity":{"detect_on":"canvas","events":{"onhover":{"enable":false,"mode":"repulse"},"onclick":{"enable":true,"mode":"push"},"resize":true},"modes":{"grab":{"distance":400,"line_linked":{"opacity":1, "distance": 64}},"bubble":{"distance":400,"size":40,"duration":2,"opacity":8,"speed":2},"repulse":{"distance":200,"duration":0.4},"push":{"particles_nb":4},"remove":{"particles_nb":2}}},"retina_detect":true});var count_particles, stats, update; stats = new Stats; stats.setMode(0); stats.domElement.style.position = 'absolute'; stats.domElement.style.left = '0px'; stats.domElement.style.top = '0px'; document.body.appendChild(stats.domElement); count_particles = document.querySelector('.js-count-particles'); update = function() { stats.begin(); stats.end(); if (window.pJSDom[0].pJS.particles && window.pJSDom[0].pJS.particles.array) { count_particles.innerText = window.pJSDom[0].pJS.particles.array.length; } requestAnimationFrame(update); }; requestAnimationFrame(update);;

const userNameField = document.querySelector('#username')

const validateUsername = (value, element) => {
  console.log(value)
  const errorMsg = document.querySelector('#username-feedback')
  if (value.length > 0) {
    fetch("/authenticate/validate-username/", {
      body: JSON.stringify({username: value}),
      method: "POST",
    }).then(res=> res.json()).then(data=> {
      console.log("data", data.username_error)
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
    element.classList.remove("is-invalid", "valid")
    errorMsg.style.display = "none";
  };
};
userNameField.addEventListener("keyup", (event)=> validateUsername(event.target.value, userNameField))


const validatePassword = (value, element) => {
  const errorMsg = document.querySelector("#password-feedback")
  const confirm = document.querySelector("#confirm")
  const confirmFeedback = document.querySelector("#confirm-feedback")
  console.log(value.length)
  if (value.length === 0) {
    errorMsg.innerText = "Please fill out your password."
  } else if (value.length < 7) {
    element.classList.remove("valid")
    element.classList.add("is-invalid")
    errorMsg.innerText = "Password must be more than 6 characters long."
    errorMsg.style.display = "block"
    confirm.value = ""
    confirm.placeholder = "Please fill out password above"
    confirm.classList.remove("is-invalid", "valid")
    confirmFeedback.style.display = "none"
    confirm.setAttribute("disabled", "true")
    // confirmFeedback.setAttribute()

  } else {
    element.classList.remove("is-invalid")
    element.classList.add("valid")
    errorMsg.style.display = "none"
    confirm.placeholder = ""
    confirm.removeAttribute("disabled")
  }
}

const passwordField = document.querySelector("#password")
passwordField.addEventListener("keyup", (event)=>validatePassword(event.target.value, passwordField))



const confirmPassword = (value, element)=> {
  const password = document.querySelector("#password")
  const errorMsg = document.querySelector("#confirm-feedback")
  console.log("password", password.value)
  console.log("value", value)
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




const confirmField = document.querySelector("#confirm")
confirmField.addEventListener("keyup", (event)=> confirmPassword(event.target.value, confirmField))









