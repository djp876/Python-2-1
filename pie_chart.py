#Pie_chart 
import matplotlib.pyplot as plt
x=list(input("enter the lables :").split())
y=list(map(int,input("enter the values :").split()))
plt.pie(y,labels=x)
plt.show()