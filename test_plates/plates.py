def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if length of plate is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Ensure the first two characters are alphabetic
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    found_digit = False  # Track if digits have been found
    for i in range(2, len(s)):  # Start checking from third character
        if s[i].isalpha():
            if found_digit:  # If a letter appears after digits, it's invalid
                return False
        elif s[i].isdigit():
            # Check that the first digit is not zero
            if not found_digit and s[i] == '0':
                return False
            found_digit = True
        else:
            return False  # Non-alphanumeric characters are invalid

    return True

if __name__ == "__main__":
    main()
