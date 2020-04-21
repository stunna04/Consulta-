import tkinter,time,os,winsound

class Maneger:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""

    def cadastro(self):


    def valor_do_bem_adquirido(self):
        pass


    def update(self):
        pass


    def get_list(self):
        pass

    def tipo_de_financiamento(self):
        pass

    def inserir_produto(self):
        pass

    def menu(self):
        os.system("cls")
        winsound.Beep(2000,60)
        print("-------------------------MENU-----------------------")
        time.sleep(0.10)
        print()

        print("1 :) Dados de Cadastro")
        time.sleep(0.10)


        print("2 :) Valor do Bem Adquirido")
        time.sleep(0.10)

        print("3 :) Update")
        time.sleep(0.10)

        print("4 :) Tipo de Financiamento")
        time.sleep(0.10)

        print("5 :) Inserir Produto")
        print()

        opcao = input("selecione uma opção :")
        if opcao =="1":
            self.add()

        elif opcao =="2":
             self.remove()

        elif opcao =="3":
             self.update()

        elif opcao =="4":
             self.get_list()

        elif opcao =="5":
             self.terminate()

        else:
            winsound.Beep(2500,100)
            print("ERROR, TENTA NOVAMENTE AS OPÇÕES 1-5")
            time.sleep(2)
            self.menu()

    def main(self):
        os.system("cls")
        self.menu()

contacs_manager = Maneger()
contacs_manager.main()


