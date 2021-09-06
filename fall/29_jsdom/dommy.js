var fibbutt = document.getElementById("fb");
var butt = document.getElementById("b");
var fiblist = [];

var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e;
}

var removeItem = function(e) {
  e.remove();
}

var lis = document.getElementsByTagName("li");
for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover',
    function(e) { changeHeading(this.innerHTML); });
  lis[i].addEventListener('mouseout',
    function(e) { changeHeading("Hello World!"); });
  lis[i].addEventListener('click',
    function(e) { removeItem(this); });
}

var addItem = function(e) {
  console.log("works");
  var thelist = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  item.addEventListener('mouseover',
    function(e) { changeHeading(this.innerHTML); });
  item.addEventListener('mouseout',
    function(e) { changeHeading("Hello World!"); });
  item.addEventListener('click',
    function(e) { removeItem(this); });
  thelist.appendChild(item);
}

var fib = function(e){
  if (e <= 1) {
    fiblist.push(1);
    return 1;
  }
  else {
    final = fiblist[e-1] + fiblist[e-2];
    fiblist.push(final);
    return final;
  }
}

var addFib = function() {
  var showfib = document.getElementById("fiblist");
  var item = document.createElement("li");
  item.innerHTML = fib(fiblist.length);
  showfib.appendChild(item);
}

butt.addEventListener('click',addItem);
fibbutt.addEventListener('click', addFib);
