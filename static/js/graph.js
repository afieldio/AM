(function () {

'use strict';

  var data = [{
    "sale": "202",
    "year": "2000"
}, {
    "sale": "215",
    "year": "2001"
}, {
    "sale": "179",
    "year": "2002"
}, {
    "sale": "199",
    "year": "2003"
}, {
    "sale": "134",
    "year": "2003"
}, {
    "sale": "176",
    "year": "2010"
}];



  var vis = d3.select("#graph"),
    WIDTH = 1000,
    HEIGHT = 500,
    MARGINS = {
      top:20,
      right:20,
      bottom:20,
      left:100,
    },

    xScale = d3.scale.linear().range([MARGINS.left, WIDTH-MARGINS.right]).domain([2000,2010]),

    yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([134,215]),

    xAxis = d3.svg.axis().scale(xScale),

    yAxis = d3.svg.axis()
      .scale(yScale)
      .orient("left");

    vis.append("svg:g")
      .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
      .call(xAxis);

    vis.append("svg:g")
      .attr("transform", "translate(" + (MARGINS.left) + ",0)")
      .call(yAxis);

var getInt = function (attr) {
  var num = vis.attr('data-' + attr);

  return parseInt(num, 10);
};

var data = getInt(graph)

console.log(data.)

var lineGen = d3.svg.line()
  .x(function(d){
    return xScale(d.dt);
  })
  .y(function(d){
    return yScale(d.temp);
  })
  .interpolate("basis");

vis.append('svg:path')
  .attr('d', lineGen(data))
  .attr('stroke', 'green')
  .attr('stroke-width',2)
  .attr('fill','none');
}());