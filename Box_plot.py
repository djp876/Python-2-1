#Box_plot
import matplotlib.pyplot as plt
x=list(map(int,input("enter the values of x:").split()))
%matplotlib inline
plt.boxplot(x)
plt.show()