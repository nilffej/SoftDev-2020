var butt = document.getElementById("b");
var fibbutt = document.getElementById("fb");
var list = {};

var changeHeading = function(e) {
  var h = document.getElementById("h");
  // console.log(e.getAttribute("Id"));
  h.innerHTML = e;
}

var removeItem = function(e) {
  e.remove();
}

var lis = document.getElementsByTagName("li");
for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover',
    function(e) { changeHeading(lis[i]); });
  lis[i].addEventListener('mouseout',
    function(e) { changeHeading("Hello World!"); });
  lis[i].addEventListener('click',
    function(e) { removeItem(lis[i]); });
}

// button.addEventListener('click',
//   function(e) {console.log(e); }
// );
