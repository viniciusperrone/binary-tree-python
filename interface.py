

class Interface:

    def __init__(self):
        self.option = None

    def show_menu(self):
        print("\n-----------ÁRVORE BINÁRIA-----------\n")
        print("1. Inserir valor")
        print("2. Mostrar árvore")
        print("3. Pesquisar valor")
        print("4. Remover valor")
        print("5. Sair")


    def choose_option(self):
        self.option = int(input('\nOpção: '))

    def get_value(self) -> int:
        value = int(input('\nValor: '))

        return value 

