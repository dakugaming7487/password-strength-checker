from getpass import getpass

def check_length(password):
    return len(password) >= 8

password = getpass("Enter your password: ")

print("\nPassword checks:")

print(f"Length: {'OK' if check_length(password) else "Missing"}")

