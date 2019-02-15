def count_lowercase(s,low,high):
    if low==high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        hold = count_lowercase(s,low+1,high)
        if s[low].islower():
            return hold + 1
        else:
            return hold

def is_number_of_lowercase_even(s,low,high):
    if low==high and s[low].islower():
        return False
    else:
        hold = is_number_of_lowercase_even(s,low+1,high)
        if s[low].islower() and hold==False:
            return True
        elif s[low].islower() and hold==True:
            return False
        else:
            return hold
