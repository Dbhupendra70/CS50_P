import inflect

p = inflect.engine()
#we are going to use join() method from inflect package
inp_list=[]
while 1:
    try:
        userInput= input("Name: ").strip().title()
        inp_list.append(userInput)
    except EOFError:
        break
print("\nAdieu, adieu, to",p.join(inp_list))
