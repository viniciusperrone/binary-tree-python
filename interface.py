

class Interface:

    def __init__(self):
        self.option = None

    def show_menu(self):
        print("-----------ÁRVORE BINÁRIA-----------\n")
        print("1. Inserir valor")
        print("2. Mostrar árvore")
        print("3. Sair\n")

        self.option = input('Opção: ')
