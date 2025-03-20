
#Exercise 6 - Strings

#For this exercise I decided to also use a loop so that the user can enter a password until it meets the all criteria.

import re

def check_password_strength(password):
    criteria = [
        (len(password) >= 8, "Password must be at least 8 characters long."),
        (any(char.isupper() for char in password), "Password must contain an uppercase letter."),
        (any(char.islower() for char in password), "Password must contain a lowercase letter."),
        (any(char in "!@#$%^&*()_+" for char in password), "Password must contain a special character."),
    ]

    failed_criteria = [msg for check, msg in criteria if not check]

    if not failed_criteria:
        return "Password is strong"
    return "\n".join(failed_criteria)

while True:
    password = input("Enter a password: ")
    result = check_password_strength(password)
    if result == "Password is strong":
        print(result)
        break
    else:
        print(result)

