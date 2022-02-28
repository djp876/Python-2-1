import numpy as np

A=np.array([[1,1300,2.7],[1,1260,3.7],
            [1,1220,2.9],[1,1180,2.5],
            [1,1060,3.9],[1,1140,2.1],
            [1,1100,3.5],[1,1020,3.3],
            [1,980,2.3],[1,940,3.1]])
print('coeff of matrix is :\n{}'.format(A))
Y=np.array([[1],[1],[1],[1],[1],[0],[0],[0],[0],[0]])
print('dependent matrix is:\n{}'.format(Y))
AT=np.transpose(A)
betahat=np.dot(np.linalg.inv(np.dot(AT,A)),np.dot(AT,Y))
print('regression coefficents are:\n{}'.format(betahat))
Yhat=np.dot(A,betahat)
print('Yhat matrix is :\n{}'.format(Yhat))
eps=Y-Yhat
print('error matrix is :\n{}'.format(eps))
sse=np.dot(np.transpose(eps),eps)
print('sum of squares due to error is:\n{}'.format(sse))
sst=np.dot(np.transpose(Y-np.mean(Y,axis=0)),Y-np.mean(Y,axis=0))       
print('sum of squares due to total is :\n{}'.format(sst))
ssr=sst-sse
print('sum of squares due to regresion is:\n{}'.format(ssr))