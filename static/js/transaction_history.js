var accountId = document.querySelector("h3").getAttribute("account-id")
console.log(accountId)

let arr = ['100000.00']
let emptyArr = ['']

fetch(`/accounts/transaction-history/${accountId}/`, {
  method: 'POST',
  body: {
    data: 'ok'
  }
}).then(res=>res.json())
  .then(data=>{
    console.log(data.list)
    let float
    let acc
    let index
    for(let i=0; i<data.list.length; i++) {
      console.log("..................................................")
      float = data.list[i].usd_gained
      console.log("float--______>", float)
      acc = (parseFloat(arr[arr.length-1]) + parseFloat(float)).toString()
      console.log('acc-----------------_>', acc)
      index = acc.indexOf('.') + 5
      // console.log('index of dot ----------------__>', index)
      // console.log(acc.slice(0, index))
      if (acc.includes('.')) {
        acc = acc.slice(0, index)
        arr.push(acc)
      } else {
        arr.push(acc + '.00')
      }
      emptyArr.push('')
      console.log("acc again", acc)
      console.log("........................................................")
    }
    dataObj.data.datasets[0].data = arr
    dataObj.data.labels = emptyArr
    chart.update()
    console.log(arr)
  })



var dataObj = {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: [],
        datasets: [{
            label: 'Balance',
            backgroundColor: 'rgba(255, 99, 132, 0)',
            borderColor: 'rgb(255, 99, 132)',
            data: [2,2,2,2,2,2,2,2],
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
          text: 'Account Balance',
          position: 'top',
          fontColor: 'rgb(255, 99, 132)',
          fontSize: 20
        },
        scales: {
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Account Balance (USD)',
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


var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, dataObj)
