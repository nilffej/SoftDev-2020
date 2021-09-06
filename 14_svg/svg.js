// Jeff Lin & Jackson Zou
// SoftDev2 pd9
// K14 -- Ask Circles [Change || Die] While Moving, etc.
// 2020-04-01

var svg = document.getElementById("vimage");

var clearB = document.getElementById("clear");
var moveB = document.getElementById("move");
var xtraB = document.getElementById("xtra");

balls = []
var animation = 0;

var draw = function(e) {
  console.log(e.target)
  if (e.target == svg) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    var x = e.offsetX;
    var y = e.offsetY;
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", "10");
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "black");
    c.setAttribute("movex", "2");
    c.setAttribute("movey", "1");
    svg.appendChild(c);
    balls.push(c);
  }

  else {
    if (e.target.getAttribute("fill") == "blue") {
      e.target.setAttribute("fill", "violet");
    }
    else {
      var xval = e.target.getAttribute("cx");
      var yval = e.target.getAttribute("cy");
      svg.removeChild(e.target)
      for (i = 0; i < balls.length; i++) {
          if (balls[i].getAttribute("cx") == xval && balls[i].getAttribute("cy") == yval) {
            balls.splice(i, 1);
          }

      }
      var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      var x = Math.floor(Math.random() * 500);
      var y = Math.floor(Math.random() * 500);
      c.setAttribute("cx", x);
      c.setAttribute("cy", y);
      c.setAttribute("r", "10");
      c.setAttribute("fill", "blue");
      c.setAttribute("stroke", "black");
      svg.appendChild(c);
      balls.push(c);
    }
  }
  console.log(balls);
}

var awaken = function(e) {
  if (animation == 0) {
    animation = window.requestAnimationFrame(move);
  }
}

var move = function(e) {
  for (i = 0; i < balls.length; i++) {
    if (parseInt(balls[i].getAttribute("cx")) > 500 || parseInt(balls[i].getAttribute("cx")) < 0) {
      balls[i].setAttribute("movex", balls[i].getAttribute("movex") * -1);
    }
    if (parseInt(balls[i].getAttribute("cy")) > 500 || parseInt(balls[i].getAttribute("cy")) < 0) {
      balls[i].setAttribute("movey", balls[i].getAttribute("movey") * -1);
    }
    var newx = String(parseInt(balls[i].getAttribute("cx")) + parseInt(balls[i].getAttribute("movex")));
    var newy = String(parseInt(balls[i].getAttribute("cy")) + parseInt(balls[i].getAttribute("movey")));
    balls[i].setAttribute("cx", newx);
    balls[i].setAttribute("cy", newy);
  }
  animation = window.requestAnimationFrame(move);
}

var clear = function(e) {
  while (svg.lastChild) {
    svg.removeChild(svg.lastChild);
  }
  balls = []
  console.log(balls);
  window.cancelAnimationFrame(animation);
  animation = 0;
}

var explode = function(e) {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  for (i = 0; i < balls.length; i++) {
    balls[i].setAttribute("fill", color);
  }
}

clearB.addEventListener('click',clear);
moveB.addEventListener('click', awaken);
xtraB.addEventListener('click', explode)


svg.addEventListener('click', draw);