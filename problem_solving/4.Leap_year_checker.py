leap_year = input("enter your year : ")
leap_year = int(leap_year)

if leap_year % 400 == 0 or ( leap_year % 4==0 and leap_year % 100 != 0):
    print("your selected year is leap year")

else :
    print("your selected year is a not leap year")


