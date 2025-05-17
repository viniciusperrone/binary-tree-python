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

    binary_tree.insert(node=5)
    binary_tree.insert(node=9)

    binary_tree.show()

    # Should returns False
    print(binary_tree.search(node=77))

    # Should returns True
    print(binary_tree.search(node=8))

    # Remove node 30
    binary_tree.remove(node=30)

    binary_tree.show()