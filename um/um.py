import re

def main():
    print(count(input("Text: ")),end='')


def count(s):
    # checks if W(no alphanum ) or start and ends with um
    count1 = re.findall(r"\bum\b" , s ,  re.IGNORECASE)

    return len(count1)

if __name__ == "__main__":
    main()
