import random
import time
import re

opcao = int()
nome = str()
cpf = str()
digito_esperado = int()
saldo = float()
agencia = "0001"
conta = random.randrange (1,99999)
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
taxa_limite_disponivel = float(random.uniform(0.75,1.75))
valor_limite_disponivel = float()
quantidade_parcelas = int()
juros = float()
taxa_juros = 0.02
valor_emprestimo = float()
valor_parcela = float()
contrato_ativo = bool()

def validar_cpf(cpf):
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf) and not re.match(r'\d{3}\d{3}\d{3}\d{2}', cpf) and not re.match(r'\d{3}\d{3}\d{3}-\d{2}', cpf):
        return False

    numeros_inteiros_cpf = [int(digit) for digit in cpf if digit.isdigit()]
    
    if len(numeros_inteiros_cpf) != 11:
        return False

    soma_produtos = sum(a*b for a, b in zip(numeros_inteiros_cpf[0:9], range(10, 1, -1)))
    resto_esperado = soma_produtos % 11
    if resto_esperado < 2:
        digito_esperado = 0
    else:
        digito_esperado = 11 - resto_esperado 
        
    if numeros_inteiros_cpf[9] != digito_esperado:
        return False
    
    soma_produtos = sum(a*b for a, b in zip(numeros_inteiros_cpf[0:10], range(11, 1, -1)))
    resto_esperado = soma_produtos % 11
    if resto_esperado < 2:
        digito_esperado = 0
    else:
        digito_esperado = 11 - resto_esperado    
    
    if numeros_inteiros_cpf[10] != digito_esperado:
        return False

    return True

def exibir_menu():
    if conta_aberta == True:
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

def opcao_digitada():
    global opcao
    opcao = int(input())
    return opcao

def opcao_1():
    global nome
    global cpf
    global saldo
    global conta_aberta
    global valor_limite_disponivel
    global taxa_limite_disponivel
    print("INFORME NOME: ")
    nome = str(input())
    nome_sem_espaco = nome.replace(" ", "")
    
    while nome_sem_espaco.isalpha() == False:
        print("ATENÇÃO!! É PERMITIDO APENAS LETRAS NO NOME, DIGITE NOVAMENTE")
        print("INFORME NOME: ")
        nome = str(input())
        nome_sem_espaco = nome.replace(" ", "")
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
            valor_limite_disponivel = saldo * taxa_limite_disponivel  
            exibir_menu()
            opcao = opcao_digitada()
            
def opcao_2():
    global agencia
    global conta_str
    global digito_str
    global conta_digito
    print("AGENCIA: ", agencia)
    conta_str = str(conta)
    digito_str = str(digito)
    conta_digito = "CONTA: " + conta_str + "-" + digito_str
    print(conta_digito)
    print("NOME: ", nome)
    print("CPF: ", cpf)
    print("SALDO: ", "{0:.2f}".format(round(saldo,2)))
    print("LIMITE DISPONIVEL: ", "{0:.2f}".format(round(valor_limite_disponivel,2)))
    print("PRESSIONE ENTER PARA CONTINUAR...")
    enter = str(input())
    exibir_menu()
    opcao = opcao_digitada()

def opcao_3_submenu():
    print("-------------------------")
    print("SELECIONE UMA DAS OPÇÕES: ")
    print("-------------------------")
    print("1 - TRANSFERENCIA PARA CONTA BANK OF MEG")
    print("2 - TRANSFERENCIA ENTRE BANCOS")
    print("0 - VOLTAR")
    print("-------------------------")
    print("OPÇÃO: ")
    
def opcao_3_submenu_opcao_1():
    global agencia_destino
    global conta_destino
    global digito_destino
    global saldo
    global valor_transacao
    global descricao_extrato
    global opcao
    print("ENTRE COM AS INFORMAÇÕES DA CONTA DESTINO")
    print("AGENCIA: ")
    agencia_destino = str(input())
    print("CONTA: ")
    conta_destino = int(input())
    print("DIGITO: ")
    digito_destino = int(input())
    print("VALOR: ")
    valor_transacao = float(input())

    while valor_transacao > saldo:
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
        opcao = 3
        opcao_3_submenu()

def opcao_3_submenu_opcao_2():
    global codigo_banco_destino
    global agencia_destino
    global conta_destino
    global digito_destino
    global saldo
    global valor_transacao
    global descricao_extrato
    global cpf
    print("ENTRE COM AS INFORMAÇÕES DA CONTA DESTINO")
    print("CODIGO DO BANCO: ")
    codigo_banco_destino = str(input())
    print("AGENCIA: ")
    agencia_destino = str(input())
    print("CONTA: ")
    conta_destino = int(input())
    print("DIGITO: ")
    digito_destino = int(input())
    print("CPF: ")
    cpf_destino = str(input())
    retorno_cpf = validar_cpf(cpf_destino)
        
    while retorno_cpf == False:
        print("ATENÇÃO!! CPF INVÁLIDO, DIGITE NOVAMENTE")
        print("INFORME CPF: ")
        cpf_destino = str(input())
        retorno_cpf = validar_cpf(cpf)
    else:
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
            opcao = 3
            opcao_3_submenu()
    
def opcao_4():
    global saldo
    global num_boleto
    global cedente
    global valor_transacao
    global descricao_extrato
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

def opcao_6_submenu_simular():
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

def validar_opcao_simular():
    global opcao
    while opcao != 0:
        if opcao == 1:
            simular_emprestimo()
            opcao = simular_emprestimo_efetivar()
            if opcao != 1:
                opcao_6_submenu_simular()
                opcao = opcao_digitada()
        elif opcao == 2:
            contratos_ativos()
            opcao_6_submenu_simular()
            opcao = opcao_digitada()
        else:
            print("OPCAO INVALIDA")
            opcao_6_submenu_simular()
            opcao = opcao_digitada()
    else:
        exibir_menu()
        opcao = opcao_digitada()
        
def simular_emprestimo():
    global saldo
    global valor_transacao
    global quantidade_parcelas
    global descricao_extrato
    global juros
    global taxa_juros
    global valor_emprestimo
    global opcao
    print("ENTRE COM AS INFORMAÇÕES PARA SIMULAR EMPRESTIMO")
    print("VALOR: ")
    valor_transacao = float(input())
    while valor_transacao > valor_limite_disponivel:
        print("VALOR DO EMPRESTIMO NAO APROVADO")
        print("VALOR: ")
        valor_transacao = float(input())
    else:
        print("QUANTIDADE DE PARCELAS: ")
        quantidade_parcelas = int(input())
        while quantidade_parcelas < 1 or quantidade_parcelas > 36:
            print("A QUANTIDADE DE PARCELAS INFORMADA DEVE SER ENTRE 1 E 36 ")
            print("INFORME A QUANTIDADE DE PARCELAS: ")
            quantidade_parcelas = int(input())
        else:    
            print("SIMULACAO DO EMPRESTIMO")
            juros = valor_transacao * taxa_juros * quantidade_parcelas
            valor_emprestimo = valor_transacao + juros
            valor_parcela = valor_emprestimo / quantidade_parcelas
            print("VALOR EMPRESTIMO: ", "{0:.2f}".format(round(valor_emprestimo,2)))
            print("QUANTIDADE DE PARCELAS: ", quantidade_parcelas)
            print("VALOR PARCELA:", "{0:.2f}".format(round(valor_parcela,2)))

def opcao_6_submenu_efetivar():
    print("-------------------------")
    print("SELECIONE UMA DAS OPÇÕES: ")
    print("-------------------------")
    print("1 - EFETIVAR EMPRESTIMO")
    print("2 - SIMULAR NOVAMENTE")
    print("0 - VOLTAR")
    print("-------------------------")
    print("OPÇÃO: ")

def simular_emprestimo_efetivar():
    global opcao      
    opcao_6_submenu_efetivar()
    opcao = opcao_digitada()
    while opcao != 0:
        while opcao != 1 and opcao != 2 and opcao != 0:
            print("OPÇÃO NÃO EXISTE")
            validar_opcao_simular()
            opcao = opcao_digitada() 
        if opcao == 1:
            efetivar_emprestimo()
            return 0
        elif opcao == 2:
            return 1
    else:
        validar_opcao_simular()
                  
def contratos_ativos():
    global extrato
    print("CONTRATOS ATIVOS")
    if  extrato:
        print (*extrato, sep= "\n")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
    else:
        print("NENHUM ITEM PARA SER EXIBIDO")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())

def efetivar_emprestimo():
    global saldo
    global valor_limite_disponivel
    global data_transacao
    global sinal_transacao
    global valor_transacao
    global descricao_extrato
    global contrato_ativo
    saldo = saldo + valor_transacao
    valor_limite_disponivel = valor_limite_disponivel - valor_transacao
    data_transacao = time.strftime("%d/%m/%Y")
    contrato_ativo = True
    sinal_transacao = "+"
    valor_transacao_str = str(valor_transacao)
    descricao_extrato = data_transacao + "|" + sinal_transacao + valor_transacao_str + "|" + "EMPRESTIMO CONTRATADO"
    extrato.append(descricao_extrato)
    print("SALDO ATUAL:", "{0:.2f}".format(round(saldo,2)))
    print("LIMITE DISPONIVEL: ", "{0:.2f}".format(round(valor_limite_disponivel,2)))
    print("PRESSIONE ENTER PARA CONTINUAR...")
    enter = str(input())

exibir_menu()
opcao = opcao_digitada()

while opcao != 0:
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 0:
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
            opcao_3_submenu()
            opcao = opcao_digitada()
            while opcao != 0:
                while opcao != 1 and opcao != 2 and opcao != 0:
                    print("OPÇÃO NÃO EXISTE")
                    opcao_3_submenu()
                    opcao = opcao_digitada() 
                if opcao == 1:
                    opcao_3_submenu_opcao_1()
                    opcao = opcao_digitada()
                else:
                    opcao_3_submenu_opcao_2()
                    opcao = opcao_digitada()
            else:
                exibir_menu()
                opcao = opcao_digitada()                                  
        elif opcao == 4:
            opcao_4()
        elif opcao == 5:
            opcao_5()
        elif opcao == 6:
            opcao_6_submenu_simular()
            opcao = opcao_digitada()
            validar_opcao_simular()
    else:
        print("CONTA AINDA NÃO FOI ABERTA")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        exibir_menu()
        opcao = opcao_digitada()
else:
    quit