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

const arr = () => {
  let now = new Date()
  let minutes
  let hour
  let arr = []
  let setter
  for(let i=0; i < 7; i++) {
    setter = new Date(now - i * 60000)
    minutes = setter.getMinutes()
    hours = setter.getHours()
    if (minutes < 10) minutes = '0' + minutes.toString()
    if (hours < 10) hour = '0' + hours.toString()
    minutes.toString()
    hour.toString()
    arr.unshift(`${hour}:${minutes}`)
  }
  return arr
}

labels = arr()

const updateTime = () => {
  let now = new Date()
  let minutes = now.getMinutes()
  let hours = now.getHours()
  if (minutes < 10) minutes = '0' + minutes.toString()
  if (hours < 10) hour = '0' + hours.toString()
  minutes.toString()
  hour.toString()

  dataObj.data.labels.push(`${hour}:${minutes}`)
  dataObj.data.labels.shift()
  chart.update()
  console.log(`${hour}:${minutes}`)
}

console.log(60000 - new Date().getSeconds()*1000)
// 60000 - new Date().getSeconds()*1000


var dataObj = {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: labels,
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
          animationDuration: 0
       },
       legend: {
        display: false
       },
        title: {
          display: true,
          text: '。Live Data',
          position: 'top',
          fontColor: 'rgb(255, 99, 132)',
          fontSize: 20
        },
        scales: {
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: '$USD / BTC',
              fontSize: 18
            }
          }]
        }
      }
  }

var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, dataObj);



setInterval(function() {
  updateTime();
}, 60000 - new Date().getSeconds()*1000);






