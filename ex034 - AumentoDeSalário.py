#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário atual: R$'))

if salario <= 1250:

    salario2 = (salario * 1.15)
else:
    salario2 = (salario * 1.10)

print('Com o aumento, seu salário foi de R${:.2f} para R${:.2f}'.format(salario, salario2))
