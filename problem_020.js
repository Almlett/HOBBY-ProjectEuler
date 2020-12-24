/* Problem 20 project euler */
/*
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

*/

const lut = [1n, 1n];
            
// returns factorial as BigInt instead of Number
function factorial (n) {
    for (let i = lut.length; i <= n; i++) {
        lut.push(BigInt(i) * lut[i - 1]);
    }

    return lut[n];
}

// first time will require computation
let allDigits = factorial(100).toString();

sum = 0;
for(index in allDigits){
    let digit = parseInt(allDigits[index]);
    sum += digit;
    //console.log(`${index}- previousDigit: ${digit} - sum: ${sum}`)
}
console.log(sum)