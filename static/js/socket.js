// console.log(window.location)

// let endpoint = ''


// if (window.location.protocol === "https:") {
//   endpoint = `wss://${window.location.host}${window.location.pathname}`
// } else {
//   endpoint = `ws://${window.location.host}${window.location.pathname}`
// }
const host = 'http://127.0.0.1:8000/api/price'

function formatDate() {
  const today = new Date();
  const dd = String(today.getDate()).padStart(2, '0');
  const mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  const yyyy = today.getFullYear();

  return [yyyy, mm, dd].join('-');
}


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

var thumb = document.querySelector("#thumb")
// console.log(endpoint)
const endpoint = "ws://localhost:8000/ws/priceData/"

var dataObj = {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: labels,
        datasets: [{
            label: 'Price',
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
        },
        elements: {
          line: {
            tension: 0
          }
        }
      }
  }

var hisObj = {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: [],
        datasets: [{
            label: 'Price',
            backgroundColor: 'rgba(255, 99, 132, 0)',
            borderColor: 'rgb(255, 99, 132)',
            data: [],
            pointRadius: 0
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
          }],
          xAxes: [{
            scaleLabel: {
              ticks: {
                stepValue: 3,
                steps: 5
              }
            }
          }]
        },
          elements: {
            line: {
              tension: 0
            }
          }
        }
      }


var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, dataObj);

console.log(ctx)

var htx = document.getElementById('historicalChart').getContext('2d')
var hisChart = new Chart(htx, hisObj)

console.log(htx)


fetch(`${host}`).then(res=>res.json()).then(data=>{
  // console.log(data.slice(data.length-7, data.length))
  if (data.length > 7) {
    const diff = document.querySelector("#difference")
    const statement = document.querySelector("#price-statement")
    data = data.slice(data.length-31, data.length)
    console.log(data)
    data = data.map(x=> x.USD)
    dataObj.data.datasets[0].data = data
    const value = data[data.length - 1]
    const old = data[data.length - 2]
    difference = Math.round((value-old) * 100) / 100
    console.log(diff)
    console.log(difference)
    if (difference > 0) {
      diff.innerText = `+${difference} USD`
      diff.style.color = "#3BE2AB"
      statement.innerText = `An increase of ${difference} USD per BTC compared to last minute.`
      thumb.classList.remove("fa-angle-double-down")
      thumb.classList.add("fa-angle-double-up")
      thumb.style.color = "#3BE2AB"
    } else if (difference < 0) {
      diff.innerText = `${difference} USD`
      diff.style.color = "rgb(255, 99, 132)"
      statement.innerText = `A decrease of ${Math.abs(difference)} USD per BTC compared to last minute.`
      thumb.classList.add("fa-angle-double-down")
      thumb.classList.remove("fa-angle-double-up")
      thumb.style.color = "rgb(255, 99, 132)"
    }
    chart.update()
    priceText.innerText = `1 BTC = ${value} USD`
  }
})

const weekFromNow = (dateNow) => {
  const d = new Date(dateNow);
  console.log(d.toLocaleDateString());
  d.setDate(d.getDate() - 10);
  console.log(d.toLocaleDateString())
  return d.toLocaleDateString().split('/').reverse().join('-')
}

const renderChart = async (startFrom, dateNow) => {
  // const dateNow = await formatDate()
  // console.log("------->", dateNow)
  // const startFrom = weekFromNow(dateNow)
  // console.log("---->", startFrom)
  fetch(`https://api.coindesk.com/v1/bpi/historical/close.json?start=${startFrom}&end=${dateNow}`)
    .then(res=>res.json())
    .then(data=>{
      let x = []
      let y = []
      for (const [key, value] of Object.entries(data.bpi)) {
        x.push(key)
        y.push(value)
      }
      console.log(x)
      y.push(['', '', ''])
      hisObj.data.labels = x
      hisObj.data.datasets[0].data = y
      hisChart.update()
    })
}

const dateNow = formatDate()
const lastWeek = weekFromNow(dateNow)

renderChart(lastWeek, dateNow)

const week = document.querySelector("#pills-week-tab")
const month = document.querySelector("#pills-month-tab")
const all = document.querySelector("#pills-max-tab")
const pad = document.querySelector("#pad-change")

week.addEventListener("click", ()=>{
  if (!week.classList.contains('active')) {
    const dateNow = formatDate()
    const lastWeek = weekFromNow(dateNow)
    renderChart(lastWeek, dateNow)
    // pad.classList.remove('pb-2')
    // pad.classList.add('pb-5')
  }
})

const monthFromNow = (dateNow) => {
  const d = new Date(dateNow);
  console.log(d.toLocaleDateString());
  d.setDate(d.getDate() - 34);
  console.log(d.toLocaleDateString())
  return d.toLocaleDateString().split('/').reverse().join('-')
}


month.addEventListener("click", ()=>{
  if (!month.classList.contains('active')) {
    const dateNow = formatDate()
    const lastmonth = monthFromNow(dateNow)
    renderChart(lastmonth, dateNow)
    // pad.classList.remove('pb-5')
    // pad.classList.add('pb-2')
  }
})

all.addEventListener("click", ()=>{
  if (!all.classList.contains('active')) {
    const dateNow = formatDate()
    const start = '2016-01-21'
    renderChart(start, dateNow)
    // pad.classList.remove('pb-5')
    // pad.classList.add('pb-2')
  }
})


var priceText = document.querySelector("#price-text")

const socket = new WebSocket(endpoint)
socket.onmessage = (event) => {
  value = (JSON.parse(event.data).value)[0]
  console.log(value)
  if (value !== null) {
    const diff = document.querySelector("#difference")
    const statement = document.querySelector("#price-statement")
    const old = dataObj.data.datasets[0].data[30]
    difference = Math.round((value-old) * 100) / 100
    value.toString()
    dataObj.data.datasets[0].data.shift()
    dataObj.data.datasets[0].data.push(value)
    chart.update()
    priceText.innerText = `1 BTC = ${value} USD`
    if (difference > 0) {
      diff.innerText = `+${difference} USD`
      diff.style.color = "#3BE2AB"
      statement.innerText = `An increase of ${difference} USD per BTC compared to last minute.`
      thumb.classList.remove("fa-angle-double-down")
      thumb.classList.add("fa-angle-double-up")
      thumb.style.color = "#3BE2AB"
    } else if (difference < 0) {
      diff.innerText = `${difference} USD`
      diff.style.color = "rgb(255, 99, 132)"
      statement.innerText = `A decrease of ${Math.abs(difference)} USD per BTC compared to last minute.`
      thumb.classList.add("fa-angle-double-down")
      thumb.classList.remove("fa-angle-double-up")
      thumb.style.color = "rgb(255, 99, 132)"
    }
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






