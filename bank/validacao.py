import re

class Validacao:

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

    def validar_nome(nome):
        nome = str(input())
        nome_sem_espaco = nome.replace(" ", "")
        return nome_sem_espaco.isalpha()