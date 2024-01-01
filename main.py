'''
Desafio 24 - Voltando o quadrado através de função.

Requisitos:
- O usuário vai informa um número.
- Função

Saida:
- Retorna o valor o quadrado.

'''

#Entrada
numero = int(input('Digite um número: '))

#Função

def quadrado(numero):
    return numero * numero

#Saida
print(f'O quadrado de {numero} é {quadrado(numero)}.')

