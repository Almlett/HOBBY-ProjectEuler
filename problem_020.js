/* Problem 20 project euler */
/*
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

*/


let result = 1;

let fact = val => {
    if (val > 0){
        result = result * val;
        fact(val - 1);
    }
};

fact(100);
const allDigits = new String(BigInt(result).toString())
console.log(allDigits.toString())

let sum = 0;
for(index in allDigits){
    let digit = parseInt(allDigits[index]);
    sum += digit;
    console.log(`${index}- previousDigit: ${digit} - sum: ${sum}`)
}
console.log(sum)