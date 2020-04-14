import random
import time
import re

opcao = int()
nome = str()
cpf = str() 
saldo = float()
agencia = "0001"
conta = random.randrange (1,9999)
digito = random.randrange (1,9)
enter = str()
agencia_destino = str()
conta_destino = int()
digito_destino = int()
valor_transacao = float()
num_boleto = int()
cedente = str()
data_transacao = str()
sinal_transacao = str()
extrato = []
conta_aberta = bool()
descricao_extrato = str()
conta_digito = str()

def validar_cpf(cpf):
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf) and not re.match(r'\d{3}\d{3}\d{3}\d{2}', cpf) and not re.match(r'\d{3}\d{3}\d{3}-\d{2}', cpf):
        return False

    numeros_inteiros_cpf = [int(digit) for digit in cpf if digit.isdigit()]
    
    if len(numeros_inteiros_cpf) != 11:
        return False

    soma_produtos = sum(a*b for a, b in zip(numeros_inteiros_cpf[0:9], range(10, 1, -1)))
    digito_esperado = (soma_produtos * 10) % 11
    
    if numeros_inteiros_cpf[9] != digito_esperado:
        return False
    
    soma_produtos = sum(a*b for a, b in zip(numeros_inteiros_cpf[0:10], range(11, 1, -1)))
    digito_esperado = (soma_produtos * 10) % 11
    
    if numeros_inteiros_cpf[10] != digito_esperado:
        return False

    return True

def exibir_menu():
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

def opcao_digitada():
    global opcao
    opcao = int(input())
    return opcao

def opcao_1():
    global nome
    global cpf
    global saldo
    global conta_aberta
    print("OPÇÃO SELECIONADA: 1")
    print("INFORME NOME: ")
    nome = str(input())

    while nome.isalpha() == False:
        print("ATENÇÃO!! É PERMITIDO APENAS LETRAS NO NOME, DIGITE NOVAMENTE")
        print("INFORME NOME: ")
        nome = str(input())
    else:
        print("INFORME CPF: ")
        cpf = str(input())
        retorno_cpf = validar_cpf(cpf)
        
        while retorno_cpf == False:
            print("ATENÇÃO!! CPF INVÁLIDO, DIGITE NOVAMENTE")
            print("INFORME CPF: ")
            cpf = str(input())
            retorno_cpf = validar_cpf(cpf)
        else:
            print("INFORME SALDO: ")
            saldo = float(input())
            conta_aberta = True
            exibir_menu()
            opcao = opcao_digitada()
            
def opcao_2():
    global agencia
    global conta_str
    global digito_str
    global conta_digito
    print("OPÇÃO SELECIONADA: 2")
    print("AGENCIA: ", agencia)
    conta_str = str(conta)
    digito_str = str(digito)
    conta_digito = "CONTA: " + conta_str + "-" + digito_str
    print(conta_digito)
    print("NOME: ", nome)
    print("CPF: ", cpf)
    print("SALDO: ", "{0:.2f}".format(round(saldo,2)))
    print("PRESSIONE ENTER PARA CONTINUAR...")
    enter = str(input())
    exibir_menu()
    opcao = opcao_digitada()

def opcao_3():
    global agencia_destino
    global conta_destino
    global digito_destino
    global saldo
    global valor_transacao
    global descricao_extrato
    print("OPÇÃO SELECIONADA: 3")
    print("ENTRE COM AS INFORMAÇÕES DA CONTA DESTINO")
    print("AGENCIA: ")
    agencia_destino = str(input())
    print("CONTA: ")
    conta_destino = int(input())
    print("DIGITO: ")
    digito_destino = int(input())
    print("VALOR: ")
    valor_transacao = float(input())

    if valor_transacao > saldo:
        print("SALDO INSUFICIENTE")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        exibir_menu()
        opcao = opcao_digitada()
    else:
        print("TRANSFERÊNCIA REALIZADA COM SUCESSO")
        saldo = saldo - valor_transacao
        data_transacao = time.strftime("%d/%m/%Y")
        sinal_transacao = "-"
        valor_transacao_str = str(valor_transacao)
        agencia_destino_str = str(agencia_destino)
        conta_destino_str = str(conta_destino)
        digito_destino_str = str(digito_destino)
        descricao_extrato = data_transacao + "|" + sinal_transacao + valor_transacao_str + "|" + "TRANSFERENCIA PARA AGENCIA: " + agencia_destino_str + ", CONTA: " + conta_destino_str + "-" + digito_destino_str  
        extrato.append(descricao_extrato)
        print("SALDO ATUAL:", "{0:.2f}".format(round(saldo,2)))
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        exibir_menu()
        opcao = opcao_digitada()

def opcao_4():
    global saldo
    global num_boleto
    global cedente
    global valor_transacao
    global descricao_extrato
    print("OPÇÃO SELECIONADA: 4")
    print("ENTRE COM AS INFORMAÇÕES DO PAGAMENTO")
    print("NUMERO DO BOLETO: ")
    num_boleto = int(input())
    print("CEDENTE: ")
    cedente = str(input())
    print("VALOR: ")
    valor_transacao = float(input())

    if valor_transacao > saldo:
        print("SALDO INSUFICIENTE")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        exibir_menu()
        opcao = opcao_digitada()
    else:
        print("PAGAMENTO REALIZADO COM SUCESSO")
        saldo = saldo - valor_transacao
        data_transacao = time.strftime("%d/%m/%Y")
        sinal_transacao = "-"
        valor_transacao_str = str(valor_transacao)
        descricao_extrato = data_transacao + "|" + sinal_transacao + valor_transacao_str + "|" + "PAGAMENTO DE BOLETO, CEDENTE: " + cedente
        extrato.append(descricao_extrato)
        print("SALDO ATUAL:", "{0:.2f}".format(round(saldo,2)))
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        exibir_menu()
        opcao = opcao_digitada()

def opcao_5():
    global extrato
    if  extrato:
        print("OPÇÃO SELECIONADA: 5")
        print (*extrato, sep= "\n")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        exibir_menu()
        opcao = opcao_digitada()
    else:
        print("NENHUM ITEM PARA SER EXIBIDO")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        exibir_menu()
        opcao = opcao_digitada()

exibir_menu()
opcao = opcao_digitada()

while opcao != 0:
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 0:
        print("OPÇÃO NÃO EXISTE")
        exibir_menu()
        opcao = opcao_digitada()

    if opcao == 1:        
        if conta_aberta == False:
            opcao_1()
        else:
            print("CONTA JÁ CRIADA")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            exibir_menu()
            opcao = opcao_digitada()

    if conta_aberta == True:
        if opcao == 2:
            opcao_2()
        elif opcao == 3:
            opcao_3()    
        elif opcao == 4:
            opcao_4()
        elif opcao == 5:
            opcao_5()
    else:
        print("CONTA AINDA NÃO FOI ABERTA")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        exibir_menu()
        opcao = opcao_digitada()
else:
    quit