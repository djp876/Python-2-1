#Visualization using matplot lib
#Bar_graph
import matplotlib.pyplot as plt
indexes=list(map(int,input("Enter The values :").split()))
values=list(map(int,input("Enter The Values :").split()))
title=input("Enter The Title :")
xlable=input("x lable :")
ylable=input("y lable :")
plt.xlabel(xlable)
plt.ylabel(ylable)
plt.title(title)
plt.bar(indexes,values,color='maroon',width=0.4)
plt.show()