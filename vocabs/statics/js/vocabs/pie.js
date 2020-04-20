//pie
var ctxP = document.getElementById("pieChart").getContext('2d');
var ratio = JSON.parse(document.getElementById('ratio').textContent);

var wrong = ratio['false'];
var right = ratio['true'];
var total = wrong + right;
var wrong_percent = (wrong * 100 / total).toFixed(2);
var right_percent = (right * 100 / total).toFixed(2);


var myPieChart = new Chart(ctxP, {
  type: 'pie',
  data: {
    labels: ["Wrong: " + wrong, "Right: " + right],
    datasets: [{
      data: [ wrong_percent, right_percent ],
      backgroundColor: ["#F7464A", "#46BFBD"],
      hoverBackgroundColor: ["#FF5A5E", "#5AD3D1"]
    }]
  },
  options: {
    responsive: true
  }
});