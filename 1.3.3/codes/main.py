import numpy as np
import matplotlib.pyplot as plt
A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])



#D = B + (C - B) * (np.dot(A - B, C - B) / (np.linalg.norm(C-B))**2)
E = C + (C - A) * (((B-C).T@(C - A)) / (np.linalg.norm(C-A))**2)
print('The coordinates of E1 are: ',E)
F = A + (B-A) * (((B-A).T@(C - A)) / (np.linalg.norm(A-B))**2)
print('The coordinates of F1 are: ',F)
print("BE1 = ",B,"+ k",(E-B))
print("CF1 = ",C,"+ k",(F-C))
plt.plot([A[0], B[0]], [A[1], B[1]])
plt.plot([B[0], C[0]], [B[1], C[1]])
plt.plot([C[0], A[0]], [C[1], A[1]])
#plt.scatter(D[0], D[1], label='D1')
plt.scatter(A[0], A[1], label='A')
plt.scatter(B[0], B[1], label='B')
plt.scatter(C[0], C[1], label='C')
plt.scatter(E[0], E[1], label='E1')
plt.scatter(F[0], F[1], label='F1')

plt.annotate('A', A, textcoords="offset points", xytext=(0,10))
plt.annotate('B', B, textcoords="offset points", xytext=(0,10))
plt.annotate('C', C, textcoords="offset points", xytext=(0,10))
#plt.annotate('D1', D, textcoords="offset points", xytext=(0,-20))
plt.annotate('E1', E, textcoords="offset points", xytext=(0,-20))
plt.annotate('F1', F, textcoords="offset points", xytext=(0,-20))

#plt.plot([A[0], D[0]], [A[1], D[1]], linestyle='--', label='AD1')
plt.plot([A[0], E[0]], [A[1], E[1]], linestyle='-.')

plt.plot([B[0], E[0]], [B[1], E[1]], linestyle='--', label='BE1')
plt.plot([C[0], F[0]], [C[1], F[1]], linestyle='--', label='CF1')
plt.plot([A[0], F[0]], [A[1], F[1]], linestyle='-.')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Altitude of a Triangle')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
