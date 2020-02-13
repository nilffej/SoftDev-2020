/*
Jeff Lin
SoftDev2 PD9
K06 -- Dot Dot Dot
2020-02-12
*/

var c = document.getElementById("playground");
var butt = document.getElementById("butt");
var clearbutt = document.getElementById("clear");
var switchbutt = document.getElementById("switch");

clearbutt.addEventListener("click", clear);
c.addEventListener("mousemove", showCoords);
c.addEventListener("mousedown", draw);
var first = false;

var peepee = c.getContext("2d");
var canvaspos = c.getBoundingClientRect();

function showCoords(event) {
  var x = event.clientX - canvaspos.x;
  var y = event.clientY - canvaspos.y;
  var coor = "X coords: " + x + ", Y coords: " + y;
  document.getElementById("demo").innerHTML = coor;
}

function draw(event) {
  var x = event.clientX - canvaspos.x;
  var y = event.clientY - canvaspos.y;
  if (first) {
    peepee.lineTo(x,y);
    peepee.stroke();
  }
  peepee.fillStyle = "black";
  peepee.beginPath();
  peepee.arc(x, y, 0, 0, 2 * Math.PI);
  peepee.stroke();
  peepee.fill();
  peepee.moveTo(x,y)
  if (!first) {
    first = true;
  }
}

function clear(event) {
  first = false;
  peepee.clearRect(0,0,c.width,c.height);
}

console.log(canvaspos);
