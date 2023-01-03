import numpy as np
import math
import sys

n = 10000
p = np.arange(n).reshape(n//2, 2)
M = np.zeros((p.shape[0], p.shape[0]))

print(p)
print(p.shape)

for i in range(p.shape[0]):
    for j in range(p.shape[0]):
        M[i][j] = math.dist(p[i], p[j])

print(M)
print(type(M))
print(sys.getsizeof(M))