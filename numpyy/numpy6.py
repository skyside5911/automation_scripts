import numpy as np
np.random.seed(122)
matrix=np.random.randint(1,21,9).reshape(3,3)
print(matrix)
print(np.min(matrix,1))
print(np.max(matrix,0))
print(np.cumsum(matrix,1))


