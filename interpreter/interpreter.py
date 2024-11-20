




e = input("Expression: ")
x,y,z = e.split(' ')
x = int(x)
z = int(z)
match y:
    case '+' :
        print (float(x+z))
    case '-':
        print (float(x-z))
    case '*':
        print (float(x*z))
    case '/':
        print (float(x/z))
    case _:
        print ("invalid input")