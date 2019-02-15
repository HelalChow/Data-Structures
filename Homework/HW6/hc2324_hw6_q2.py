from ADT import DoublyLinkedList


class Integer:
    def __init__(self, num_str):
        self.num = DoublyLinkedList.DoublyLinkedList()
        for i in num_str:
            self.num.add_last(i)

    def __add__(self, other):
        last_num = self.num.last_node()
        last_other = other.num.last_node()
        hold = 0
        sum = DoublyLinkedList.DoublyLinkedList()
        if len(self.num) > len(other.num):
            min_num = len(other.num)
            excess = len(self.num) - min_num
        else:
            min_num = len(self.num)
            excess = len(other.num) - min_num
        for i in range(min_num):
            add = int(last_num.data) + int(last_other.data)
            curr = add % 10
            sum.add_first(curr + hold)
            hold = add // 10
            last_num = last_num.prev
            last_other = last_other.prev
        if len(self.num) >= len(other.num):
            for i in range(excess):
                add = int(last_num.data) + hold
                sum.add_first(add % 10)
                hold = add // 10
                last_num = last_num.prev
        else:
            for i in range(excess):
                add = int(last_other.data) + hold
                sum.add_first(add % 10)
                hold = add // 10
                last_other = last_other.prev
        if hold != 0:
            sum.add_first(hold)

        return Integer(sum)

    def __repr__(self):
        str_num = ''
        for i in self.num:
            str_num = str_num + str(i)
        return str_num
