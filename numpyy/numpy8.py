import numpy as np
np.random.seed(122)
a=np.random.randint(1,21,9).reshape(3,3)
b=np.random.randint(31,51,9).reshape(3,3)
print(np.hstack((a,b)))
print(np.vstack((a,b)))