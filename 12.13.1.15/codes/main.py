import numpy as np 
a=np.array([[-2/3,0,0,0],[-4/3,-2,0,0],[1,1,1,0],[1,1,0,1]]) 
z=np.array([[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,1]]) 
a_1=np.linalg.inv(a) 
b=np.array([1,0,0,0]) 
# print(a_1) 
az=np.matmul(a,z) 
aza_1=np.matmul(az,a_1) 
print(aza_1) 
print(np.matmul(aza_1,b.T))

