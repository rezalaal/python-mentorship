# Calculates the BMI of a person

# Get the weight and height from the user
weight = float(input("Enter your weight in Kg: "))
height = float(input("Enter your height in meters: "))
# Calculate the BMI
bmi = weight / height ** 2

# round the bmi to 2 decimal places
bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")