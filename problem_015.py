"""
    Problem 15 project euler
"""
import time
import numpy as np
start_time = time.time()

lattice = np.zeros((21,21),dtype=float)
lattice[20,:] = 1
lattice[:,20] = 1
lattice[20,20] = 0

for ix in range(19,-1,-1):
    for iy in range (19,-1,-1):
        lattice[ix,iy] = lattice[ix+1,iy]+lattice[ix,iy+1]

print(lattice[0,0])
print(str(time.time()-start_time)+" seconds")
