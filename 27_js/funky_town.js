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
  if (x % y == 1) return 1;
  else{
    return gcd(y, x % y);
  }
}
