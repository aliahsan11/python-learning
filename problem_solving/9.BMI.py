weight = input("Enter your weight(kg) :")
height = input("Enter your height(feet) : ")

height = float(height)

convertToMeter = height * 0.3048

weight = float(weight)

bmi = weight / (convertToMeter**2)

#  bmi = "%.4g" % (bmi)


if 18.5 > bmi:
    print("your BMI category : Underweight")

elif 18.5 >= bmi or 24.9 <= bmi:
    print("your BMI category : Normal weight ")

elif 25 >= bmi or 29.9 <= bmi:
    print("your BMI category : Overweight ")

elif 30 >= bmi or 34.9 <= bmi:
    print("your BMI category : Obesity (Class 1) ")

elif 35 >= bmi or 39.9 <= bmi:
    print("your BMI category : Obesity (Class 2) ")


elif 40 <= bmi:
    print("your BMI category : Extreme Obesity (Class 3) ")


else:
    print("invalid Category")
