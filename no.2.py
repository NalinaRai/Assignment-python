# Taking input for days taken by A, B, and C respectively
x = float(input("Enter days taken by person A to do the job alone: "))
y = float(input("Enter days taken by person B to do the job alone: "))
z = float(input("Enter days taken by person C to do the job alone: "))

# Calculating the number of days it will take for them to complete the job together
total_days = (x * y * z) / (x * y + y * z + x * z)

# Printing the result
print("The job will be completed by A, B, and C together in approximately", round(total_days, 2), "days.")

