class UnsortedArrayMap:
    class Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):
        for item in self.table:
            if item.key == key:
                return item.value
        raise KeyError("Key Error: " + str(key))

    def __setitem__(self, key, value):
        for item in self.table:
            if item.key == key:
                item.value = value
                return
        new_item = UnsortedArrayMap.Item(key, value)
        self.table.append(new_item)

    def __delitem__(self, key):
        for i in range(len(self)):
            if self.table[i] == key:
                self.table.pop(i)
            return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key

