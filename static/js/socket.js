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




var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgba(255, 99, 132, 0)',
            borderColor: 'rgb(255, 99, 132)',
            data: [1000, 2500, 1250, 2003, 3000, 1000, 100]
        }]
    },

    // Configuration options go here
    options: {
      maintainAspectRatio: false,
      aspectRatio: 1,
       tooltips: {
          mode: 'index',
          intersect: false
       },
       hover: {
          mode: 'index',
          intersect: false,
          animationDuration: 100
       },
       legend: {
        display: false
       },
        title: {
          display: true,
          text: 'Market Spot Price'
        }
    }
});









