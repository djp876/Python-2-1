import numpy as np
import math
obs=np.array([2.81,5.46])
A=np.array([[2.95,6.63],[2.53,7.79],[3.57,5.65],[3.16,5.47]])
print('A matrix is :\n{}'.format(A))
A=A.mean(axis=0)
print('mean :\n{}'.format(A))

FM=np.array([[2.95,6.63],[2.53,7.79],[3.57,5.65],[3.16,5.47],[3.16,5.47],[2.58,4.46],[2.16,6.22],[3.27,3.52]])
print('The full matrix is:\n{}'.format(FM))
print('Mean of matrix is:\n{}'.format(np.mean(Fm,axis=0)))
FM=print('the scaled matrix is:\n{}'.format(FM))
poolconv=np.dot(np.transpose(FM),FM)/7
print('The variancecovariance matrix is:\n{}'.format(np.round(poolcov,2)))
pcniv=np.linalg.inv(poolcov)
print('the inverse of pooled covariance matrix is:\n{}'.format(pcniv))
mu1=np.transpose(A)
mu2=np.transpose(B)
f1=np.dot(np.dot(mu1,pcinv),np.transpose(obs))-(0.5*(np.dot(mu1,pcniv),np.transpose(mu1)))+(math.log(4/7))
f1=np.dot(np.dot(mu2,pcinv),np.transpose(obs))-(0.5*(np.dot(mu2,pcniv),np.transpose(mu2)))+(math.log(3/7))
print('\n\n f1={}'.format(np.round(f1,2)))
print('f2=')