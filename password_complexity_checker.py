import re 
import getpass 

def pass_complex_checker(pwd):

    # Check the length of the password 
    length = len(pwd) >= 10

    # Check the uppercase letter in the password 
    uppercase = bool(re.search(r'[A-Z]', pwd))

    # Check for lowercase letters in the password 
    lowercase = bool(re.search(r'[a-z]', pwd))

    # Check for numbers in the password
    number = bool(re.search(r'[0-9]', pwd))

    # Check for special characters in the password
    special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd)) 

    # Calculate total score
    total_score = length + uppercase + lowercase + number + special_char 

    # Prepare suggestions for missing criteria
    suggestions = []
    if not length:
        suggestions.append("Password should be at least 10 characters long.")
    if not uppercase:
        suggestions.append("Add at least one uppercase letter.")
    if not lowercase:
        suggestions.append("Add at least one lowercase letter.")
    if not number:
        suggestions.append("Add at least one number.")
    if not special_char:
        suggestions.append("Add at least one special character (!@#$%^&*(),.?\":{}|<>).")

    # Provide feedback based on the total score
    if total_score == 5:
        strength = "Strong password"
    elif total_score >= 3:
        strength = "Average password"
    else:
        strength = "Weak password"

    return strength, suggestions
    

pwd = input("Enter your password: ")
strength, suggestions = pass_complex_checker(pwd)
print("Password strength:", strength)
if suggestions:
    print("Suggestions to improve your password:")
    for suggestion in suggestions:
        print("-", suggestion)
