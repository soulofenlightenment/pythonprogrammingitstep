// დავალება 4.1
let arr1 = [1, "hello", true, 45];
console.log(arr1.length);

// დავალება 4.2
let arr2 = ['a', 'b', 'c'];
arr2[3] = 'd';
arr2[1] = 'x';
console.log(arr2);

// დავალება 4.3
let arr3 = [];
arr3.push('a', 'b', 'c');
console.log(arr3);

// დავალება 4.4
let arr4 = [1, 2, 3, 4, 5];
let key1 = 1;
let key2 = 2;
let result4 = arr4[key1] + arr4[key2];
console.log(result4);

// დავალება 4.5
let arr5 = ['a', 'b', 'c', 'd', 'e'];
delete arr5[1];
delete arr5[3];
console.log(arr5.length);
console.log(arr5);

// დავალება 4.6
let names = ['ხვიჩა', 'გოგა', 'მაკა', 'ანა', 'ინა'];
let arr6 = [11, 22, 33, 44, 55];
names.sort();
console.log(names);
names.sort().reverse();
console.log(names);
console.log(arr6[arr6.length - 1]);

// დავალება 4.7
let arr7 = [10, 11, 12, 13, 14];
console.log(arr7.length);

// დავალება 4.8
let arr8 = [10, 11, 12, 13, 14];
console.log(arr8.length);

// დავალება 4.9
function getBlankArray() {
  return [];
}
console.log(getBlankArray());

// დავალება 4.10
function getNumOfComponents(components) {
  return components.length;
}
console.log(getNumOfComponents([1,2,3]));

// დავალება 4.11
const priceSum = (prices) => prices.reduce((sum, p) => sum + p, 0);
console.log(priceSum([10, 20, 30]));

// დავალება 4.12
function addBoll(toys) {
  toys.push("ბურთი");
  return toys;
}
let toys12 = ['ოვერბორდი', 'პაზლი', 'Lego'];
console.log(addBoll(toys12));

// დავალება 4.13
function addToy(toy, toys) {
  toys.push(toy);
  return toys;
}
let toys13 = ['ოვერბორდი', 'პაზლი', 'Lego'];
let toy13 = 'Yo-yo';
console.log(addToy(toy13, toys13));

// დავალება 4.14
function getLastToy(toys) {
  return toys[toys.length - 1];
}
let toys14 = ['ოვერბორდი', 'პაზლი', 'Lego', 'Yo-yo'];
console.log(getLastToy(toys14));



