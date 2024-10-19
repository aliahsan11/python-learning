number1 = input("enter number1 ")
number1= int(number1)

number2 = input("enter number2 ")
number2= int(number2)

number3 = input("enter number3 ")
number3= int(number3)



if number1>number2 and number1>number3:
    print(f"the large number is {number1}")

elif number2>number1 and number2>number3:
    print(f"the large number is {number2}")
    
else:
    print(f"the large number is {number3}")
