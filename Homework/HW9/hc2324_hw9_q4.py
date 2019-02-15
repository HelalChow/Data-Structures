import random
import UnsortedArrayMap as unsorted_map
import DoublyLinkedList


class ChainingHashTableMap:

    def __init__(self, N=64, p=40206835204840513073):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)
        self.DLL = DoublyLinkedList.DoublyLinkedList()

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        if self.table[i] is None:
            self.table[i] = unsorted_map.UnsortedArrayMap()
        old_size = len(self.table[i])
        self.table[i][key] = value
        new_size = len(self.table[i])
        if (new_size > old_size):
            self.n += 1
            self.DLL.add_last(key)
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        del curr_bucket[key]
        self.n -= 1
        if len(curr_bucket) == 0:
            self.table[i] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        cursor = self.DLL.header.next
        while cursor is not self.DLL.trailer:
            key = cursor.data
            index = self.hash_function(key)
            not_exist = False
            if self.table[index] is not None:
                for item in self.table[index]:
                    if item == key:
                        yield key
                        cursor = cursor.next
                        not_exist = True
            if not_exist == False:
                cursor = cursor.next
                self.DLL.delete_node(cursor.prev)

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        self.DLL = DoublyLinkedList.DoublyLinkedList()
        for (key, value) in old:
            self[key] = value
