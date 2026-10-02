from getpass import getpass

def check_length(password):
    return len(password) >= 8

def has_lowercase(password):
    return any(char.lower() for char in password)

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_number(password):
    return any(char.isdigit() for char in password)

password = getpass("Enter your password: ")

print("\nPassword checks:")

print(f"Length: {'OK' if check_length(password) else 'Missing'}")
print(f"Lowercase: {'OK' if has_lowercase(password) else 'Missing'}")
print(f"Uppercase: {'OK' if has_uppercase(password) else 'Missing'}")
print(f"Number: {'OK' if has_number(password) else 'Missing'}")
