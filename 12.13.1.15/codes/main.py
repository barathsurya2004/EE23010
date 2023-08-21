import numpy as np 
a=np.array([[1/3,2/3,0,0],[0,0,1/2,1/2],[0,0,1,0],[0,0,0,1]]) 
b=np.array([1,0,0,0]) 
c=a 
for i in range(100): 
    c=np.matmul(c,a) 
print(np.matmul(b,c))

