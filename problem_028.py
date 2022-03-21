# Number spiral diagonals
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import time
import math
start_time = time.time()

matrix = []
quantity = 1001
center = math.floor(quantity/2)
x = center
y = center
directions = {
    1: "Rigth",
    2: "Down",
    3: "Left",
    4: "Up"
}
direction = 1
iteraciones = 1
tmp = 1
num = 1
total = 0

for i in range(0, quantity):
    matrix.append([0]*quantity)

for i in range(0, (quantity*quantity)):
    matrix[x][y] = num
    if directions[direction] == 'Rigth':
        y += 1
        if tmp == iteraciones:
            direction = 2
            tmp = 1
        else:
            tmp += 1
    elif directions[direction] == 'Down':
        x += 1
        if tmp == iteraciones:
            direction = 3
            iteraciones += 1
            tmp = 1
        else:
            tmp += 1
    elif directions[direction] == 'Left':
        y -= 1
        if tmp == iteraciones:
            direction = 4
            tmp = 1
        else:
            tmp += 1
    elif directions[direction] == 'Up':
        x -= 1
        if tmp == iteraciones:
            direction = 1
            tmp = 1
            iteraciones += 1
        else:
            tmp += 1
    num += 1

iteracion = 0
for i in range(0, quantity):
    a = matrix[i][0 + iteracion]
    b = matrix[i][(quantity-1) - iteracion]
    iteracion += 1
    if a == b:
        total += a
    else:
        total = total + a + b

print(total)
print("--- %s seconds ---" % (time.time() - start_time))
# 669171001
# --- 0.3978705406188965 seconds ---
