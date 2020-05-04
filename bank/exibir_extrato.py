from menu import Menu
from transferencia import Transferencia
from visualizar_cliente import Visualizar_cliente
from cliente import Cliente


class Extrato:
    def exibir_extrato(extrato):
        if  Transferencia.extrato:
            print (*extrato, sep= "\n")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            Menu.exibir_menu(dados_cliente)
        else:
            print("NENHUM ITEM PARA SER EXIBIDO")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            Menu.exibir_menu(dados_cliente)