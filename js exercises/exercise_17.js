// დავალება 3.1
let num1 = 7.45, num2 = '13.56';
num2 = Number(num2);
num1 = Math.round(num1);
num2 = Math.round(num2);
let result1 = num1 * num2;
document.write(result1);

// დავალება 3.2
let num1_2 = 20.3;
let num2_2 = 27.2;
let result2 = (num1_2 + num2_2).toFixed(2);
document.write("<br>" + result2);

// დავალება 3.3
let num3 = 77;
let result3 = Math.sqrt(num3).toFixed(1);
console.log(result3);

// დავალება 3.4
let num4 = 3.55;
let result4 = Math.pow(num4, 3).toFixed(2);
console.log(result4);

// დავალება 3.5
function info(str) {
  alert(str);
}

// დავალება 3.6
function exponentiation(a, b) {
  let res = Math.pow(a, b);
  alert(res);
  return res;
}

// დავალება 3.7
function isEven(num) {
  return num % 2 === 0;
}
console.log(isEven(4));
console.log(isEven(7));

// დავალება 3.8
function cutString(str, length) {
  return str.substring(0, length);
}
console.log(cutString("JavaScript", 4));

// დავალება 3.9
function address(addr) {
  document.getElementById("my-Address").innerHTML += "<br>" + addr;
}

// დავალება 3.10
function roundProduct(a, b) {
  let product = a * b;
  return {
    toTen: Math.round(product / 10) * 10,
    toOne: Math.round(product),
    toHundred: Math.round(product / 100) * 100
  };
}
console.log(roundProduct(12, 7));

// დავალება 3.11
function filterHTML(str) {
  return str.replace(/HTML/g, "");
}
console.log(filterHTML("I love HTML and CSS"));

// დავალება 3.12
const squared = (x) => x * x;
console.log(squared(5));

