"""
    Problem 17 project euler (copy - I did it but I lost the code)
"""
from num2words import num2words
nums = range(1, 1001)
word_nums = []
for num in nums:
	a = num2words(num)
	b = a.replace(' ', '')
	c = b.replace('-', '')
	l = int(len(c))
	word_nums.append(l)
result = sum(word_nums)
print(result)