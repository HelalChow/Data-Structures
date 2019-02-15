import ArrayQueue


class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, root):
        if (root is None):
            return 0
        else:
            left_count = self.subtree_count(root.left)
            right_count = self.subtree_count(root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, root):
        if (root is None):
            return 0
        else:
            left_sum = self.subtree_sum(root.left)
            right_sum = self.subtree_sum(root.right)
            return root.data + left_sum + right_sum


    def height(self):
        return self.subtree_height(self.root)

    def subtree_height(self, root):
        if (root.left is None and root.right is None):
            return 0
        elif (root.left is  None):
            return 1 + self.subtree_height(root.right)
        elif (root.right is  None):
            return 1 + self.subtree_height(root.left)
        else:
            left_height = self.subtree_height(root.left)
            right_height = self.subtree_height(root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, root):
        if(root is None):
            return
        else:
            yield root
            yield from self.subtree_preorder(root.left)
            yield from self.subtree_preorder(root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_postorder(root.left)
            yield from self.subtree_postorder(root.right)
            yield root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_inorder(root.left)
            yield root
            yield from self.subtree_inorder(root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue.ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

    def leaves_list(self):
        if self.root is None:
            return []
        else:
            return [leaf_node.data for leaf_node in self.leaves_list_generator(self.root)]

    def leaves_list_generator(self, curr_root):
        if curr_root.left is None and curr_root.right is None:
            yield curr_root
        elif curr_root.left is None:
            yield from self.leaves_list_generator(curr_root.right)
        elif curr_root.right is None:
            yield from self.leaves_list_generator(curr_root.left)
        else:
            yield from self.leaves_list_generator(curr_root.left)
            yield from self.leaves_list_generator(curr_root.right)

    def iterative_inorder(self):
        if (self.root is None):
            return
        else:
            cursor = self.root
            while cursor is not None:
                if cursor.left is None:
                    yield cursor.data
                    cursor = cursor.right
                else:
                    left = cursor.left
                    while left.right is not None and left.right != cursor:
                        left = left.right
                    if left.right is None:
                        left.right = cursor
                        cursor = cursor.left
                    else:
                        left.right = None
                        yield cursor.data
                        cursor = cursor.right

