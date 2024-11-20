def main():

    months= [

        "January",

        "February",

        "March",

        "April",

        "May",

        "June",

        "July",

        "August",

        "September",

        "October",

        "November",

        "December"

    ]

    while 1:

        try:
            userD= input("Date: ")

            if "/" in userD:
                userl = userD.split("/")

            elif "," in userD:

                userl = userD.replace(",","")
                userl= userl.split()

                month =months.index(userl[0])+1
                userl[0]=(month)

            if int(userl[0])>12 or int(userl[1])>31:
                raise ValueError
        except (ValueError, NameError,IndexError):
            pass
        else:
            print(f"{int(userl[2])}-{int(userl[0]):02}-{int(userl[1]):02}")
            break
main()
