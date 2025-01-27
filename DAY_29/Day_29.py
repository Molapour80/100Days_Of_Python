import re

def is_valid_email(email):
    # Define the regex pattern for validating an email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the defined pattern
    return re.match(email_pattern, email) is not None

# Example usage
email = input("Please enter your email address: ")
if is_valid_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")