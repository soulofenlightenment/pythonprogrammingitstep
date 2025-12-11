// დავალება 1
let arr1 = [10, 12, 45, 76, 11, 22, 90, -1, -5, -89];
let boolArr = arr1.map(num => num > 0);
console.log(boolArr);

// დავალება 2
let arr2 = [10, 12, 45, 76, 11, 22, 90, -1, -5, -89];
let filteredArr = arr2.filter(num => num > 20 && num < 90);
console.log(filteredArr);

// დავალება 3
let arr3 = [10, 12, 45, 76, 11, 22, 90, -1, -5, -89, 1, 3, 5, 4, 8, 6, 900];
let twoDigitArr = arr3.filter(num => Math.abs(num) >= 10 && Math.abs(num) <= 99);
console.log(twoDigitArr);

// დავალება 4
let arr4 = [10, 12, 45, 76, 11, 22, 90, -1, -5, -89, 1, 3, 5, 4, 8, 6, 900];
let hasThreeDigit = arr4.some(num => Math.abs(num) >= 100 && Math.abs(num) <= 999);
console.log(hasThreeDigit);
