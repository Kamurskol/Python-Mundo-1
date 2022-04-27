#Escreva um programa que pergunte a quantidade de Km percorridis por um carro alugado e e a quantidade de dias que ele foi alugado
#Caucule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

dias = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos Km foram percorridos com o carro? '))

valord = dias * 60
valorkm = km * 0.15

valortotal = valord + valorkm

print('O valor total a pagar é R${:.2f}'.format(valortotal))
