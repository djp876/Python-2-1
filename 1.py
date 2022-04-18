##1.	Program to determine number of days in a given month

  #Program to Determine Number Of Days In A Given Months
month= int(input("enter month:"))
year=int(input("enter year:")) 
if ((month==1) or (month==3) or (month==5) or (month==8) or (month==10) or (month==12)):
    print("Number of Days is 31")
elif((month==2)and ((year%400==0)or(year%4==0 and year!=100))):
    print("The No Of Days Is 29.")
elif(month==2):
    print("Number of days is 28")
else:
    print("No Of Days is 30")

##2.	Coin change exercise program

#Coin change exercise program
lis=[500,200,100,50,20,10,2,1]
money=int(input("Please Enter Amount:"))
for i in lis:
    coin = int(money//i)
    print("No Of",i,"Note in",money,"is",coin)
coin=coin%i

##3.	Program to display  a calendar month between the years 1800 and 2099

#Program to display  a calendar month between the years 1800 and 2099
import calendar as cal
year = int(input("Input The Year:"))
if (year>=1800 and year<=2099):
    m =int(input("input the month :"))
    print(cal.month(year,m))
else:
    print("The Given Year I Out Of Range ")

##4.	Password encryption/decryption program

import base64 as bs
jo = input("Input The Password :")
password=jo.encode()
encode=bs.b64encode(password)
print(encode)
decoded=bs.b64decode(password)
print(decoded)

##5.	Temperature conversion program

print("1.FAHRENHEIT")
print("2.CELSIUS")
conv=(int(input("Enter The Coversion You Want To Covert Into :")))
if conv==1:
    celsius=(float(input("Enter The Temperature Into Celsius :")))
    fahrenheit=(celsius*9/5)+32
    print(fahrenheit)
elif conv==2:
    fahrenheit=(float(input("Enter The Temperature Into Fahrenheit :")))
    celsius=(fahrenheit-32)*5/9
    print(celsius)

##6.  GPA calculation program

##7.	Word frequency count program

#Word frequency count program
text = input("Enter the text :").split()
key_word = input("Enter the word :")
if key_word in text:
    print(key_word,text.count(key_word))

##8.	Mixed fraction class 

#Mixed fraction Class
m=int(input("Enter The Divident :"))
n=int(input("Enter The Divisor :"))
a=m//n
b=m%n
print("Mixed Fraction :",a,b,"/",n)

##9. Matrix manuplation1.	Program to determine number of days in a given month


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
result1 = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
print("addition of matrices")
for r in result:
    print(r)
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result1[i][j]+=X[i][k]*Y[k][j]
print("multiplication of matrices")
for z in result1 :
    print(z)
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] - Y[i][j]
print("subtraction of matrices")
for r in result:
    print(r)
