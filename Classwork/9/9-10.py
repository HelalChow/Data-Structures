#basic syntax
def tens_lst(n):
    return[10*i for i in range(1,n+1)]

def str_data(s):
    return[(i,ord(i)) for i in s]

def ext_str_data(s):
    return[(i,s[i],ord(s[i])) for i in range(len(s))]

#Extended syntax
def factors_list(num):
    return[i for i in range(1, num+1) if num%i==0]

class Counter:
    def __init__(self):
        self.val=0
    def inc(self):
        self.val +=1
    def __repr__(self):
        return str(self.val)

lst1 = [Counter()]*3
for c in lst1:
    c.inc()
    #print(c)
#multiplying creates new list with 3 elements, each referring to Counter

lst2=[Counter() for i in range(3)]
for c in lst2:
    c.inc()
    #print(c)

#ITERATOR
lst=[1,2,3]
s="abc"
r=range(3)
lst_iter=iter(lst)
s_iter=iter(s)
r_iter=iter(r)
next(lst_iter)

