import re
import getpass


def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Determine password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    return strength, score, feedback


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = getpass.getpass("Enter a password to check: ")

    strength, score, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Score: {score}/5")

    if feedback:
        print("\nSuggestions for improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("\nAll five checks passed!")

    print("\nNote: This is a basic educational checker.")


if __name__ == "__main__":
    main()
