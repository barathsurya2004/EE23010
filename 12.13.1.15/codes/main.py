import numpy as np 
a=np.array([[1/3,2/3,0,0],[0,0,1/2,1/2],[0,0,1,0],[0,0,0,1]]) 
b=np.array([1,0,0,0]) 
m=1000
c=np.linalg.matrix_power(a,m)
print(np.matmul(b,c))


