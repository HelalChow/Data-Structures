class Polynomial:
    def __init__(self,lst=[0]):
        self.lst = lst
    def __repr__(self):
        poly = ""
        for i in range(len(self.lst)-1,0,-1):
            if i == 1:
                poly += str(self.lst[i])+"x^"+str(i)+"+"+str(self.lst[0])
            else:
                poly += str(self.lst[i]) + "x^" + str(i)+"+"
        count = poly.count("-")
        for i in range(count):
            minus=poly.find("-")
            poly = poly[:minus-1]+poly[minus:]
        return poly

    def evaluate(self, val):
        sum = 0
        for i,j in enumerate(self.lst):
            sum+=j*val**i
        return sum

    def __add__(self, other):
        new = []
        count=0
        if len(self.lst)>len(other.lst):
            for i in range(len(other.lst)):
                sum=self.lst[i]+other.lst[i]
                new.append(sum)
                count=i+1
            for i in range(count,len(self.lst)):
                new.append(self.lst[i])
        else:
            for i in range(len(self.lst)):
                sum=self.lst[i]+other.lst[i]
                new.append(sum)
                count=i+1
            for i in range(count,len(other.lst)):
                new.append(other.lst[i])
        return Polynomial(new)

    def __mul__(self, other):
        new = [0]*(len(self.lst)+len(other.lst)-1)
        for i,j in enumerate(self.lst):
            for k,l in enumerate(other.lst):
                new[i+k] += j*l
        return Polynomial(new)
    def derive(self):
        new = []
        for i,j in enumerate(self.lst):
            new.append(j*i)
        new.pop(0)
        return Polynomial(new)

def main():
    test1 = Polynomial([3,7,0,-9,2])
    test2 = Polynomial([1,2])
    test_eval = Polynomial([3, 7, 0, -9, 2]).evaluate(2)
    test_add = test1+test2
    mul = test1*test2
    derive = Polynomial([3,7,0,-9,2]).derive()
    print(derive)
main()

