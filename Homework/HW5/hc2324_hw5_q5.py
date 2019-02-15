from ADT import ArrayQueue, ArrayStack


def permutations(lst):
    perm_queue = ArrayQueue.ArrayQueue()
    res_lst = []

    for elem in lst:
        perm_queue.enqueue([elem])
        unused_stack = ArrayStack.ArrayStack()
        for other_elem in lst:
            if other_elem != elem:
                unused_stack.push(other_elem)
        while len(perm_queue.first()) < len(lst):
            while not (unused_stack.is_empty()):
                perm_queue.enqueue(perm_queue.first() + [unused_stack.pop()])
            perm_queue.dequeue()
            for final_elem in lst:
                if final_elem not in perm_queue.first():
                    unused_stack.push(final_elem)
        while not (perm_queue.is_empty()):
            res_lst.append(perm_queue.dequeue())
        return res_lst

print(permutations([1,2,3,4]))