import numpy as np
M=1000
pab=0
cointoss=0
roll=0
for i in range(M):
    die=np.random.randint(1,7)
    if die%3!=0:
        cointoss+=1
        coin=np.random.randint(0,2)
        if die ==3 and coin ==1:
            pab+=1
    roll+=1
print('P(B|A) : ', pab/M)
