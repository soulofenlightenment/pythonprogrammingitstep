// 1. 1-დან 100-მდე რიცხვების დაყოფა 2-ისა და 3-ის ჯერადებად
let evens = [];
let divByThree = [];
for (let i = 1; i <= 100; i++) {
  if (i % 2 === 0) {
    evens.push(i);
  }
  if (i % 3 === 0) {
    divByThree.push(i);
  }
}
console.log("2-ის ჯერადები:", evens);
console.log("3-ის ჯერადები:", divByThree);

// 2. 1-დან 500-მდე, ნაბიჯი = 6
let i = 1;
while (i <= 500) {
  console.log(i);
  i += 6;
}

//3. მასივიდან 10-ზე უნაშთოდ გაყოფადი ელემენტები
let arr = [10, 12, 67, 54, 90, 33, 78, 2, 0];

for (let num of arr) {
  if (num % 10 === 0) {
    console.log(num);
  }
}
//4. მასივიდან ლუწ ინდექსებზე მდგომი ელემენტები
let ar = [10, 12, 67, 54, 90, 33, 78, 2, 0];

for (let i = 0; i < arr.length; i++) {
  if (i % 2 === 0) {
    console.log(arr[i]);
  }
}

