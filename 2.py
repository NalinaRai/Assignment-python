# Take input from the user
character = input("Enter a character: ")

# Using ord() to get the Unicode code point of the character
unicode_code_point = ord(character)
print(f"The Unicode code point of '{character}' is:", unicode_code_point)

# Take input from the user again, this time the Unicode code point
code_point = int(input("Enter a Unicode code point: "))

# Using chr() to get the character corresponding to the Unicode code point
character_from_code_point = chr(code_point)
print(f"The character corresponding to the Unicode code point {code_point} is:", character_from_code_point)
