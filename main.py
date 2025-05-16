from binary_tree import BinaryTree
from interface import Interface


if __name__ == '__main__':
    binary_tree = BinaryTree()
    interface = Interface()

    binary_tree.insert(node=20)

    binary_tree.insert(node=25)
    binary_tree.insert(node=10)

    binary_tree.insert(node=8)
    binary_tree.insert(node=30)
    binary_tree.insert(node=22)

    binary_tree.insert(node=35)
    binary_tree.insert(node=23)

    binary_tree.show()