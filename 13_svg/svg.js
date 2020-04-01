// Jeff Lin
// SoftDev2 pd9
// K13: Ask Circles [Change || Die]
// 2020-03-31

var svg = document.getElementById("vimage");

var draw = function(e) {
  console.log(e.target)
  if (e.target == svg) {
    var x = e.offsetX;
    var y = e.offsetY;
    drawdot(x,y);
  }
  else {
      checkdot(e);
  }
}

var drawdot = function(x,y) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", "8");
    c.setAttribute("fill", "blue");
    svg.appendChild(c);
}

var checkdot = function(e){
    if (e.target.getAttribute("fill") == "blue") {
        e.target.setAttribute("fill", "violet");
    }
    else {
        svg.removeChild(e.target)
        var x = Math.floor(Math.random() * 500);
        var y = Math.floor(Math.random() * 500);
        drawdot(x,y);
    }
}

var clear = function(e) {
  while (svg.lastChild) {
    svg.removeChild(svg.lastChild);
  }
}

document.getElementById("clear").addEventListener('click',clear);
svg.addEventListener('click', draw);