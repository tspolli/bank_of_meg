class Extrato:
    def exibir_extrato(extrato):
        if  extrato:
            print (*extrato, sep= "\n")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
        else:
            print("NENHUM ITEM PARA SER EXIBIDO")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())

    def contratos_ativos(extrato):
        print("CONTRATOS ATIVOS")
        if  extrato:
            print (*extrato, sep= "\n")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
        else:
            print("NENHUM ITEM PARA SER EXIBIDO")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())