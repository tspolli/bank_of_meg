import time
from menu import Menu

extrato = []

class Pagar_boleto:
    def pagar_boleto(dados_cliente):
        print("ENTRE COM AS INFORMAÇÕES DO PAGAMENTO")
        print("NUMERO DO BOLETO: ")
        num_boleto = int(input())
        print("CEDENTE: ")
        cedente = str(input())
        print("VALOR: ")
        valor_transacao = float(input())

        if valor_transacao > dados_cliente.saldo:
            print("SALDO INSUFICIENTE")
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            Menu.exibir_menu(dados_cliente)
            opcao = Opcao_digitada.opcao_digitada()
        else:
            print("PAGAMENTO REALIZADO COM SUCESSO")
            saldo = dados_cliente.saldo - valor_transacao
            data_transacao = time.strftime("%d/%m/%Y")
            sinal_transacao = "-"
            valor_transacao_str = str(valor_transacao)
            descricao_extrato = data_transacao + "|" + sinal_transacao + valor_transacao_str + "|" + "PAGAMENTO DE BOLETO, CEDENTE: " + cedente
            print("SALDO ATUAL:", "{0:.2f}".format(round(saldo,2)))
            print("PRESSIONE ENTER PARA CONTINUAR...")
            enter = str(input())
            return saldo, descricao_extrato