def shift(lst,k):
    for i in range(k):
        lst.append(lst[0])
        lst.pop(0)
    return lst


