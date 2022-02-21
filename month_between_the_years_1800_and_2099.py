#Program to display  a calendar month between the years 1800 and 2099
import calendar as cal
year = int(input("Input The Year:"))
if (year>=1800 and year<=2099):
    m =int(input("input the month :"))
    print(cal.month(year,m))
else:
    print("The Given Year I Out Of Range ")
