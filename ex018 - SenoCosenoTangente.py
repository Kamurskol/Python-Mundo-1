#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite o angulo que você deseja '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))


print('O ângulo de {} tem:\n SENO de {:.2}\n COSSENO de {:.2f}\n TANGENTE de {:.2f}'.format(angulo, seno, cosseno, tangente))
