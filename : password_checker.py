# Muhammad Abd Ur Rehman

import string

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "111111", "letmein", "admin", "welcome"
}

def evaluate_password(password: str) -> dict:
    length_ok = len(password) >= 8
    is_common = password.lower() in COMMON_PASSWORDS

    if not length_ok or is_common:
        return {
            "length_ok": length_ok,
            "has_upper": False,
            "has_lower": False,
            "has_digit": False,
            "has_symbol": False,
            "is_common": is_common,
            "variety_score": 0,
            "strength": "Weak"
        }

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    variety_score = sum([has_upper, has_lower, has_digit, has_symbol])

    if variety_score >= 4 and len(password) >= 12:
        strength = "Strong"
    elif variety_score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return {
        "length_ok": length_ok,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "is_common": is_common,
        "variety_score": variety_score,
        "strength": strength
    }

def print_report(password: str, results: dict) -> None:
    print("\n--- Password Strength Report ---")
    print(f"Password length      : {len(password)} chars "
          f"({'OK' if results['length_ok'] else 'Too short (min 8)'})")
    print(f"Contains uppercase    : {'Yes' if results['has_upper'] else 'No'}")
    print(f"Contains lowercase    : {'Yes' if results['has_lower'] else 'No'}")
    print(f"Contains digit        : {'Yes' if results['has_digit'] else 'No'}")
    print(f"Contains symbol       : {'Yes' if results['has_symbol'] else 'No'}")
    if results["is_common"]:
        print("Warning               : This password appears in a common/leaked list!")
    print(f"Overall Strength      : {results['strength'].upper()}")
    print("---------------------------------\n")

def main():
    print("=== DecodeLabs Password Strength Checker ===")
    print("Type 'exit' to quit.\n")

    while True:
        password = input("Enter a password to check: ")
        if password.lower() == "exit":
            print("Goodbye!")
            break
        if not password:
            print("Please enter a non-empty password.\n")
            continue

        report = evaluate_password(password)
        print_report(password, report)

if __name__ == "__main__":
    main()
