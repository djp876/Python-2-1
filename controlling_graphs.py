#Controlling colours and styles of various graph elements in matplot lib

import matplotlib.pyplot as plt
indexes=list(map(int,input("Enter The values :").split()))
values=list(map(int,input("Enter The Values :").split()))
title=input("Enter The Title :")
xlable=input("x lable :")
ylable=input("y lable :")
plt.xlabel(xlable)
plt.ylabel(ylable)
plt.title(title)
color=input("Enter The colour :")
plt.barh(indexes,values,color=color)
plt.show()