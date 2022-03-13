#Histogram
from matplotlib import pyplot as plt
import numpy as np
x=list(map(int,input("enter the values :").split()))
a=np.array(x)
b=list(map(int,input("enter the values :").split()))
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(a, bins=b)
plt.show()