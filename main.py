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

    def is_complete_binary(self, root, index, number_of_nodes):
        # define terminal state when tree empty
        if root is None:
            return True
        if index >= number_of_nodes:
            # the resulting index should never exceed the number of nodes
            return False
        # if there is a break in children where left is none and right is not, then we break
        if root.left is None and root.right is not None:
            return False
        # then, we make use of the fact that the for the ith element of the array that populates the tree,
        # the left child has index 2i+1 and the right child has index 2i+2
        # these can then be recursively fed in until we assign a value that is null to the input of the recursion
        return self.is_complete_binary(root.left, 2*index + 1, number_of_nodes) and self.is_complete_binary(root.right, 2*index + 2, number_of_nodes)

    def search_binary_tree(self, root, value):
        # terminal state
        if root is None:
            return None
        # match scenario
        if value == root.value:
            return root
        # if we don't match, then we check the value of the node we are on to see which subtree we access
        if value < root.value:
            return self.search_binary_tree(root.left, value)
        if value > root.value:
            return self.search_binary_tree(root.right, value)
        return None

    def insert_binary_tree(self, root, value):
        # terminal state is when we reach a leaf node that is null.
        # we then set
        if root is None:
            root = Node(value)
        # logic for traversing subtrees
        if value < root.value:
            root.left = self.insert_binary_tree(root.left, value)
        if value > root.value:
            root.right = self.insert_binary_tree(root.right, value)
        return root

    def delete_binary_tree(self, node):

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

    # initialise a bst
    bst = Tree()
    bst.root = Node(8)

    bst.root.left = Node(3)
    bst.root.right = Node(10)

    bst.root.left.left = Node(1)
    bst.root.left.right = Node(6)
    bst.root.right.right = Node(14)

    bst.root.left.right.left = Node(4)
    bst.root.left.right.right = Node(7)
