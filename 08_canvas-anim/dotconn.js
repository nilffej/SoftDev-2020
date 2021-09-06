/*
Jeff Lin
SoftDev2 PD9
K07 -- They lock us in the tower whenever we get caught
2020-02-13
*/



var img = new Image();
img.src = 'dvd.jpg'

var c = document.getElementById("playground");
var butt = document.getElementById("animate");
var dvdbutt = document.getElementById("dvd");
var clearbutt = document.getElementById("stop");

butt.addEventListener("click",
  function() {
    animate(0);
});
dvdbutt.addEventListener("click",
  function() {
    animate(1);
});
clearbutt.addEventListener("click", stop);

var ctx = c.getContext("2d");
var canvaspos = c.getBoundingClientRect();

var mode = 0;
var started = false;
var size = 0;
var change = 1;

var imgx = 50 + Math.floor(Math.random() * (c.width - img.width * 0.2 - 200));
var imgy = 50 + Math.floor(Math.random() * (c.height - img.height * 0.2 - 200));
var dx = 1 + Math.random() * 1;
var dy = 1 + Math.random() * 1;

function animate(newmode) {
  console.log(imgx + " " + imgy);
  console.log(mode + " " + started);
  if (started == false || newmode != mode) {
    mode = newmode;
    started = true;
    if (mode == 0) window.requestAnimationFrame(drawCircle);
    if (mode == 1) window.requestAnimationFrame(drawDVD);
  }
}

function drawCircle() {
  if (started == false || mode != 0) {
    return;
  }
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
  window.requestAnimationFrame(drawCircle);
}

function drawDVD() {
  if (started == false || mode != 1) {
    return;
  }
  ctx.clearRect(0,0,c.width,c.height);
  ctx.drawImage(img, imgx, imgy, img.width * 0.2, img.height * 0.2);
  imgx += dx;
  imgy += dy;
  if (imgx <= 0 || imgx >= c.width - img.width * 0.2) dx *= -1;
  if (imgy <= 0 || imgy >= c.height - img.height * 0.2) dy *= -1;
  window.requestAnimationFrame(drawDVD);
}

function stop(event) {
  started = false;
}

console.log(canvaspos);
