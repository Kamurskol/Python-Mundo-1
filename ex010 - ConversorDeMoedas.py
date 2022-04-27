#Crie um programa que leia quantos reais uma pessoa tem na carteira e quantas outras moedas essa pessoa pode comprar
#Considere 1 dólar = R$ 5,02 (21/03/2022)
#Considere 1 euro = R$ 5,54(21/03/2022)
#Considere 1 libra = R$ 6,60 (21/03/2022)


real = float(input('Quanto dinheiro você tem na carteira? R$ '))

dolar = real/5.02
euro = real/5.54
libra = real/6.60

print('Com {:.2f}R$ você pode comprar:\n US${:.2f}\n €{:.2f}\n £{:.2f}.'.format(real, dolar, euro, libra))
