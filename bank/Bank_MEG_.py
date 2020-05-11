import random
import time
import re
from validacao import Validacao
from conta import Conta
from cliente import Cliente
from visualizar_cliente import Visualizar_cliente
from menu import Menu
from transferencia import Transferencia
from pagar_boleto import Pagar_boleto
from exibir_extrato import Extrato
from emprestimo import Emprestimo

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
            dados_cliente = Cliente(nome, cpf, saldo, valor_limite_disponivel)
            dados_cliente = Conta.abrir_conta(dados_cliente)
            Menu.exibir_menu(dados_cliente)
            opcao = Menu.opcao_digitada()
            
def opcao_2():
    global dados_cliente
    global opcao
    Visualizar_cliente.visulizar_dados_cliente(dados_cliente)
    print("PRESSIONE ENTER PARA CONTINUAR...")
    enter = str(input())
    Menu.exibir_menu(dados_cliente)
    opcao = Menu.opcao_digitada()


Menu.exibir_menu(dados_cliente)
opcao = Menu.opcao_digitada()

while opcao != 0:
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 0:
        print("OPÇÃO NÃO EXISTE")
        Menu.exibir_menu(dados_cliente)
        opcao = Menu.opcao_digitada()

    if opcao == 1:        
        if conta_aberta == False:
            opcao_1()
        else:
            print("CONTA JÁ CRIADA")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            Menu.exibir_menu(dados_cliente)
            opcao = Menu.opcao_digitada()

    if dados_cliente != None:
        if opcao == 2:
            opcao_2()
        elif opcao == 3:
            Menu.opcao_3_submenu()
            opcao = Menu.opcao_digitada()
            while opcao != 0:
                while opcao != 1 and opcao != 2 and opcao != 0:
                    print("OPÇÃO NÃO EXISTE")
                    Menu.opcao_3_submenu()
                    opcao = Menu.opcao_digitada() 
                if opcao == 1:
                    a = Transferencia.opcao_3_submenu_opcao_1(dados_cliente)
                    dados_cliente.saldo = a[0]
                    extrato.append(a[1])
                    Menu.opcao_3_submenu()
                    opcao = Menu.opcao_digitada()
                else:
                    a = Transferencia.opcao_3_submenu_opcao_2(dados_cliente)
                    dados_cliente.saldo = a[0]
                    extrato.append(a[1])
                    Menu.opcao_3_submenu()
                    opcao = Menu.opcao_digitada()
            else:
                Menu.exibir_menu(dados_cliente)
                opcao = Menu.opcao_digitada()                                 
        elif opcao == 4:
            a = Pagar_boleto.pagar_boleto(dados_cliente)
            dados_cliente.saldo = a[0]
            extrato.append(a[1])            
            Menu.exibir_menu(dados_cliente)
            opcao = Menu.opcao_digitada()
        elif opcao == 5:
            Extrato.exibir_extrato(extrato)
            Menu.exibir_menu(dados_cliente)
            opcao = Menu.opcao_digitada()
        elif opcao == 6:
            Menu.opcao_6_submenu_simular(dados_cliente)
            opcao = Menu.opcao_digitada()
            a = Emprestimo.validar_opcao_simular(opcao, dados_cliente, taxa_juros)
    else:
        print("CONTA AINDA NÃO FOI ABERTA")
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        Menu.exibir_menu(dados_cliente)
        opcao = Menu.opcao_digitada()
else:
    quit