import math as m 
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def fobj(x):
	l=len(x)
	sum=0
	for xx in x:
		sum=sum+(xx**2)/l
	return sum

x=np.linspace(-5,5,1000)
y=np.linspace(-5,5,1000)
xx,yy=np.meshgrid(x,y)
z=fobj([xx,yy])
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.contour3D(xx,yy,z,100)
# ax.plot_wireframe(xx,yy,z)
ax.set_xlabel("feature x1,x2")
ax.set_ylabel("feature y1,y2")
ax.set_zlabel("cost of the function")
plt.show()
