def max_and_min(bin_tree):
    if len(bin_tree) == 0:
        raise Exception("Binary Tree is Empty")
    return subtree_min_and_max(bin_tree.root)

def subtree_min_and_max(subtree_root):
    if subtree_root is None:
        return (0,0)
    else:
        left = subtree_min_and_max(subtree_root.left)
        right = subtree_min_and_max(subtree_root.right)
        curr_max = max(subtree_root.data, left[1], left[1])
        curr_min = min(subtree_root.data, left[0], right[0])
        return (curr_min, curr_max)

