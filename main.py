from getpass import getpass
import math

COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "abc123",
    "password123",
    "admin",
    "letmein",
}

COMMON_SEQUENCES = {
    "1234",
    "2345",
    "3456",
    "abcd",
    "bcde",
    "cdef",
    "qwerty",
}

def check_length(password):
    return len(password) >= 8

def get_lenth_score(password):
    length = len(password)

    if length < 8:
        return 0
    elif length < 12:
        return 1
    elif length < 16:
        return 2
    else:
        return 3

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_number(password):
    return any(char.isdigit() for char in password)

def has_special_character(password):
    return any(not char.isalnum() for char in password)

def calculate_score(password):
    score = 0

    score += get_lenth_score(password)

    if has_lowercase(password):
        score += 1

    if has_uppercase(password):
        score += 1

    if has_number(password):
        score += 1

    if has_special_character(password):
        score += 1

    if is_common_password(password):
        score -= 2

    if has_repeated_characters(password):
        score -= 1

    if has_sequential_pattern(password):
        score -= 1

    return max(score, 0)

def get_strength(score, password):
    if not check_length(password):
        return "weak"

    if score <= 4:
        return "Medium"

    return "Strong"

def get_feedback(password):
    feedback = []

    if not check_length(password):
        feedback.append("Use at least 8 characters.")

    if not has_lowercase(password):
        feedback.append("Add a lowercase letter.")

    if not has_uppercase(password):
        feedback.append("Add an uppercase letter.")

    if not has_number(password):
        feedback.append("Add a number.")

    if not has_special_character(password):
        feedback.append("Add a special character.")

    if is_common_password(password):
        feedback.append("Avoid common or easily guessed passwords.")

    if has_repeated_characters(password):
        feedback.append("Avoid repeating the same character three or more times.")

    if has_sequential_pattern(password):
        feedback.append("Avoid predictable sequences like 1234 or abcd.")

    return feedback

def is_common_password(password):
    normalized = "".join(
        char for char in password.lower()
        if char.isalnum()
    )

    return normalized in COMMON_PASSWORDS

def has_repeated_characters(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False

def has_sequential_pattern(password):
    password = password.lower()

    for sequence in COMMON_SEQUENCES:
        if sequence in password:
            return True

    return False

def calculate_entropy(password):
    character_set_size = 0

    if any(char.islower() for char in password):
        character_set_size += 26

    if any(char.isupper() for char in password):
        character_set_size += 26

    if any(char.isdigit() for char in password):
        character_set_size += 10

    if any(not char.isalnum() for char in password):
        character_set_size += 32

    if character_set_size == 0:
        return 0

    return len(password) * math.log2(character_set_size)

password = getpass("Enter your password: ")
score = calculate_score(password)
entropy = calculate_entropy(password)
strength = get_strength(score, password)
common = is_common_password(password)
repeated = has_repeated_characters(password)
sequential = has_sequential_pattern(password)
feedback = get_feedback(password)

print("\nPassword checks:")

print(f"Length: {'OK' if check_length(password) else 'Missing'}")
print(f"Lowercase: {'OK' if has_lowercase(password) else 'Missing'}")
print(f"Uppercase: {'OK' if has_uppercase(password) else 'Missing'}")
print(f"Number: {'OK' if has_number(password) else 'Missing'}")
print(
    f"Special character: "
    f"{'OK' if has_special_character(password) else 'Missing'}"
)
print(f"\nStrength score: {score}/7")
print(f"Estimated entropy: {entropy:.1f} bits")
print(f"Strength: {strength}")
print(f"Common password: {'Yes' if common else 'no'}")
print(f"Repeated characters: {'Yes' if repeated else 'No'}")
print(f"Sequential pattern: {'Yes' if sequential else 'No'}")
print("\nSuggestions:")

if feedback:
    for suggestion in feedback:
        print(f"- {suggestion}")
else:
    print("- No obvious issues detected.")