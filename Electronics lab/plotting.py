import numpy as np
import matplotlib.pyplot as plt
import scipy as s

#PLOTTING
"""
xs = np.linspace(-2,2,1000)
f=xs**3

plt.plot(xs,f)
plt.axhline(0, color='black', linewidth='0.5')
plt.axvline(0, color="black",linewidth="0.5")
plt.show() 

ys=np.linspace(0,1)

f=ys**3

d=f.max()
print(d)"""

# Calculating
u_iz=[138,146,155,165,175,182.2,185,186,189.2,221,220,218,217,211,209,195,186,172.7,151.7]
u_ul=[6.27,6.27,6.25,6.23,6.25,6.32,6.3,6.28,6.37,7.4,7.35,7.31,7.38,7.25,7.27,7.14,7.03,6.76,6.44]
u_ul=np.array(u_ul)
u_iz=np.array(u_iz)

A=u_iz/u_ul

print(A)