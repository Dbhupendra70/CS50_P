
import sys
import operator
from inflect import engine
from datetime import date

p= engine()

def main():
    try:
        birth_date = input("Date of Birth: ").strip()

        birth_date   = (date.fromisoformat(birth_date))
        this_d = date.today()

        difference = operator.sub(this_d , birth_date)
        print(total_time(difference.days))


    except (ValueError,TypeError):
        sys.exit("Invalid date")
    # if "-" in dat:
    #     year , month , day = dat.split("-")

def total_time(time):
    minutes = time * 24 * 60
    num_to_words = p.number_to_words(minutes , andword='').capitalize()
    return f"{num_to_words} minutes"

if __name__ == "__main__":
    main()
