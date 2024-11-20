def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if 2 <= len(plate) <= 6 and plate.isalnum():
        # Return true if characters are all letters
        if plate.isalpha():
            return True
        else:
            # Check for number in the middle
            # (only if the first two characters are letters and the last character is number)
            if plate[:2].isalpha() and plate[-2:].isdigit():
                for i in range(len(plate)):
                    if plate[i].isdigit():
                        # Return false if number starts with 0 or the following character is letter
                        if plate[i].startswith("0") or plate[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    main()
