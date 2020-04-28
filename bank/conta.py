from cliente import Cliente
import random

class Conta:
    def abrir_conta(nome, cpf, valor):
        taxa_limite_disponivel = float(random.uniform(0.75,1.75))
        valor_limite_disponivel = saldo * taxa_limite_disponivel 
        cliente = Cliente(nome, cpf, valor, valor_limite_disponivel)
        return cliente

        