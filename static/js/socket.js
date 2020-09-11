// console.log(window.location)

// let endpoint = ''


// if (window.location.protocol === "https:") {
//   endpoint = `wss://${window.location.host}${window.location.pathname}`
// } else {
//   endpoint = `ws://${window.location.host}${window.location.pathname}`
// }
const host = 'http://127.0.0.1:8000/api/price/'

const arr = () => {
  let now = new Date()
  let minutes
  let hours
  let arr = []
  let setter
  for(let i=0; i < 31; i++) {
    setter = new Date(now - i * 60000)
    minutes = setter.getMinutes()
    hours = setter.getHours()
    if (minutes < 10) minutes = '0' + minutes.toString()
    if (hours < 10) hours = '0' + hours.toString()
    minutes.toString()
    hours.toString()
    arr.unshift(`${hours}:${minutes}`)
  }
  arr.push([''])
  arr.push([''])
  return arr
}

labels = arr()

// console.log(endpoint)
const endpoint = "ws://localhost:8000/ws/priceData/"

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
            data: [],
            pointRadius: 3,
            pointHoverRadius: 6
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
          text: '。Live Data - updates every minute.',
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
              // ticks: {
              //   beginAtZero: false,
              //   steps: 10,
              //   stepValue: 5,
              //   max: 100000
              // }
            }
          }]
        }
      }
  }
var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, dataObj);



fetch('http://127.0.0.1:8000/api/price').then(res=>res.json()).then(data=>{
  // console.log(data.slice(data.length-7, data.length))
  if (data.length > 7) {
    data = data.slice(data.length-31, data.length)
    data = data.map(x=> x.market_price)
    dataObj.data.datasets[0].data = data
    chart.update()
  }
})



const socket = new WebSocket(endpoint)
socket.onmessage = (event) => {
  value = (JSON.parse(event.data).value)
  if (value !== null) {
    value.toString()
    console.log(value)
    console.log(dataObj.data.datasets[0].data)
    dataObj.data.datasets[0].data.shift()
    dataObj.data.datasets[0].data.push(value)
    chart.update()
  }
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







const updateTime = () => {
  let now = new Date()
  let minutes = now.getMinutes()
  let hours = now.getHours()
  if (minutes < 10) minutes = '0' + minutes.toString()
  if (hours < 10) hours = '0' + hours.toString()
  minutes.toString()
  hours.toString()
  dataObj.data.labels[31] = `${hours}:${minutes}`
  dataObj.data.labels.push([''])
  dataObj.data.labels.shift()
  chart.update()
  console.log(`${hours}:${minutes}`)
}

console.log(60000 - new Date().getSeconds()*1000)
// 60000 - new Date().getSeconds()*1000





setInterval(function() {
  if (new Date().getSeconds() === 0)updateTime();
}, 1000);






