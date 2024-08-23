import re 
def password_strength_check(password):
    # Initialize score
    score = 0
    feedback = []

    # Criteria 1: Length of password

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criteria 2: Atleast one Uppercase letter

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Criteria 3: Atleast one Lowercase letter

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Criteria 4:Add atleast a Number
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Criteria 5: Add any Special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Feedback on the strength of the password
    if score == 5:
        return "Password Strength: Strong", feedback
    elif 3 <= score < 5:
        return "Password Strength: Moderate", feedback
    else:
        return "Password Strength: Weak", feedback

# Example usage:
password = input("Enter a password to check the strenth : ")
strength, feedback = password_strength_check(password)

print(strength)
if feedback:
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")

