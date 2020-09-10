// console.log(window.location)

// let endpoint = ''


// if (window.location.protocol === "https:") {
//   endpoint = `wss://${window.location.host}${window.location.pathname}`
// } else {
//   endpoint = `ws://${window.location.host}${window.location.pathname}`
// }

// console.log(endpoint)
const endpoint = "ws://localhost:8000/ws/priceData/"

const socket = new WebSocket(endpoint)
socket.onmessage = (event) => {
  console.log(event)
}

socket.onopen = (event) => {
  console.log(event)
}

socket.onerror = (event) => {
  console.log(event)
}

socket.onclose = (event) => {
  console.log(event)
}
