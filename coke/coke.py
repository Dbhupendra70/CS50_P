amountDue=50

while amountDue>0:
    print(f"Amount Due: {amountDue}")
    insCoin=int(input("Insert Coin: "))
    if insCoin in [5,10,25]:
        amountDue-=insCoin


else:
    print(f"Change Owed: {abs(amountDue)}")
