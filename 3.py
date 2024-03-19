# Taking input from the user for weight and height
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculating BMI
bmi = weight_kg / (height_m ** 2)

# Displaying the BMI
print("Your BMI is:", bmi)
