import numpy as np

a=np.array([1,2,3,4])
b=np.array([(1,2,3),(1,4,5)])
c=np.array([[(1,2,3),(2,4,3)],[(3,4,2),(2,3,4)]])
print(a)
print(b)
print(c)

print(c.ndim)
print(c.shape)
print(c.size)
print(c.itemsize)
