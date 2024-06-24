import numpy as np
from matplotlib import pyplot as plt

a=np.arange(1,9,3)
b1=np.arange(1,9,3)
b2=np.arange(1,9,3)

plt.plot(a,b1,label='Line 1')
plt.plot(a,b2,label='Line 2')

plt.title('Example')
plt.xlabel('a')
plt.ylabel('b')

plt.legend(loc='best')
plt.show()
