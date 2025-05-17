from binary_tree import BinaryTree
from interface import Interface


if __name__ == '__main__':
    binary_tree = BinaryTree()
    interface = Interface()

    while interface.option != 5:
        interface.show_menu()
        interface.choose_option()

        match interface.option:
            case 1:
                node = interface.get_value()

                binary_tree.insert(node=node)

            case 2:
                print('\n')
                binary_tree.show()

            case 3:
                node = interface.get_value()

                result = binary_tree.search(node=node)

                print('\nEncontrado!\n') if result else print('\nNão encontrado\n')

            case 4:
                node = interface.get_value()

                binary_tree.remove(node=node)

                print('\nValor removido!\n')

            case 5:
                break

            case _:
                pass


    # binary_tree.insert(node=20)

    # binary_tree.insert(node=25)
    # binary_tree.insert(node=10)

    # binary_tree.insert(node=8)
    # binary_tree.insert(node=30)
    # binary_tree.insert(node=22)

    # binary_tree.insert(node=35)
    # binary_tree.insert(node=23)

    # binary_tree.insert(node=5)
    # binary_tree.insert(node=9)

    # binary_tree.show()

    # Should returns False
    # print(binary_tree.search(node=77))

    # Should returns True
    # print(binary_tree.search(node=8))

    # Remove node 30
    # binary_tree.remove(node=30)

    # binary_tree.show()