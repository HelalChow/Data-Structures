#Sorting Problem
def merge_sort(lst):
    pass

def merge_sort_helper(lst,low,high):
    if low == high:
        return
    else:
        mid = (low + high)//2
        merge_sort_helper(lst,low,mid)
        merge_sort_helper(lst,mid+1,high)
        merge(lst,low,mid,high)
def merge(lst,low,mid,high):
    pass








