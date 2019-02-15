def permutations(lst,low,high):
    if low==high:
        return [lst]

    new_lst = []
    for i in range(high-low+1):
        lst_copy = lst[:]
        lst_copy[low],lst_copy[high-i]=lst_copy[high-i],lst_copy[low]
        new_lst.extend(permutations(lst_copy,low+1,high))

    return  new_lst

