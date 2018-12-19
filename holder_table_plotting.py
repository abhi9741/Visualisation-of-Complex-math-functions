import math as m 
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def holder_table_func(x,y):
	a=x**2+y**2
	aa=(np.sqrt(a))/np.pi 
	b=abs(1-aa)
	bb=np.exp(b)
	c=np.sin(x)*np.cos(y)
	d=abs(bb*c)
	d=(-1)*d
	print (d)
	return d

k1=holder_table_func(8.05502,9.66459)
k2=holder_table_func(8.05502,-9.66459)
k3=holder_table_func(-8.05502,9.66459)
k4=holder_table_func(-8.05502,-9.66459)
print("known global minimum at x=8.05502,y=9.66459\nx=-8.05502,y=9.66459\nx=8.05502,y=-9.66459\nx=-8.05502,y=-9.66459  is : ",k1,k2,k3,k4)
kk=holder_table_func(0,0)
print("our global optimum at x=0,y=0",kk)
x=np.linspace(-10,10,50)
y=np.linspace(-10,10,50)
xx,yy=np.meshgrid(x,y)
z=holder_table_func(xx,yy)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.contour3D(xx,yy,z,100)
# ax.plot_wireframe(xx,yy,z)
ax.set_xlabel("feature x")
ax.set_ylabel("feature y")
ax.set_zlabel("cost z")
plt.title("Holder Table Function")
plt.show()
