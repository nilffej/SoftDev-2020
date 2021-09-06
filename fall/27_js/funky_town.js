var fibonacci = function(n){
  if (n == 0) return n;
  if (n == 1) return n;
  else{
    return fibonacci(n-1) + fibonacci(n-2);
  }
}

var gcd = function(x, y){
  // switches x and y if y > x
  if (y > x){
    var hold = y;
    y = x;
    x = hold;
  }
  if (x % y == 0) return y;
  else{
    return gcd(y, x % y);
  }
}

var studlist = ["Jeff","Nichol","Jackson","JunTao","Grace","Mr. Mykolyk"]

var randomStudent = function(){
  var rand = Math.floor(Math.random() * studlist.length);
  return studlist[rand];
}



// document.getElementByID(<ID>)
// document.getElementsByTagName(<ID>)
// document.getElementsByClassName(<CLASS>)

// .addEventListener(<EVENT>,<FUNCTION>)

// HTML
// <button id="b"> The button </button>
// JS
// var dasbut = document.getElementById("b");
// dasbut.addEventListener('click',fxnName);

// document.createElement(<HTML TAG NAME>)
// element.setAttribute(<NAME>,<VALUE>)

// element.remove()
