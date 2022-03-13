#Line_chart_and_subplots
import matplotlib.pyplot as plt
import numpy as np
a=float(input("The string Point Of Graph:"))
b=float(input("The Ending Point Of Graph : "))
c= float(input("distance between poinits of garph :"))
j=float(input("The first value :"))
k=float(input("the second value :"))
x=np.arange(a*np.pi,b*np.pi,c)
y=np.sin(j*x)/x
y2=np.sin(x*x)/x
y3=np.sin(x)/x
plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()