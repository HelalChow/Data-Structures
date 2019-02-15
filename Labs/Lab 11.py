from ADT import LinkedBinaryTree


def count_val(root, val):
    if root is None:
        return 0
    else:
        left = count_val(root.left, val)
        right = count_val(root.right, val)
        count = 0
        if root.data == val:
            count = 1
        return count + left + right


def right_circular_shift(lnk_lst):
    last = lnk_lst.trailer.prev
    first = lnk_lst.header.next
    last.prev.next = lnk_lst.trailer
    lnk_lst.trailer.prev = last.prev
    last.prev = lnk_lst.header
    lnk_lst.header.next = last
    last.next = first
    first.prev = last



def reverse(root):
    if root is None:
        return root
    else:
        left = reverse(root.left)
        right = reverse(root.right)
        new_root = LinkedBinaryTree.Node(root)
        new_root.left = right
        left.parent = new_root
        new_root.right = left
        right.parent = new_root
        return new_root



