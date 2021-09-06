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


var legendsvg = d3.select("#legend")
    .append("svg")
        .attr("width", 450)
        .attr("height", 600)

var getinfo = document.getElementById("info")
info = JSON.parse(getinfo.innerHTML)
getinfo.innerHTML = ""

var datasets = []
for (var i = 0; i <= 18; i++){
    var year = (1999 + i).toString()
    datasets.push(info[year])
}

function rangecolors(num){
    var colorlist = []
    for (var i = 0; i < num; i++){
        colorlist.push(d3.interpolateTurbo(i/num))
    }
    return colorlist
}

var index = 0
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

    document.getElementById("year").innerHTML = 1999 + index;

    legendsvg.selectAll("*").remove()
    legendlabels = []
    for (var i = 0; i < keys.length; i++){
        legendlabels.push(keys[i].concat(" - ",data[keys[i]]))
    }
    legendsvg.selectAll("mydots")
        .data(keys)
        .enter()
        .append("circle")
            .attr("cx", 100)
            .attr("cy", function(d,i){ return 100 + i*40}) // 100 is where the first dot appears. 25 is the distance between dots
            .attr("r", 7)
            .style("fill", function(d){ return color(d)})
    legendsvg.selectAll("mylabels")
        .data(legendlabels)
        .enter()
        .append("text")
            .attr("x", 120)
            .attr("y", function(d,i){ return 100 + i*40}) // 100 is where the first dot appears. 25 is the distance between dots
            .style("fill", function(d){ return color(d)})
            .text(function(d){ return d})
            .attr("text-anchor", "left")
            .style("alignment-baseline", "middle")
            .attr("font-size","20px")

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
var gogo = setInterval(function() { update(datasets[index]) }, 2000)
