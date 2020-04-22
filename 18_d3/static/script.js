// set the dimensions and margins of the graph
var width = 450
    height = 450
    margin = 10

// The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
var radius = Math.min(width, height) / 2 - margin

// append the svg object to the div called 'my_dataviz'
var svg = d3.select("#pie")
    .append("svg")
        .attr("width", width)
        .attr("height", height)
    .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

// create 2 data_set
// JACKSON WORK HERE
var data1 = {a: 9, b: 20, c:30, d:8, e:12}
var data2 = {a: 6, b: 16, c:20, d:14, e:19, f:12}

var datasets = [data1, data2]
var index = 0

function rangecolors(num){
    var colorlist = []
    for (var i = 0; i < num; i++){
        colorlist.push(d3.interpolateTurbo(i/num))
    }
    return colorlist
}

// A function that create / update the plot for a given variable:
function update(data) {
    if (index == datasets.length) {
        clearInterval(gogo)
        return
    }

    // set the color scale
    var keys = Object.keys(data)
    console.log(keys)
    var color = d3.scaleOrdinal()
        .domain(keys)
        .range(rangecolors(keys.length));
    
    document.getElementById("year").innerHTML = 2069

    // Compute the position of each group on the pie:
    var pie = d3.pie()
        .value(function(d) {return d.value; })
        .sort(function(a, b) { console.log(a) ; return d3.ascending(a.key, b.key);} ) // This make sure that group order remains the same in the pie chart
    var data_ready = pie(d3.entries(data))

    // map to data
    var u = svg.selectAll("path")
        .data(data_ready)

    // Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
    u.enter()
        .append('path')
        .merge(u)
        .transition()
        .duration(1000)
        .attr('d', d3.arc()
            .innerRadius(0)
            .outerRadius(radius)
        )
        .attr('fill', function(d){ return(color(d.data.key)) })
        .attr("stroke", "white")
        .style("stroke-width", "2px")
        .style("opacity", 1)

    // remove the group that is not present anymore
    u.exit().remove()
    
    index += 1
}

update(datasets[0])
var gogo = setInterval(function() { update(datasets[index]) }, 3000)