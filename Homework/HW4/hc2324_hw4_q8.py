def flat_list(nested_lst,low,high):
    if low==high:
        if isinstance(nested_lst[low],list):
            return flat_list(nested_lst[low],0,len(nested_lst[low])-1)
        else:
            return [nested_lst[low]]
    else:
        rest = flat_list(nested_lst,low+1,high)
        if isinstance(nested_lst[low], list):
            return flat_list(nested_lst[low],0,len(nested_lst[low])-1)+rest
        else:
            return [nested_lst[low]]+rest

