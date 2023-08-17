height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are over weight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
