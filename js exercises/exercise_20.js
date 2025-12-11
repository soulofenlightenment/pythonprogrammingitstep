// დავალება 7.1
let weekDays = {
  1: "ორშაბათი",
  2: "სამშაბათი",
  3: "ოთხშაბათი",
  4: "ხუთშაბათი",
  5: "პარასკევი",
  6: "შაბათი",
  7: "კვირა"
};
console.log(weekDays);

// დავალება 7.2
let obj = {
  '9name': 10,
  'key7': 20,
  'a-b': 30,
  'city 10': 40,
  'city10': 50
};
console.log(obj['9name']);
console.log(obj.key7);
console.log(obj['a-b']);
console.log(obj['city 10']);
console.log(obj.city10);

// დავალება 7.3
const person = {
  name: "ვაჟა ცხადაძე",
  gender: "მამრობითი"
};
const dob = {
  data_of_birth: 2011
};
const personInfo = {...person, ...dob};
console.log(personInfo);

// დავალება 7.4
const person2 = {
  name: "ვაჟა ცხადაძე",
  gender: "მამრობითი"
};
const {name, gender} = person2;
console.log(name, gender);

// დავალება 7.5
const person3 = {
  name: "ვაჟა ცხადაძე",
  gender: "მამრობითი",
  data_of_birth: 2011
};
const canVote = (p) => {
  let currentYear = new Date().getFullYear();
  let age = currentYear - p.data_of_birth;
  return age >= 18;
};
console.log(canVote(person3));
