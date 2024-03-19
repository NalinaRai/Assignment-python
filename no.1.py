# Total number of seconds
total_seconds = 12970

# Calculate hours, minutes, and remaining seconds
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Print the result
print(f"{total_seconds} Seconds is: {hours} Hours, {minutes} Minutes and {seconds} Seconds.")