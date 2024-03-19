# Total number of sheets
total_sheets = 50

# Number of students
num_students = 15

# Number of sheets each student will receive
sheets_per_student = total_sheets // num_students

# Number of sheets left over
sheets_left_over = total_sheets % num_students

# Printing the result
print("Each student will receive", sheets_per_student, "sheets of paper.")
print("There will be", sheets_left_over, "sheets left over.")

