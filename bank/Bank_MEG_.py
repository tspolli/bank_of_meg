import random
nome = str()
cpf = int() 
saldo = float()
agencia = "0001"
conta = random.randrange(1,9999)
digito = random.randrange(1,9)
var_global_conta = 9999
enter = str()
agencia_destino = int()
conta_destino = int()
digito_destino = int()
valor_transferido = float()

print("-------------------------")
print("BEM VINDO AO BANK OF MEG ")
print("-------------------------")
print("SELECIONE UMA DAS OPÇÕES: ")
print("-------------------------")
print("1 - ABRIR CONTA")
print("2 - VISUALIZAR MEUS DADOS")
print("3 - TRANSFERÊNCIA")
print("4 - PAGAMENTO")
print("5 - VISUALIZAR EXTRATO")
print("0 - SAIR")
print("-------------------------")
print("OPÇÃO: ")

opcao = int(input())

while opcao != 0:
    if opcao == 1:
        print("OPÇÃO SELECIONADA: 1")
        print("INFORME NOME: ")
        nome = str(input())
        print("INFORME CPF: ")
        cpf = int(input())
        print("INFORME SALDO: ")
        saldo = float(input())
        print("-------------------------")
        print("BEM VINDO AO BANK OF MEG: ")
        print("-------------------------")
        print("SELECIONE UMA DAS OPÇÕES: ")
        print("-------------------------")
        print("1 - ABRIR CONTA")
        print("2 - VISUALIZAR MEUS DADOS")
        print("3 - TRANSFERÊNCIA")
        print("4 - PAGAMENTO")
        print("5 - VISUALIZAR EXTRATO")
        print("0 - SAIR")
        print("-------------------------")
        print("OPÇÃO: ")
        opcao = int(input())
    
    if opcao == 2:
        print("OPÇÃO SELECIONADA: 2")
        print("AGENCIA: ", agencia)
        print("CONTA: ", conta)
        print("DIGITO: ", digito)
        print("NOME: ", nome)
        print("CPF: ", cpf)
        print("SALDO: ", saldo)
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        print("-------------------------")
        print("BEM VINDO AO BANK OF MEG: ")
        print("-------------------------")
        print("SELECIONE UMA DAS OPÇÕES: ")
        print("-------------------------")
        print("1 - ABRIR CONTA")
        print("2 - VISUALIZAR MEUS DADOS")
        print("3 - TRANSFERÊNCIA")
        print("4 - PAGAMENTO")
        print("5 - VISUALIZAR EXTRATO")
        print("0 - SAIR")
        print("-------------------------")
        print("OPÇÃO: ")
        opcao = int(input())
         
    if opcao == 3:
        print("OPÇÃO SELECIONADA: 3")
        print("ENTRE COM AS INFORMAÇÕES DA CONTA DESTINO")
        print("AGENCIA: ")
        agencia_destino = int(input())
        print("CONTA: ")
        conta_destino = int(input())
        print("DIGITO: ")
        digito_destino = int(input())
        print("VALOR: ")
        valor_transferido = float(input())

        if valor_transferido > saldo:
            print("SALDO INSUFICIENTE")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            print("-------------------------")
            print("BEM VINDO AO BANK OF MEG: ")
            print("-------------------------")
            print("SELECIONE UMA DAS OPÇÕES: ")
            print("-------------------------")
            print("1 - ABRIR CONTA")
            print("2 - VISUALIZAR MEUS DADOS")
            print("3 - TRANSFERÊNCIA")
            print("4 - PAGAMENTO")
            print("5 - VISUALIZAR EXTRATO")
            print("0 - SAIR")
            print("-------------------------")
            print("OPÇÃO: ")
            opcao = int(input())
        else:
            print("TRANSFERÊNCIA REALIZADA COM SUCESSO")
            saldo = saldo - valor_transferido
            print("SALDO ATUAL:", saldo)
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            print("-------------------------")
            print("BEM VINDO AO BANK OF MEG: ")
            print("-------------------------")
            print("SELECIONE UMA DAS OPÇÕES: ")
            print("-------------------------")
            print("1 - ABRIR CONTA")
            print("2 - VISUALIZAR MEUS DADOS")
            print("3 - TRANSFERÊNCIA")
            print("4 - PAGAMENTO")
            print("5 - VISUALIZAR EXTRATO")
            print("0 - SAIR")
            print("-------------------------")
            print("OPÇÃO: ")
            opcao = int(input())

    elif opcao == 4 or opcao == 5:
        print("OPÇÃO AINDA NÃO LIBERADA PARA OS CLIENTES")
        print("-------------------------")
        print("BEM VINDO AO BANK OF MEG: ")
        print("-------------------------")
        print("SELECIONE UMA DAS OPÇÕES: ")
        print("-------------------------")
        print("1 - ABRIR CONTA")
        print("2 - VISUALIZAR MEUS DADOS")
        print("3 - TRANSFERÊNCIA")
        print("4 - PAGAMENTO")
        print("5 - VISUALIZAR EXTRATO")
        print("0 - SAIR")
        print("-------------------------")
        print("OPÇÃO: ")

        opcao = int(input())

    else:
        print("OPÇÃO NÃO EXISTE")
        print("-------------------------")
        print("BEM VINDO AO BANK OF MEG: ")
        print("-------------------------")
        print("SELECIONE UMA DAS OPÇÕES: ")
        print("-------------------------")
        print("1 - ABRIR CONTA")
        print("2 - VISUALIZAR MEUS DADOS")
        print("3 - TRANSFERÊNCIA")
        print("4 - PAGAMENTO")
        print("5 - VISUALIZAR EXTRATO")
        print("0 - SAIR")
        print("-------------------------")
        print("OPÇÃO: ")

        opcao = int(input())
else:
    quit