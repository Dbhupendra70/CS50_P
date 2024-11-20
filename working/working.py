"""
Points to remember
1.) colon and minutes in time are optional while "to" is fixed.
2.) Hour in 12 hour format cannot be greater than 12. Fit for Test case
3.) Minute cannot be greater than 59. Fit for Test case
4.) Minute will be always of 2 digits. Example: 1 minute = 01, 2 minutes = 02
5.) It can either be AM or PM, not both. No space or period in between.
6.) Any format other than 4 given above, raise ValueError. Fit for Test Case.

"""

import re



def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$",s, re.I)

    if time:
        time_parts = list(time.groups())

        if time_parts[1] == None:
            time_parts[1] = 0

        if time_parts[4] == None:
            time_parts[4] = 0

        if int(time_parts[0]) > 12 or int(time_parts[3]) > 12:
            raise ValueError

        if int(time_parts[1]) > 59 or int(time_parts[4]) > 59:
            raise ValueError

        lhs_time = formater(time_parts[0],time_parts[1],time_parts[2])
        rhs_time = formater(time_parts[3],time_parts[4],time_parts[5])

        return lhs_time + " to " + rhs_time
    else:
        raise ValueError

def formater(hh,mm,xx):
    if xx == "PM":
        if int(hh) == 12:
            new_hh = 12
        else:
            new_hh = int(hh) + 12
    else:
        if int(hh) == 12:
            new_hh = 0
        else:
            new_hh = int(hh)

    new_time = (f"{new_hh:02}") + ":" + (f"{mm:02}")
    return new_time

if __name__ == "__main__":
    main()
