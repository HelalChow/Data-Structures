#Iterators and Generators

"""lst = [1,2,3]
lst_iter = iter(lst)
p=next(lst_iter)
print(p)

s = "abc"
s_iter = iter(s)
end = False
while(end==False):
    try:
        item = next(s_iter)
        print(item)
    except StopIteration:
        end = True

for elem in my_range(3,10,0.5):
    print(elem)
def my_range(start,stop,step):
    res = []
    curr = start
    while(curr<stop):
        res.append(curr)
        curr+=step
    return res
#Each elem printed, prints a whole list created from my_range
"""

#GENERATORS#
def f():
    x=1
    yield x
    x +=1
    yield x
    x +=1
    yield x
g=f()
next(g) #Will print 1
next(g) #Will print 2
#Yield: Takes snapshot of the active data and stores it with the position from where execution should resume to (the next line)
#Next: Datat that was saved is restored and execution resumes where it takes off


def my_range(start,stop,step):
    curr = start
    while (curr<stop):
        yield curr
        curr += step
for elem in my_range(3,10,0.5):
    print(elem)

def factors(num):
    for curr in range(1,num+1):
        if num%curr ==0:
            yield curr
for elem in factors(21):
    print(elem)




