x = input("camelCase: ")
print("snake_case: ", end="")
for i in x :
    if i.islower():
        print(i,end="")
    else :
        print("_"+i.lower(),end="")
print()
