import time
from menu import Menu
from exibir_extrato import Extrato

extrato = []

class Emprestimo:
    def validar_opcao_simular(opcao, dados_cliente, taxa_juros):
        while opcao != 0:
            if opcao == 1:                
                valor_transacao = Emprestimo.simular_emprestimo(dados_cliente, taxa_juros)
                opcao = Emprestimo.simular_emprestimo_efetivar(dados_cliente, valor_transacao)
                if opcao != 1:
                    a = Menu.opcao_6_submenu_simular(dados_cliente.contrato_ativo)
                    opcao = Menu.opcao_digitada()
            elif opcao == 2:
                Extrato.contratos_ativos(extrato)
                Menu.opcao_6_submenu_simular(dados_cliente.contrato_ativo)
                opcao = Menu.opcao_digitada()
            else:
                print("OPCAO INVALIDA")
                Menu.opcao_6_submenu_simular(dados_cliente.contrato_ativo)
                Menu.opcao_digitada()
        else:
            Menu.exibir_menu(dados_cliente)
            opcao = Menu.opcao_digitada()
            
    def simular_emprestimo_efetivar(dados_cliente, valor_transacao):
        Menu.opcao_6_submenu_efetivar()
        opcao = Menu.opcao_digitada()
        while opcao != 0:
            while opcao != 1 and opcao != 2 and opcao != 0:
                print("OPÇÃO NÃO EXISTE")
                Emprestimo.validar_opcao_simular()
                opcao = Menu.opcao_digitada() 
            if opcao == 1:
                a = Emprestimo.efetivar_emprestimo(dados_cliente, valor_transacao)
                dados_cliente.saldo = a[0]
                dados_cliente.valor_limite_disponivel = a[2].valor_limite_disponivel
                extrato.append(a[1])
                return 0
            elif opcao == 2:
                return 1
        else:
            Emprestimo.validar_opcao_simular()
            
    def simular_emprestimo(dados_cliente, taxa_juros):
        print("ENTRE COM AS INFORMAÇÕES PARA SIMULAR EMPRESTIMO")
        print("VALOR: ")
        valor_transacao = float(input())
        while valor_transacao > dados_cliente.valor_limite_disponivel:
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
                return valor_transacao

    def efetivar_emprestimo(dados_cliente, valor_transacao):
        saldo = dados_cliente.saldo + valor_transacao
        valor_limite_disponivel = dados_cliente.valor_limite_disponivel - valor_transacao
        data_transacao = time.strftime("%d/%m/%Y")
        dados_cliente.contrato_ativo = True
        dados_cliente.saldo = saldo
        dados_cliente.valor_limite_disponivel = valor_limite_disponivel
        sinal_transacao = "+"
        valor_transacao_str = str(valor_transacao)
        descricao_extrato = data_transacao + "|" + sinal_transacao + valor_transacao_str + "|" + "EMPRESTIMO CONTRATADO"
        print("SALDO ATUAL:", "{0:.2f}".format(round(saldo,2)))
        print("LIMITE DISPONIVEL: ", "{0:.2f}".format(round(valor_limite_disponivel,2)))
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        return saldo, descricao_extrato, dados_cliente
                    

