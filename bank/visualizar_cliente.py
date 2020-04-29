from cliente import Cliente
from conta import Conta

class Visualizar_cliente:
    def visulizar_dados_cliente(dados_cliente):
        dados_cliente = Cliente(nome, cpf, saldo)
        dados_cliente = Conta.abrir_conta(dados_cliente)
        print("AGENCIA: ", dados_cliente.agencia)
        conta_str = str(dados_cliente.conta)
        digito_str = str(dados_cliente.digito)
        conta_digito = "CONTA: " + conta_str + "-" + digito_str
        print(conta_digito)
        print("NOME: ", dados_cliente.nome)
        print("CPF: ", dados_cliente.cpf)
        print("SALDO: ", "{0:.2f}".format(round(dados_cliente.saldo,2)))
        print("LIMITE DISPONIVEL: ", "{0:.2f}".format(round(dados_cliente.valor_limite_disponivel,2)))
        return dados_cliente
        print("PRESSIONE ENTER PARA CONTINUAR...")
        enter = str(input())
        