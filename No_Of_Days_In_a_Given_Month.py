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
