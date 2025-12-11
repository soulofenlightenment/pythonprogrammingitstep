// დავალება 6.1
for (let i = 55; i <= 77; i++) {
  console.log(i);
}

// დავალება 6.2
for (let i = 10; i <= 120; i++) {
  if (i % 2 !== 0) {
    console.log(i);
  }
}

// დავალება 6.3
for (let i = 110; i >= 90; i--) {
  console.log(i);
}

// დავალება 6.4
let toys1 = ['ოვერბორდი', 'პაზლი', 'Lego', 'Yo-yo'];
for (let i = 1; i < toys1.length - 1; i++) {
  console.log(toys1[i]);
}

// დავალება 6.5
let toys2 = ['ოვერბორდი', 'პაზლი', 'Lego', 'Yo-yo'];
for (let i = 0; i < toys2.length; i++) {
  console.log(toys2[i]);
}

// დავალება 6.6
let arr6 = [2, 2, 3, 4, 5];
for (let num of arr6) {
  console.log(num);
}

// დავალება 6.7
let i7 = 10;
while (i7 <= 30) {
  console.log(i7);
  i7++;
}

// დავალება 6.8
let i8 = 1;
while (i8 <= 10) {
  console.log(i8 * i8);
  i8++;
}

// დავალება 6.9
let arr9 = [2, 2, 3, 4, 5];
for (let num of arr9) {
  if (num % 2 === 0) {
    console.log(num);
  }
}

// დავალება 6.10
let arr10 = [1, 77, 9, 17, 4, 3, 9, 8, 20];
for (let num of arr10) {
  if (num > 5 && num < 10) {
    console.log(num);
  }
}

// დავალება 6.11
let object = {a: 7, b: 8, c: 15, d: 20, e: 55};
for (let key in object) {
  if (object[key] % 2 === 0) {
    console.log(object[key]);
  }
}

// დავალება 6.12
let sum12 = 0;
for (let i = 10; i <= 80; i++) {
  if (i % 2 === 0) {
    sum12 += i;
  }
}
console.log(sum12);

// დავალება 6.13
let product13 = 1;
for (let i = 5; i <= 30; i++) {
  product13 *= i;
}
console.log(product13);

// დავალება 6.14
let str14 = "";
for (let i = 2; i <= 14; i += 2) {
  str14 += i;
}
console.log(str14);

// დავალება 6.15
let str15 = "";
for (let i = -11; i <= -3; i++) {
  str15 += i;
}
console.log(str15);

// დავალება 6.16
for (let i = 50; i <= 500; i++) {
  let str = i.toString();
  if (str.length >= 2) {
    let sum = Number(str[0]) + Number(str[1]);
    if (sum === 4) {
      console.log(i);
    }
  }
}

// დავალება 6.17
let arr17 = [10.8, 7.227, 9, 17.34, 10.34, 3, 7.9, -8, 20, 100, 77, 345.67];
let sum17 = 0;
for (let num of arr17) {
  if (num < 0) break;
  sum17 += num;
}
console.log(sum17);

// დავალება 5.18
let names = ['ხვიჩა', 'გოგა', 'მაკა', 'ანა', 'ინა', 'მაიკლი', 'ფანტომასი', 'ბონდო', 'ობამა', 'მესი', 'მარადონა'];
console.log(names.indexOf('ფანტომასი'));

// დავალება 5.19
let sum19 = 0;
let count19 = 0;
while (sum19 <= 200) {
  count19++;
  sum19 += count19;
}
console.log(count19);

// დავალება 5.20
for (let a = 1; a <= 4; a++) {
  for (let b = 1; b <= 2; b++) {
    document.write(a);
  }
}

// დავალება 5.21
let matr = [
  [128, 52, 6, 76, 200],
  [95, 36, 2, 44, 300],
  [2, 4, 7, 9, 2]
];
let sums = [];
for (let row of matr) {
  let s = 0;
  for (let num of row) {
    s += num;
  }
  sums.push(s);
}
console.log(sums);

// დავალება 5.22
for (let i = 0; i <= 9; i++) {
  let num = 3;
  for (let j = 0; j <= 9; j++) {
  }
}
console.log(num); // ReferenceError: num is not defined

// დავალება 5.23
let arr23 = [];
for (let i = 20; i <= 40; i++) {
  arr23.push(i);
}
console.log(arr23);

// დავალება 5.24
let arr24 = [1, -77, 9, 17, -4, 3, 9, -8, 20];
let positives = [];
for (let num of arr24) {
  if (num > 0) {
    positives.push(num);
  }
}
console.log(positives);

// დავალება 5.25
let arr25 = [10.8, 7.227, 9, 17.34, 10.34, 3, 7.9, -8, 20, 100, 77, 345.67];
let squaredArr = [];
for (let num of arr25) {
  squaredArr.push(num * num);
}
console.log(squaredArr);

// დავალება 5.26
let obj = {};
let keys = ['ორ.', 'სამშ.', 'ოთხ.', 'ხუთ.', 'პარ.', 'შაბ.', 'კვ.'];
let values = [1, 2, 3, 4, 5, 6, 7];
for (let i = 0; i < keys.length; i++) {
  obj[keys[i]] = values[i];
}
console.log(obj);

// დავალება 5.27
let cars = {
  BMW: 'შავი',
  Mercedes: 'ვერცხლისფერი',
  Nissan: 'შავი',
  Ford: 'წითელი',
  Toyota: 'შავი'
};
let blackCars = {};
for (let key in cars) {
  if (cars[key] === 'შავი') {
    blackCars[key] = cars[key];
  }
}
console.log(blackCars);

// დავალება 5.28
let day = new Date().getDay();
let days = ['კვ.', 'ორ.', 'სამშ.', 'ოთხ.', 'ხუთ.', 'პარ.', 'შაბ.'];
let type = (day === 0 || day === 6) ? 'დასვენების დღე' : 'სამუშაო დღე';
document.write(days[day] + " - " + type);

// დავალება 5.29
let months = [
  'იანვარი', 'თებერვალი', 'მარტი', 'აპრილი', 'მაისი', 'ივნისი',
  'ივლისი', 'აგვისტო', 'სექტემბერი', 'ოქტომბერი', 'ნოემბერი', 'დეკემბერი'
];
let currentMonth = new Date().getMonth();
document.write(months[currentMonth]);
