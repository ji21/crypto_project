const add = document.querySelector("#add")
console.log(add)

var host = '/accounts/'

add.addEventListener("click", ()=> {
  const name = document.querySelector("#name")
  const value = name.value
  const error = document.querySelector("#error")
  if (value.replace(/ /g,'') !== "" && value.length < 13) {
    fetch(host, {
      body: JSON.stringify({name: value}),
      method: "POST"
    }).then(res=>res.json())
      .then(data=> {
        console.log(data)
        window.location.reload()
    })
  } else if (value.length > 12) {
    name.classList.add("is-invalid")
    error.style.display = "block"
    error.innerText = "Name should be at most 12 characters long."
  } else {
    console.log(name)
    name.classList.add("is-invalid")
    error.style.display = "block"
    error.innerText = "You must enter a name"
  }
})

const deleteAccount = (event) => {
  id = event.target.id
}

document.querySelectorAll(".fa-trash-alt").forEach(i =>
    i.addEventListener("click", (event) => {
      id = event.target.id
      fetch(host, {
        body: JSON.stringify({id: id}),
        method: "DELETE"
      }).then(res=>res.json())
        .then(data=> {
          console.log(data)
          window.location.reload()
      })
    }
  ));


document.querySelectorAll(".accounts").forEach(account => {
  account.addEventListener("click", (event)=> console.log(event.target))
})







