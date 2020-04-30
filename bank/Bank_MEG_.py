import random
import time
import re
from validacao import Validacao
from conta import Conta
from cliente import Cliente
from visualizar_cliente import Visualizar_cliente
from menu import Menu
from opcao_digitada import Opcao_digitada
from menu_transferencia import Menu_transferencia
from transferencia import Transferencia
from pagar_boleto import Pagar_boleto

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



dados_cliente = None

def opcao_1():
    global dados_cliente
    global opcao
    print("INFORME NOME: ")
    nome = str(input())   
    while Validacao.validar_nome(nome) == False:
        print("ATENÇÃO!! É PERMITIDO APENAS LETRAS NO NOME, DIGITE NOVAMENTE")
        print("INFORME NOME: ")
        nome = str(input())
    else:
        print("INFORME CPF: ")
        cpf = str(input())
        retorno_cpf = Validacao.validar_cpf(cpf)
        
        while Validacao.validar_cpf(cpf) == False:
            print("ATENÇÃO!! CPF INVÁLIDO, DIGITE NOVAMENTE")
            print("INFORME CPF: ")
            cpf = str(input())
            retorno_cpf = Validacao.validar_cpf(cpf)
        else:
            print("INFORME SALDO: ")
            saldo = float(input())
            dados_cliente = Cliente(nome, cpf, saldo)
            dados_cliente = Conta.abrir_conta(dados_cliente)
            Menu.exibir_menu(dados_cliente)
            opcao = Opcao_digitada.opcao_digitada(opcao)
            
def opcao_2():
    global dados_cliente
    global opcao
    Visualizar_cliente.visulizar_dados_cliente(dados_cliente)
    print("PRESSIONE ENTER PARA CONTINUAR...")
    enter = str(input())
    Menu.exibir_menu(dados_cliente)
    opcao = Opcao_digitada.opcao_digitada(opcao)
  
def opcao_4():
    global saldo
    global num_boleto
    global cedente
    global valor_transacao
    global descricao_extrato
    global opcao
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
        Menu.exibir_menu(dados_cliente)
        opcao = Opcao_digitada.opcao_digitada(opcao)
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
        Menu.exibir_menu(dados_cliente)
        opcao = Opcao_digitada.opcao_digitada(opcao)

def opcao_5():
    global extrato
    global opcao
    if  extrato:
        print (*extrato, sep= "\n")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        Menu.exibir_menu(dados_cliente)
        opcao = Opcao_digitada.opcao_digitada(opcao)
    else:
        print("NENHUM ITEM PARA SER EXIBIDO")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        Menu.exibir_menu(dados_cliente)
        opcao = Opcao_digitada.opcao_digitada(opcao)

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
                Opcao_digitada.opcao_digitada(opcao)
        elif opcao == 2:
            contratos_ativos()
            opcao_6_submenu_simular()
            opcao = Opcao_digitada.opcao_digitada(opcao)
        else:
            print("OPCAO INVALIDA")
            opcao_6_submenu_simular()
            Opcao_digitada.opcao_digitada(opcao)
    else:
        Menu.exibir_menu(dados_cliente)
        opcao = Opcao_digitada.opcao_digitada(opcao)
        
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
    opcao = Opcao_digitada.opcao_digitada(opcao)
    while opcao != 0:
        while opcao != 1 and opcao != 2 and opcao != 0:
            print("OPÇÃO NÃO EXISTE")
            validar_opcao_simular()
            opcao = Opcao_digitada.opcao_digitada(opcao) 
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

Menu.exibir_menu(dados_cliente)
opcao = Opcao_digitada.opcao_digitada(opcao)

while opcao != 0:
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 0:
        print("OPÇÃO NÃO EXISTE")
        Menu.exibir_menu(dados_cliente)
        opcao = Opcao_digitada.opcao_digitada(opcao)

    if opcao == 1:        
        if conta_aberta == False:
            opcao_1()
        else:
            print("CONTA JÁ CRIADA")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            Menu.exibir_menu(dados_cliente)
            opcao = Opcao_digitada.opcao_digitada(opcao)

    if dados_cliente != None:
        if opcao == 2:
            opcao_2()
        elif opcao == 3:
            Menu_transferencia.opcao_3_submenu()
            opcao = Opcao_digitada.opcao_digitada(opcao)
            while opcao != 0:
                while opcao != 1 and opcao != 2 and opcao != 0:
                    print("OPÇÃO NÃO EXISTE")
                    Menu_transferencia.opcao_3_submenu()
                    opcao = Opcao_digitada.opcao_digitada(opcao) 
                if opcao == 1:
                    Transferencia.opcao_3_submenu_opcao_1(dados_cliente)
                    opcao = Opcao_digitada.opcao_digitada(opcao)
                else:
                    Transferencia.opcao_3_submenu_opcao_2(dados_cliente)
                    opcao = Opcao_digitada.opcao_digitada(opcao)
            else:
                Menu.exibir_menu(dados_cliente)
                opcao = Opcao_digitada.opcao_digitada(opcao)                                 
        elif opcao == 4:
            Pagar_boleto.pagar_boleto(dados_cliente)
            opcao = Opcao_digitada.opcao_digitada(opcao)
        elif opcao == 5:
            opcao_5()
        elif opcao == 6:
            opcao_6_submenu_simular()
            opcao = Opcao_digitada.opcao_digitada(opcao)
            validar_opcao_simular()
    else:
        print("CONTA AINDA NÃO FOI ABERTA")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        Menu.exibir_menu(dados_cliente)
        opcao = Opcao_digitada.opcao_digitada(opcao)
else:
    quit