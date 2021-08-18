import numpy as np
n, m = map(int, input().split())
print(np.max(np.min(np.array([input().split() for _ in range(n)],int), axis = 1)))

