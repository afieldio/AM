google.load("visualization", "1", {packages:["gauge"]});
google.setOnLoadCallback(drawWTChart);
function drawWTChart() {

  var data = google.visualization.arrayToDataTable([
    ['Label', 'Value'],
    ['', 80],
  ]);

  var options = {
    width: 300, height: 300,
    redFrom: 90, redTo: 100,
    yellowFrom:75, yellowTo: 90,
    minorTicks: 5
  };

  var chart = new google.visualization.Gauge(document.getElementById('chart_wt'));

  chart.draw(data, options);

}

google.setOnLoadCallback(drawATChart);
function drawATChart() {

  var data = google.visualization.arrayToDataTable([
    ['Label', 'Value'],
    ['', 80],
  ]);

  var options = {
    width: 300, height: 300,
    redFrom: 90, redTo: 100,
    yellowFrom:75, yellowTo: 90,
    minorTicks: 5
  };

  var chart = new google.visualization.Gauge(document.getElementById('chart_at'));

  chart.draw(data, options);

}

console.log("width");