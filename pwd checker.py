import re

def check_password_strength(password):
    if password.lower() == "exit":
        return "exit"

    length = len(password)
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r"[!@#$%^&*()\-_=+{}[\]:\"|'\\<,>.?/]", password))

    strength = 0

    # Criteria weights
    length_weight = 2
    uppercase_weight = 2
    lowercase_weight = 2
    digit_weight = 2
    special_weight = 3

    # Check length
    if length >= 8:
        strength += length_weight

    # Check uppercase letters
    if has_uppercase:
        strength += uppercase_weight

    # Check lowercase letters
    if has_lowercase:
        strength += lowercase_weight

    # Check digits
    if has_digit:
        strength += digit_weight

    # Check special characters
    if has_special:
        strength += special_weight

    # Assess strength
    if strength >= 12:
        return "Strong"
    elif strength >= 8:
        return "Moderate"
    else:
        return "Weak"

# Test the function
while True:
    password = input("Enter your password (type 'exit' to quit): ")
    if password.lower() == "exit":
        print("Exiting...")
        break
    strength = check_password_strength(password)
    print("Password strength:", strength)
