from getpass import getpass

def check_length(password):
    return len(password) >= 8

def has_lowercase(password):
    return any(char.lower() for char in password)

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_number(password):
    return any(char.isdigit() for char in password)

def has_special_character(password):
    return any(not char.isalnum() for char in password)

def calculate_score(password):
    score = 0

    if check_length(password):
        score += 1

    if has_lowercase(password):
        score += 1

    if has_uppercase(password):
        score += 1

    if has_number(password):
        score += 1

    if has_special_character(password):
        score += 1

    return score


password = getpass("Enter your password: ")
score = calculate_score(password)

print("\nPassword checks:")

print(f"Length: {'OK' if check_length(password) else 'Missing'}")
print(f"Lowercase: {'OK' if has_lowercase(password) else 'Missing'}")
print(f"Uppercase: {'OK' if has_uppercase(password) else 'Missing'}")
print(f"Number: {'OK' if has_number(password) else 'Missing'}")
print(
    f"Special character: "
    f"{'OK' if has_special_character(password) else 'Missing'}"
)
print(f"\nStrength score: {score}/5")