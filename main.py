""" Implementation of Tree data structures in Python """
import sys
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
    second.right = fifth
    third.left = sixth
    third.right = seventh


x.print_helper(x.root, "", True)