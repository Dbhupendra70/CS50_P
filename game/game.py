import random
#using imfinite loop to ensure user get re-prompted if input is not Number
while 1:

    try:
        n=int(input("Level: "))
        if n>=0:
            #generating a random input inbetween 1-n
            g = random.randint(1,n)
            while 1:
                try:
                    guess=int(input("Guess: "))
                    if guess<1:
                        continue
                    else:
                        if guess<g:
                                print("Too small!")
                        elif guess>g:
                                print("Too large!")
                        else:
                                print("Just right!")
                                raise EOFError
                except ValueError:
                    pass

    except ValueError:
        pass
    except EOFError:
        break

