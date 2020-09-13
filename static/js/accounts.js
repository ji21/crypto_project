const add = document.querySelector("#add")
console.log(add)

var host = '/accounts/'

add.addEventListener("click", ()=> {
  const name = document.querySelector("#name")
  const value = name.value
  const error = document.querySelector("#error")
  if (value.replace(/ /g,'') !== "") {
    fetch(host, {
      body: JSON.stringify({name: value}),
      method: "POST"
    }).then(res=>res.json())
      .then(data=> {
        console.log(data)
        // window.location.reload()
    })
  } else {
    console.log(name)
    name.classList.add("is-invalid")
    error.style.display = "block"
  }
})
