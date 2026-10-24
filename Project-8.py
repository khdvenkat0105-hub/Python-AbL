#Password Policy Validation Engine(29th)
password = input("Enter a password: ")

valid = True

if len(password) < 8:
    print("Password must have at least 8 characters")
    valid = False

if not any(ch.isupper() for ch in password):
    print("Password must contain an uppercase letter")
    valid = False

if not any(ch.islower() for ch in password):
    print("Password must contain a lowercase letter")
    valid = False

if not any(ch.isdigit() for ch in password):
    print("Password must contain a digit")
    valid = False

if not any(not ch.isalnum() for ch in password):
    print("Password must contain a special character")
    valid = False

if valid:
    print("Password is valid")
else:
    print("Password is invalid")
