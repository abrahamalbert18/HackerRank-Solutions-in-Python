import numpy as np
A = np.array([input().split() for _ in range(int(input()))], float)
print(round(np.linalg.det(A),2))
