from ADT import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.comp_str = DoublyLinkedList.DoublyLinkedList()
        curr = ['', 0]
        for i in orig_str:
            if curr[0] == '':
                curr[0] = i
                curr[1] = 1
            elif i == curr[0]:
                curr[1] += 1
            elif i != curr[0]:
                self.comp_str.add_last((curr[0],curr[1]))
                curr[0] = i
                curr[1] = 1
        self.comp_str.add_last((curr[0], curr[1]))


    def __add__(self, other):
        sum = DoublyLinkedList.DoublyLinkedList()
        last_type = self.comp_str.last_node().data[0]
        first_type = other.comp_str.first_node().data[0]
        if last_type == first_type:
            last_node = self.comp_str.last_node().data
            first_node = other.comp_str.first_node().data
            for i in self.comp_str:
                if i != last_node:
                    sum.add_last(i)
                else:
                    sum.add_last((last_type,last_node[1]+first_node[1]))
            for i in other.comp_str:
                if i is not first_node:
                    sum.add_last(i)
        else:
            for i in self.comp_str:
                sum.add_last(i)
            for i in other.comp_str:
                sum.add_last(i)
        return sum

    def __lt__(self, other):
        if self.comp_str.size < other.comp_str.size:
            return True
        else:
            return False

    def __le__(self, other):
        if self.comp_str.size <= other.comp_str.size:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.comp_str.size > other.comp_str.size:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.comp_str.size >= other.comp_str.size:
            return True
        else:
            return False

    def __repr__(self):
        str = ""
        for i in self.comp_str:
            str = str + i[0]*i[1]
        return str

s1 = CompactString('aaaaabbbaaac')
s2 = CompactString('aaaaaaacccaaaa')
print(s1, s2)
s3 = s2 + s1 #in s3’s linked list there will be 6 ’real’ nodes
print(s3)
print(s1 >= s2)
