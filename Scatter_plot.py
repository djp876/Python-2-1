#Scatter_plot
import matplotlib.pyplot as plt
x=list(map(int,input("enter x values :").split()))
y=list(map(int,input("enter y values :").split()))
plt.scatter(x,y)
plt.show()