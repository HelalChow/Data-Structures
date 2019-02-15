import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    exp_list = prefix_exp_str.split()
    return create_expression_tree_helper(exp_list, 0)

def create_expression_tree_helper(prefix_exp, start_pos):
    op = '+-*/'
    if prefix_exp[start_pos] not in op:
        root = LinkedBinaryTree.Node(int(prefix_exp[start_pos]))
        subtree = LinkedBinaryTree(root)
        return subtree
    else:
        root = LinkedBinaryTree.Node(prefix_exp[start_pos])
        left_tree = create_expression_tree_helper(prefix_exp, start_pos + 1)
        right_tree = create_expression_tree_helper(prefix_exp, start_pos + 2)
        root.left = left_tree.root
        root.right = right_tree.root
        subtree = LinkedBinaryTree(root)
        return subtree

def prefix_to_postfix(prefix_exp_str):
    prefix_bin_tree = create_expression_tree(prefix_exp_str)
    return " ".join([str(node.data) for node in prefix_bin_tree.postorder()])
