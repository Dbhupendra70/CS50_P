import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression for validating IPv4 address
    pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"

    # Use re.search
    if re.search(pattern, ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

