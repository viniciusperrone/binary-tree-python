

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

    def remove(self, node: int):
        
        self.root = self.__remove_recursive(self.root, node)

    def __remove_recursive(self, current: Node, node: int):
        
        if current is None:
            return None
        
        if node == current.value:

            if current.left is None and current.right is None:
                return None
            
            if current.left is None:
                return current.right
            
            if current.right is None:
                return current.left
            
        if node < current.value:
            current.left = self.__remove_recursive(current.left, node)

            return current

        current.right = self.__remove_recursive(current.right, node)

        return current
    
    def search(self, node: int) -> bool:
        return self.__search_recursive(self.root, node)

    def __search_recursive(self, current: Node, node: int) -> bool:
        if current is None:
            return False
        
        if current.value == node:
            return True
        
        return self.__search_recursive(current.left, node) if node < current.value else self.__search_recursive(current.right, node) 

    def show(self):
        self.__show_recursive(self.root, 0)

    def __show_recursive(self, current: Node, level: int):
        
        if current:
            if level > 0:
                print("    " * (level - 1) + f"└── {current.value}")
            else:
                print(current.value)

            self.__show_recursive(current.left, level + 1)
            self.__show_recursive(current.right, level + 1)
   