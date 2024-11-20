def facts (k):
    if k in dict :
        print(f"Calories: {dict[k]}")

dict = {"apple":130,"banana":110,
        "watermelon":80, "tangerine":50,
        "sweet cherries":100, "straberries":50,
        "plums":70,"pineapple":50,
        "pear":100,"peach":60,
        "orange":80, "nectarine":60,
        "lime":20, "lemon":15 ,
        "kiwifruit":90 , "honeydew melon":50 ,
        "grapes":90 , "grapefruit": 60,
        "cantaloupe":50 , "avocado":50 }

item = input("Item: ")
item = item.lower()
facts(item)

