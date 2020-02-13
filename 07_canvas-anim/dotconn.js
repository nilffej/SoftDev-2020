/*
Jeff Lin
SoftDev2 PD9
K07 -- They lock us in the tower whenever we get caught
2020-02-13
*/

var c = document.getElementById("playground");
var butt = document.getElementById("animate");
var clearbutt = document.getElementById("stop");

butt.addEventListener("click", animate);
clearbutt.addEventListener("click", stop);

var ctx = c.getContext("2d");
var canvaspos = c.getBoundingClientRect();
var started = false;
var size = 0;
var change = 1;

// function showCoords(event) {
//   var x = event.clientX - canvaspos.x;
//   var y = event.clientY - canvaspos.y;
//   var coor = "X coords: " + x + ", Y coords: " + y;
//   document.getElementById("demo").innerHTML = coor;
// }

function animate(event) {
  if (!started) {
    window.requestAnimationFrame(draw);
    started = true;
  }
  else {
    started = false;
  }
}

function draw() {
  if (!started) { return; }
  console.log("hello");
  ctx.clearRect(0,0,c.width,c.height);
  ctx.fillStyle = "black";
  ctx.beginPath();
  ctx.arc(c.width/2, c.height/2, size, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  size += change;
  if (size == 0 || size == c.width/2) {
    change *= -1;
  }
  window.requestAnimationFrame(draw);
}

function stop(event) {
  started = !started;
}

console.log(canvaspos);
