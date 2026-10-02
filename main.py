from getpass import getpass

COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "abc123"
    "password123",
    "admin",
    "letmein",
}

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

def get_strength(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def is_common_password(password):
    return password.lower() in COMMON_PASSWORDS

def has_repeated_characters(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False

password = getpass("Enter your password: ")
score = calculate_score(password)
strength = get_strength(score)
common = is_common_password(password)
repeated = has_repeated_characters(password)

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
print(f"Strength: {strength}")
print(f"Common password: {'Yes' if common else 'no'}")
print(f"Repeated characters: {'Yes' if repeated else 'No'}")