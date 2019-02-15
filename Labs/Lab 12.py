import csv
import BinarySearchTreeMap
import random


def check_elements(tree1, tree2):
    elem = []
    for i in tree1:
        elem.append(i)
    count = 0
    for i in tree2:
        if i != elem[count]:
            return False
        count += 1
    return True

def is_bst_helper(curr_root):
    if curr_root.left is None and curr_root.right is None:
        return (True, curr_root.data)
    else:
        left = is_bst_helper(curr_root.left)
        right = is_bst_helper(curr_root.right)
        if left[0] is False or right[0] is False:
            return (False, curr_root.data)
        elif curr_root.left is None and curr_root.right is not None:
            if curr_root.data < right[1]:
                return (True, curr_root.data)
        elif curr_root.left is not None and curr_root.right is None:
            if curr_root.data > left[1]:
                return (True, curr_root.data)
        elif curr_root.data > left[1] and curr_root.data < right[1]:
            return (True, curr_root.data)
        else:
            return (False, curr_root.data)


def create_tree():
    ns = [2**i for i in range(3, 16)]
    size_lst = []
    height_lst = []
    for n in ns:
        tree = BinarySearchTreeMap.BinarySearchTreeMap()
        for i in range(1,12):
            tree.insert(i)
        size_lst.append(n)
        height_lst.append(tree.height())
    create_csv(size_lst, height_lst)



def create_csv(sizes_lst, heights_lst):
    file = open('heights.csv','w')
    if len(sizes_lst) != len(heights_lst):
        raise Exception("lists given must be of equal sizes")
    for i in range(len(sizes_lst)):
        file.write(str(sizes_lst[i]) + "," + str(heights_lst[i]) +
    '\n')
    file.close()


def height_from_node(tree, node):
    count = 0
    curr = tree.root
    while curr is not node:
        if curr.data > node.data:
            curr = curr.left
            count += 1
        else:
            curr = curr.right
            count += 1
    return count

    
def fca_bst(bst, node_a, node_b):
    height_a = height_from_node(bst, node_a)
    height_b = height_from_node(bst, node_b)
    curr_a = node_a
    curr_b = node_b
    while True:
        if curr_a == curr_b:
            return curr_a
        elif height_a <= height_b:
            curr_a = curr_a.parent
            height_a += 1
        elif height_b < height_a:
            curr_b = curr_b.parent
            height_b += 1



tree = BinarySearchTreeMap.BinarySearchTreeMap()
for i in range(1,12):
    tree.insert(random.randint(1, 1000000))
fca_bst(tree, tree.root.left, tree.root.right)







