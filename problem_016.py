"""
    Problem 16 project euler (copy - I did it but I lost the code)
"""
power = 1000
num = str(2**power)
sumOfDigits = 0

for i in range(len(num)):
    sumOfDigits += int(num[i])
print(sumOfDigits)