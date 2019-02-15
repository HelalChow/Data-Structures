#Question 1
def powers_of_two(num):
    for i in range(1,num+1):
        yield 2**i

#Question 2
def decimal_to_binary(int):
    if int==1:
        return "1"
    else:
        hold = decimal_to_binary(int-1)


#Question 3
def partition(lst):
    low = 1
    high = len(lst)-1
    pivot = lst[0]
    while low <= high:
        if lst[low]>pivot>lst[high]:
            lst[low],lst[high]=lst[high],lst[low]
            low+=1
            high-=1
        elif lst[low]<pivot>lst[high]:
            low+=1
        elif lst[low]>pivot<lst[high]:
            high-=1
        else:
            low+=1
            high-=1
    lst[low-1],lst[0]=lst[0],lst[low-1]

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
partition(lst)
print(lst)

class MyString():
    def __init__(self,str_input):
        self.str = str_input
    def __len__(self):
        return len(self.str)
    def __iter__(self):
        for i in range(len(self)):
            return self[i]
    def __repr__(self):
        str = ''

        return str
    def __getitem__(self, ind):
        if ind >= len(self):
            raise IndexError("Index is out of range")
        return self[ind]
    def __add__(self, other):
        new = self
        return new+other
    def __radd__(self, other):
        new = self
        return new + other
    def upper(self):
        new = ''
