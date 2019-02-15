def shift(lst,k,direction="left"):
    for i in range(k):
        if direction == "right":
            lst.insert(0, lst[len(lst) - 1])
            lst.pop(len(lst) - 1)
        else:
            lst.append(lst[0])
            lst.pop(0)
    return lst




