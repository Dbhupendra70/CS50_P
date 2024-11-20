menu={
    "Baja Taco":4.25,
    "Burrito":7.50,
    "Bowl":8.50,
    "Nachos":11.00,
    "Quesadilla":8.50,
    "Super Burrito":8.50,
    "Super Quesadilla":9.50,
    "Taco":3.00,
    "Tortilla Salad":8.00
}
#Initialising the total
total=0
#Infinite loop to promp user input
while 1:
    try:
        item=input("Item: ").strip().title()
        #checks for item in menu
        if item in menu:
            total+=menu[item]
            print(f"Total: ${total:.2f}")
    except EOFError:
        #to end input and get out of loop

        break
