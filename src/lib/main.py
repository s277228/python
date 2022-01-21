
from scipy import fftpack
from scipy import integrate
import numpy as np 

b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print(d)

f=np.ones(4)
print(f)

a=np.arange(6)
b=a[2:5]
b[0]=40
b[1]=50
print(a, b)
