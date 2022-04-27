#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = int(input('Qual será a distância da viagem? '))

if dist <= 200:
    preço = (dist * 0.50)
else:
    preço = (dist * 0.45)

print('O valor da viagem será de R${:.2f}'.format(preço))
