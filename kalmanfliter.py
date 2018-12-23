import numpy as np
 
NUM = 300
np.random.seed(4)
Noise= np.random.randn(NUM)         
Noise_std = np.random.randn(NUM)      
 
X = [0]*NUM
Y = [0]*NUM
 
for i in range(1,NUM):
    X[i] =  np.sin(0.2*i)
 
 
Noise_std_ = np.square(np.var(Noise_std))  
Noise_     = np.square(np.var(Noise))
 
P = [0]* NUM               
K = [0]* NUM               
 
S =  X + Noise_std        
 
 
for i in range(1,NUM):
    P[i] =  np.square(P[i-1]) + 0.1*Noise_
 
    K[i] =  0.1*np.sqrt( P[i]/( Noise_std_ + P[i]))
 
    Y[i] =  Y[i-1] + K[i] * (S[i] - Y[i-1])
 
    P[i] =  np.sqrt((1-K[i])*P[i])
    print(i,P[i])

