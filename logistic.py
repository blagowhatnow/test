import numpy as np
import matplotlib.pyplot as plt

#Parameters

nmax=100
delta_n=0.005

n=np.arange(0,nmax,delta_n)

def f(y):
   #This can be any function
   r=32*(np.sin(y))*(y**2-10)
   return r

x=[]
x.append(f(n[0]))

for i in np.arange(delta_n,nmax,delta_n):
    a=f(delta_n+i)
    x.append(a)

plt.plot(n,x)
plt.show()  

