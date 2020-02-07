/*
Jeff Lin
SoftDev2 PD9
K05 -- ...and I want to Paint It Better
2020-02-07
*/

/*
  e.preventDefault()
    stops an element from performing its default action
    Ex: does not let a check box be checked
  ctx.beginPath()
    creates a new path for the ctx to draw on
    if you don't call this after drawing, it will connect different shapes when you fill
  e.offsetX
    gives the X coordinate of the mouse based on the padding edge of the target object
  e.offsetY
    gives the Y coordinate of the moues based on the padding edge of the target object
*/

var c = document.getElementById("canvas");
var butt = document.getElementById("butt");
var clearbutt = document.getElementById("clear");
var switchbutt = document.getElementById("switch");

clearbutt.addEventListener("click", clear);
switchbutt.addEventListener("click", changemode);
c.addEventListener("mousemove", showCoords);
c.addEventListener("mousedown", draw);

var peepee = c.getContext("2d");
var canvaspos = c.getBoundingClientRect();
var mode = True;

function showCoords(event) {
  var x = event.clientX - canvaspos.x;
  var y = event.clientY - canvaspos.y;
  var coor = "X coords: " + x + ", Y coords: " + y;
  document.getElementById("demo").innerHTML = coor;
}

function draw(event) {
  var x = event.clientX - canvaspos.x;
  var y = event.clientY - canvaspos.y;
  console.log(mode);
  peepee.beginPath();
  peepee.fillStyle = "black";
  if (mode) {
    peepee.arc(x, y, 10, 0, 2 * Math.PI);
    peepee.fill();
  }
  else {
    peepee.fillRect(x, y, 20, 20);
  }
}

function clear(event) {
  peepee.clearRect(0,0,c.width,c.height);
}

function changemode(event) {
  mode = !mode;
}

console.log(canvaspos);
