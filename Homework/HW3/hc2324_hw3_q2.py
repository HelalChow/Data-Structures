import ctypes
def make_array(n):
    return(n*ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1
    def __len__(self):
        return self.n
    def append(self, val):
        if self.n==self.capacity:
            self.resize(2*self.capacity)
        self.data[self.n] = val
        self.n += 1
    def resize(self, new_capacity):
        new_data = make_array(new_capacity)
        for i in range(self.n):
            new_data[i]=self.data[i]
        self.data = new_data
        self.capacity = new_capacity
    def __getitem__(self, index):
        if index >= self.n or index < -1*self.n:
            raise IndexError("Index " + str(index) + " is out of range")
        if index>=0:
            return self.data[index]
        else:
            return self.data[len(self)+index]
    def __setitem__(self, index, val):
        if index >= self.n or index < -1 * self.n:
            raise IndexError("Index " + str(index) + " is out of range")
        if index >= 0:
            self.data[index] = val
        else:
            self.data[len(self) + index] = val
    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]
    def extend(self, other):
        for elem in other:
            self.append(elem)
    def __repr__(self):
        lst = "["+",".join(str(elem) for elem in self)+"]"
        return lst
    def __add__(self, other):
        lst3=MyList()
        lst3.extend(self)
        lst3.extend(other)
        return lst3

    def __iadd__(self, other):
        for i in range(len(other)-1):
            self.append(other.data[i])
        return self

    def __mul__(self, other):
        new_lst = MyList()
        for i in range(other):
            new_lst.extend(self)
        return new_lst
    def __rmul__(self, other):
        new_lst = MyList()
        for i in range(other):
            new_lst.extend(self)
        return new_lst

    def insert(self, index ,val):
        if index>=self.n or index < -1*self.n:
            raise IndexError("Index " + str(index)+ " is out of range")
        if self.n+1==self.capacity:
            self.resize(2*self.capacity)
        for i in range(index,len(self)-1,-1):
            self.data[i+1] = self.data[i]
        self.data[index]=val

    def pop(self, index = None):
        if index == None:
            index = len(self) - 1
            if self.n==0 or self.data[0]==None:
                raise IndexError("List contains no value to be popped")
            elif index>=self.n or index < -1*self.n:
                raise IndexError("Index " + str(index)+ " is out of range")
            pop = self.data[len(self) - 1]
            self.data[len(self)-1]=None
            self.n -= 1
            if self.n<self.capacity//4:
                self.capacity=self.capacity//2
            return pop
        else:
            if self.n==0 or self.data[0]==None:
                raise IndexError("List contains no value to be popped")
            elif index>=self.n or index < -1*self.n:
                raise IndexError("Index " + str(index)+ " is out of range")
            pop = self.data[index]
            self.data[index]=None
            for i in range(index,len(self)-1):
                self.data[i]=self.data[i+1]
                self.data[i+1]=None
            self.n -= 1
            if self.n < self.capacity // 4:
                self.capacity = self.capacity // 2
            return pop