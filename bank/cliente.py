import random

class Cliente:
    def __init__(self, nome, cpf, saldo):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.agencia = "0001"
        self.conta = random.randrange (1,99999)
        self.digito = random.randrange (1,9)
        self.conta_aberta = False
        self.valor_limite_disponivel = 0
