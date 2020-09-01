"""
    Problem 14 project euler
"""
def longest_collatz():
    """
        Collatz
    """
    term_map = dict()
    for num in range(1,1000000):
        start = num
        value = start
        counter = 1
        while value > 1:
            if value%2 == 0:
                value = value/2
            else:
                value = 3*value + 1
            if value in term_map:
                counter = counter + term_map[value]
                break
            counter += 1
        term_map[start] = counter
    max = 0
    solution = 0
    for i in term_map:
        if term_map[i] > max:
            max = term_map[i]
            solution = i
    return solution

print(longest_collatz())
        