def uniquelist(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
    print(uniquelist([1,2,3,3,5,6,7,9]))

    