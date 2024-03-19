import math
# Dimensions of the desk
width_desk = 80  # in cm
length_desk = 60  # in cm

# Calculate the diagonal length using the Pythagorean theorem: sqrt(width^2 + length^2)
diagonal_length = math.sqrt(width_desk ** 2 + length_desk ** 2)

# Round up the diagonal length to the nearest whole number to ensure the paper fully covers the desk
minimum_paper_size = math.ceil(diagonal_length)

# Display the minimum size of paper needed
print("The minimum size of paper needed to cover the desk entirely is:", minimum_paper_size, "cm")
