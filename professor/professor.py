import random
import sys


def main():

    level = get_level()
    score = 0
    for i in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        sum = x+y
        attempts = 0


        while attempts<3:
            try:
                u_sum = int(input(f"{x} + {y} = "))

                if sum==u_sum:
                    score+=1
                    break

                else:
                    raise ValueError

            except (ValueError,NameError):
                attempts+=1
                print("EEE")

            if attempts==3:
                  print(f"{x} + {y} = {sum}")
    print("Score:",score)

def get_level():
    while 1:
        try:
            level =int(input("Level: "))
            if level  in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):

    if level==1:
        return random.randint(0,9)

    elif level == 2:
        return random.randint(10,99)

    elif level== 3:
        return random.randint(100,999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
