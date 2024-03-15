import pytest

import main

def test_node():
    first = main.Node(1)
    assert first.value == 1
    assert first.left is None
    assert first.right is None

def test_tree():
    a = main.Tree()
    assert a.root is None

@pytest.fixture
def full_binary_tree():
    x = main.Tree()

    first = main.Node(1)
    second = main.Node(2)
    third = main.Node(3)

    # connect nodes
    x.root = first
    x.root.left = second
    x.root.right = third

    return x

def test_is_binary_tree(full_binary_tree):
    assert full_binary_tree.is_full_binary(full_binary_tree.root) is True

    x = main.Tree()
    first = main.Node(1)
    x.root = first
    assert x.is_full_binary(x.root) is True

    second = main.Node(2)
    first.left = second
    assert x.is_full_binary(x.root) is False

    third = main.Node(3)
    first.right = third
    assert x.is_full_binary(x.root) is True

    fourth = main.Node(4)
    second.left = fourth
    assert x.is_full_binary(x.root) is False

def test_calculate_height(full_binary_tree):
    x = main.Tree()
    first = main.Node(1)
    x.root = first
    assert x.calculate_height(x.root) == 0

    assert full_binary_tree.calculate_height(full_binary_tree.root) == 1

    second = main.Node(2)
    first.left = second
    third = main.Node(3)
    second.left = third

    assert x.calculate_height(x.root) == 2

def test_is_complete_binary():
    x = main.Tree()
    x.root = main.Node(1)
    assert x.is_perfect_binary(x.root, x.calculate_height(x.root)) is True

    x.root.left = main.Node(2)
    assert x.is_perfect_binary(x.root, x.calculate_height(x.root)) is False

    x.root.right = main.Node(3)
    assert x.is_perfect_binary(x.root, x.calculate_height(x.root)) is True

    x.root.left.left = main.Node(4)
    x.root.left.right = main.Node(5)
    assert x.is_perfect_binary(x.root, x.calculate_height(x.root)) is False

def test_count_nodes():
    x = main.Tree()
    x.root = main.Node(1)
    assert x.count_nodes(x.root) == 1

    x.root.left = main.Node(2)
    assert x.count_nodes(x.root) == 2

    x.root.right = main.Node(3)
    assert x.count_nodes(x.root) == 3

    x.root.left.left = main.Node(4)
    x.root.left.right = main.Node(5)
    assert x.count_nodes(x.root) == 5

def test_is_complete_binary():
    x = main.Tree()
    x.root = main.Node(1)
    x.root.left = main.Node(2)
    assert x.is_complete_binary(x.root, 0, x.count_nodes(x.root)) is True

    x.root.right = main.Node(2)
    assert x.is_complete_binary(x.root, 0, x.count_nodes(x.root)) is True

    x.root.left.left = main.Node(3)
    x.root.left.right = main.Node(4)
    x.root.right.left = main.Node(5)
    x.root.right.right = None
    assert x.is_complete_binary(x.root, 0, x.count_nodes(x.root)) is True

    x.root.left.left = main.Node(3)
    x.root.left.right = main.Node(4)
    x.root.right.left = None
    x.root.right.right = main.Node(5)
    assert x.is_complete_binary(x.root, 0, x.count_nodes(x.root)) is False

    x.root.left.left = main.Node(3)
    x.root.left.right = None
    x.root.right.left = main.Node(4)
    x.root.right.right = main.Node(5)
    assert x.is_complete_binary(x.root, 0, x.count_nodes(x.root)) is False

    x.root.left.left = main.Node(3)
    x.root.left.right = None
    x.root.right.left = main.Node(4)
    x.root.right.right = None
    assert x.is_complete_binary(x.root, 0, x.count_nodes(x.root)) is False

    x.root.left.left = main.Node(3)
    x.root.left.right = main.Node(4)
    x.root.right.left = None
    x.root.right.right = None
    assert x.is_complete_binary(x.root, 0, x.count_nodes(x.root)) is True