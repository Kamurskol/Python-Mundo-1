#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=-' * 21)

print('Estou pensando em um número entre 0 e 5. Tente adivinhar...')

print('-=-' * 21)
computador = randint(0, 5) #FAZ O COMPUTADOR ESCOLHER UM NÚMERO RANDOMICAMENTE

player = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(0.5) # Cria um timer

if player == computador:
    print('Acertou.')
else:
    print('Ganhei! Eu pensei no número {}'.format(computador))
