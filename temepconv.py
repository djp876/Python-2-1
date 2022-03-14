#Temperature conversion program
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