

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    root: Node

    def __init__(self):
        self.root = None

    def insert(self, node: Node):
        self.root = self.__insert_recursive(node)

    def __insert_recursive(self, current: Node, node: int):
        if current is None:
            return Node(node)
        
        if current.value < node:
            current.left = self.__insert_recursive(current, node)

        elif current.value > node:
            current.right = self.__insert_recursive(current, node)

        return current