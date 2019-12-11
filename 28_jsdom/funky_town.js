var fibonacci = function(n){
  if (n == 0) return n;
  if (n == 1) return n;
  else{
    return fibonacci(n-1) + fibonacci(n-2);
  }
}

var gcd = function(x, y){
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
  var rand = studlist[Math.floor(Math.random() * studlist.length)];
  var output = "Random student: " + rand;
  console.log(output)
  document.getElementById("output").innerHTML = output;
  return rand;
}



var randfib = function(){
  var num = Math.floor(Math.random() * 30);
  var output = "Number " + num + " in Fibonacci: " + fibonacci(num);
  document.getElementById("output").innerHTML = output;
  console.log(output);
}
var fibbutt = document.getElementById("fib");
fibbutt.addEventListener('click',randfib);

var randgcd = function(){
  var num1 = Math.floor(Math.random() * 99999);
  var num2 = Math.floor(Math.random() * 99);
  var output = "GCD of " + num1 + " and " + num2 + ": " + gcd(num1,num2);
  document.getElementById("output").innerHTML = output;
  console.log(output);
}
var gcdbutt = document.getElementById("gcd");
gcdbutt.addEventListener('click',randgcd);

var randbutt = document.getElementById("randstud");
randbutt.addEventListener('click',randomStudent);



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
