def find_lst_max(lst):
    if len(lst)==1:
        return lst[0]
    else:
        hold = find_lst_max(lst[1:])
        return max(lst[0],hold)
print(find_lst_max( [1,2,3,4,5,100,12,2]))

def product_evens(n):
    if n==2:
        return n
    else:
        if n%2==0:
            return n*product_evens(n-2)
        else:
            return n*product_evens(n-1)
#print(product_evens(8))

def is_palindrome(str, low, high):
    if low>=high:
        return False
    elif high - low == 2 or high-low ==1:
        if str[low]==str[high]:
            return True
        else:
            return False
    else:
        hold = is_palindrome(str,low+1,high-1)
        if str[low]==str[high] and hold ==True:
            return True
        else:
            return False
#print(is_palindrome("mam",0,2))

def binary_search(lst,val,low,high):
    if high==low:
        if lst[low]==val:
            return lst.index(val)
        else:
            return
    else:
        mid = (high +low)//2
        if lst[mid]>=val:
            return binary_search(lst,val,low,mid)
        else:
            return binary_search(lst,val,mid+1,high)
lst=[1,2,3,4,5,6,7,8,9,10]
#print(binary_search(lst,5,0,9))

def nested_sum(lst):
    sum = 0
    for i in lst:
        if isinstance(i, list):
            sum = sum+ nested_sum(i)
        else:
            sum += i
    return sum

#print(nested_sum( [1,[2,3,4]]))