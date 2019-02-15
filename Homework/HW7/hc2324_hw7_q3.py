def is_height_balanced(bin_tree):
    return is_height_balanced_helper(bin_tree.root)[0]

def is_height_balanced_helper(root):
    if (root.left is None) and (root.right is None):
        return True, 1
    else:
        if root.left is None and root.right is not None:
            left = True, 0
            right = is_height_balanced_helper(root.right)
        elif root.left is not None and root.right is None:
            left = is_height_balanced_helper(root.left)
            right = True, 0
        elif root.left is not None and root.right is not None:
            left = is_height_balanced_helper(root.left)
            right = is_height_balanced_helper(root.right)
        if abs(left[1] - right[1]) <= 1:
            height_balanced = True
        else:
            height_balanced = False
        height_total = max(left[1] + 1, right[1] + 1)
        node_bool = left[0] and right[0]
        total_bool = node_bool and height_balanced
        return total_bool, height_total

