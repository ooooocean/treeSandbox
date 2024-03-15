""" Implementation of Tree data structures in Python """
import sys
from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def print_helper(self, currPtr, indent, last):
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.value)
            self.print_helper(currPtr.left, indent, False)
            self.print_helper(currPtr.right, indent, True)

    def inorder(self, root):
        # starting with the root as the input, we traverse to left subtree first
        if root:
            self.inorder(root.left)
            # this recursion repeats until there is no more left subtrees
            # in this case, we will take the value out of the root
            print(str(root.value) + '->', end='')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(str(root.value) + '->', end='')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.value) + '->', end='')

    def is_full_binary(self, root):
        # empty tree case
        if root is None:
            return True
        # if child is not present, then return True
        if root.left is None and root.right is None:
            return True

        # if child is present, we want to keep recursing
        if root.left is not None and root.right is not None:
            return self.is_full_binary(root.left) and self.is_full_binary(root.right)

        return False

    def calculate_height(self, node):
        # helper function to calculate height of a node in a tree, assuming tree is perfect
        h = 0
        while node.left is not None:
            h += 1
            node = node.left
        return h

    def is_perfect_binary(self, root, height, level=0):
        # empty tree case
        if root is None:
            return False
        print(f'height={height}, we are at level={level} checking root of value {root.value}' )

        # check for no children. the recursion loop works through each 'layer' of the tree and if we find that the
        # the level does not equal the height, then the leaf nodes are not all on the same level
        if root.left is None and root.right is None:
            print('node has no children, checking if height equals level')
            return height == level

        # check for if only one children. Regardless of other subtrees, this automatically fails
        if root.left is None or root.right is None:
            print('one child is null')
            return False

        # remaining scenario is where there are subtrees in both, so repeat the previous
        return self.is_perfect_binary(root.left, height, level+1) and self.is_perfect_binary(root.right, height, level+1)

    def count_nodes(self, root):
        # define terminal state
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


if __name__ == '__main__':
    # initialise a tree
    x = Tree()

    # create nodes
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)

    # connect nodes
    x.root = first
    x.root.left = second
    x.root.right = third
    second.left = fourth
