import numpy as np
import matplotlib.pyplot as plt
import scipy as s

xs = np.linspace(-5, 3,1000)
f=((xs**3)+3*(xs**2)-6*xs-8)

plt.plot(xs,f)
plt.axhline(0, color='black', linewidth='0.5')
plt.axvline(0, color="black",linewidth="0.5")
plt.show() 

ys=np.linspace(0,2)

f=((ys**3)+3*(ys**2)-6*ys-8)

d=f.min()
print(d)

