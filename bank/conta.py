from cliente import Cliente
import random

class Conta:
    def abrir_conta(amarelo):
        taxa_limite_disponivel = float(random.uniform(0.75,1.75))
        amarelo.valor_limite_disponivel = amarelo.saldo * taxa_limite_disponivel
        amarelo.conta_aberta = True
        return amarelo

        