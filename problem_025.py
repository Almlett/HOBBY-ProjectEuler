#1000-digit Fibonacci number
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time

def get_fibonacci():
    last_fibonacci = None
    fibonacci = 1
    last_num = 0
    _continue = True
    while _continue:
        last_fibonacci = fibonacci
        fibonacci += last_num
        last_num = last_fibonacci
        yield fibonacci
        if len(str(fibonacci)) > 999:
            _continue = False


start_time=time.time()
print(len(list(get_fibonacci())) + 1)
print("--- %s seconds ---" % (time.time() - start_time))
#TIME: 0.04800057411193848 seconds
#RESULT: 4782
