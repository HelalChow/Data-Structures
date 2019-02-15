def list_min(lst, low, high):
    if low == high:
        return lst[low]
    else:
        hold = list_min(lst, low+1, high)
        if lst[low]<hold:
            return lst[low]
        else:
            return hold
