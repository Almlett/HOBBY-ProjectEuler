#Lexicographic permutations
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import time

def get_list(quantity):
    return [i for i in range(quantity)]
    
def get_permutation(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]

    permutations = []

    for x in range(len(nums)):
        current = nums[x]
        remainders = nums[:x] + nums[x+1:]
        for y in get_permutation(remainders):
            permutations.append([current] + y)
    return permutations

start_time=time.time()
nums = get_list(10)
print(get_permutation(nums)[999999])
print("--- %s seconds ---" % (time.time() - start_time))
#TIME: 16.68933367729187 seconds
#RESULT: (2, 7, 8, 3, 9, 1, 5, 4, 6, 0)

