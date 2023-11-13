#Crie um programa que leia quantos reais uma pessoa tem na carteira e quantas outras moedas essa pessoa pode comprar
#Considere 1 dólar = R$ 5,00 (27/04/2022)
#1 dólar = 4,90 (13/11/2023)
#Considere 1 euro = R$ 5,24(13/11/2022)
#Considere 1 libra = R$ 6,00 (13/11/2022)


real = float(input('Quanto dinheiro você tem na carteira? R$ '))

dolar = real/4.90
euro = real/5.24
libra = real/6.00

print('Com {:.2f}R$ você pode comprar:\n US${:.2f}\n €{:.2f}\n £{:.2f}.'.format(real, dolar, euro, libra))
