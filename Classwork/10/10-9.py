def factorial(n):
   if n==1:
       return 1
   else:
       rest = factorial(n-1)
       return n*rest

'''
***Recursive Tree*** 
1) Each recursive call is represented as a node in a tree. Inside each node is the side of the input it was called with
2) If 'A' directly calls 'B', we draw an edge from the node representing 'A' to the node representing 'B'
Cost: At the side of each node, write the local cost of the recursive call 
    (Without including the cost of the recursive call)
'''



def count_appearances(lst,val):
    def count_appearnces_helper(lst, low, high, val):
        if low == high:
            if lst[low] == val:
                return 1
            else:
                return 0
        else:
            count_rest = count_appearnces_helper(lst, low + 1, high, val)
            if lst[low] == val:
                return count_rest + 1
            else:
                return count_rest
    if len(lst)==0:
        return 0
    else:
        return count_appearances(lst,0,len(lst)-1,val)

#Theta of n
def power(x,n):
    if n==1:
        return x
    else:
        rest = power(x,n-1)
        return rest*x
print(power(4,2))

#Theta of log(n)
def power1(x,n):
    if n==1:
        return x
    else:
        hold =power(x,n//2)
        if n%2==0:
            return hold * hold
        else:
            return hold * hold * x