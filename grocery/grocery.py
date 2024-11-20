grocery={}

while True:
    try:
        item = input().strip().upper()
        if item not in grocery:
            grocery[item]=1
        else:
            grocery[item]+=1

    except EOFError:
        sort_dic = dict(sorted(list(grocery.items())))
        for item in sort_dic :
            print(sort_dic[item],item, sep=" ")
        break
    except KeyError:
        pass

