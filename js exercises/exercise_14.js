// 1.გვარის სიგრძე
const str = "kalandarishvili";
console.log(str.length); // 15

// 2. ზემო და ქვემო რეგისტრი
let name = 'ana';
console.log(name.toUpperCase()); 
name = 'GIA';
console.log(name.toLowerCase());

// 3. substring()
let capital = 'თბილისი';
console.log(capital.substring(0, 5));

// 4. ჩანაცვლება
let string = 'Hello world, this is string';

string = string.replace('world', 'Tbilisi');
string = string.replace('string', 'This is me');
console.log(string); 

