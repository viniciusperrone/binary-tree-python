

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    root: Node

    def __init__(self):
        self.root = None

    def insert(self, node: int):
        self.root = self.__insert_recursive(self.root, node)

    def __insert_recursive(self, current: Node, node: int):
        if current is None:
            return Node(node)
        
        if node < current.value:
            current.left = self.__insert_recursive(current.left, node)
        elif node > current.value:
            current.right = self.__insert_recursive(current.right, node)

        return current
    
    def show(self):
        self.__show_recursive(self.root, 0)

    def __show_recursive(self, current: Node, level: int):
        
        if current:
            if level > 0:
                print("    " * (level - 1) + "└----")

            print(current.value)

            self.__show_recursive(current.left, level + 1)
            self.__show_recursive(current.right, level + 1)


if __name__ == '__main__':
    binary_tree = BinaryTree()

    binary_tree.insert(node=20)

    binary_tree.insert(node=25)
    binary_tree.insert(node=10)

    binary_tree.insert(node=8)
    binary_tree.insert(node=30)
    binary_tree.insert(node=22)

    binary_tree.insert(node=35)
    binary_tree.insert(node=23)

    binary_tree.show()