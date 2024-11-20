import validators

def main():
    userIn = input("What's your email address? ")
    if validators.email(userIn) :
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__" :
    main()

