import numpy as np
np.random.seed(122)
matrix=np.random.randint(1,22,9).reshape(3,3)
print(matrix)
aa=np.multiply(matrix,matrix,matrix)
print(aa)