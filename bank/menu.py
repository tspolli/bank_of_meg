class Menu:
    def exibir_menu(dados_cliente):
        if dados_cliente != None:
            print("-------------------------")
            print("BEM VINDO AO BANK OF MEG ")
            print("-------------------------")
            print("SELECIONE UMA DAS OPÇÕES: ")
            print("-------------------------")
            print("2 - VISUALIZAR MEUS DADOS")
            print("3 - TRANSFERÊNCIA")
            print("4 - PAGAMENTO")
            print("5 - VISUALIZAR EXTRATO")
            print("6 - EMPRESTIMO PESSOAL")
            print("0 - SAIR")
            print("-------------------------")
            print("OPÇÃO: ")
        else:
            print("-------------------------")
            print("BEM VINDO AO BANK OF MEG ")
            print("-------------------------")
            print("SELECIONE UMA DAS OPÇÕES: ")
            print("-------------------------")
            print("1 - ABRIR CONTA")
            print("0 - SAIR")
            print("-------------------------")
            print("OPÇÃO: ") 

    def opcao_3_submenu():
        print("-------------------------")
        print("SELECIONE UMA DAS OPÇÕES: ")
        print("-------------------------")
        print("1 - TRANSFERENCIA PARA CONTA BANK OF MEG")
        print("2 - TRANSFERENCIA ENTRE BANCOS")
        print("0 - VOLTAR")
        print("-------------------------")
        print("OPÇÃO: ")

    def opcao_6_submenu_simular(contrato_ativo):
        if contrato_ativo == True:
            print("-------------------------")
            print("SELECIONE UMA DAS OPÇÕES: ")
            print("-------------------------")
            print("1 - SIMULAR")
            print("2 - CONTRATOS ATIVOS")
            print("0 - VOLTAR")
            print("-------------------------")
            print("OPÇÃO: ")
        else:
            print("-------------------------")
            print("SELECIONE UMA DAS OPÇÕES: ")
            print("-------------------------")
            print("1 - SIMULAR")
            print("0 - VOLTAR")
            print("-------------------------")
            print("OPÇÃO: ")

    def opcao_6_submenu_efetivar():
        print("-------------------------")
        print("SELECIONE UMA DAS OPÇÕES: ")
        print("-------------------------")
        print("1 - EFETIVAR EMPRESTIMO")
        print("2 - SIMULAR NOVAMENTE")
        print("0 - VOLTAR")
        print("-------------------------")
        print("OPÇÃO: ")

    def opcao_digitada():
        opcao = int(input())
        return opcao