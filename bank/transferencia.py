import time
from validacao import Validacao
from menu import Menu

class Transferencia:
    def opcao_3_submenu_opcao_1(dados_cliente):
        print("ENTRE COM AS INFORMAÇÕES DA CONTA DESTINO")
        print("AGENCIA: ")
        agencia_destino = str(input())
        print("CONTA: ")
        conta_destino = int(input())
        print("DIGITO: ")
        digito_destino = int(input())
        print("VALOR: ")
        valor_transacao = float(input())

        while valor_transacao > dados_cliente.saldo:
            print("SALDO INSUFICIENTE")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            Menu.exibir_menu(dados_cliente)
            opcao = Opcao_digitada.opcao_digitada()
        else:
            print("TRANSFERÊNCIA REALIZADA COM SUCESSO")
            saldo = dados_cliente.saldo - valor_transacao
            data_transacao = time.strftime("%d/%m/%Y")
            sinal_transacao = "-"
            valor_transacao_str = str(valor_transacao)
            agencia_destino_str = str(agencia_destino)
            conta_destino_str = str(conta_destino)
            digito_destino_str = str(digito_destino)
            descricao_extrato = data_transacao + "|" + sinal_transacao + valor_transacao_str + "|" + "TRANSFERENCIA PARA AGENCIA: " + agencia_destino_str + ", CONTA: " + conta_destino_str + "-" + digito_destino_str  
            print("SALDO ATUAL:", "{0:.2f}".format(round(saldo,2)))
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            return saldo, descricao_extrato

    def opcao_3_submenu_opcao_2(dados_cliente):
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
        retorno_cpf = Validacao.validar_cpf(cpf_destino)
            
        while retorno_cpf == False:
            print("ATENÇÃO!! CPF INVÁLIDO, DIGITE NOVAMENTE")
            print("INFORME CPF: ")
            cpf_destino = str(input())
            retorno_cpf = Validacao.validar_cpf(cpf)
        else:
            print("VALOR: ")
            valor_transacao = float(input()) 
            if valor_transacao > dados_cliente.saldo:
                print("SALDO INSUFICIENTE")
                print("PRESSIONE ENTER PARA CONTINUAR...")
                enter = str(input())
                Menu.exibir_menu(dados_cliente)
                opcao = Opcao_digitada.opcao_digitada()
            else:
                print("TRANSFERÊNCIA REALIZADA COM SUCESSO")
                saldo = dados_cliente.saldo - valor_transacao
                data_transacao = time.strftime("%d/%m/%Y")
                sinal_transacao = "-"
                valor_transacao_str = str(valor_transacao)
                agencia_destino_str = str(agencia_destino)
                conta_destino_str = str(conta_destino)
                digito_destino_str = str(digito_destino)
                descricao_extrato = data_transacao + "|" + sinal_transacao + valor_transacao_str + "|" + "TRANSFERENCIA PARA AGENCIA: " + agencia_destino_str + ", CONTA: " + conta_destino_str + "-" + digito_destino_str  
                print("SALDO ATUAL:", "{0:.2f}".format(round(saldo,2)))
                print("PRESSIONE ENTER PARA CONTINUAR...")
                enter = str(input())
                return saldo, descricao_extrato