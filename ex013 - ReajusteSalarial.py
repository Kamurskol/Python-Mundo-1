#Desenvolva um agorítmo que leia o salário de um funcionátrio e mostre o seu novo salário, com 15% de aumento

salario = float(input('Qual é o salário do funcionário? R$'))

reajuste = salario + (salario * 15 / 100)


print('Um funcionário que ganhava R${:.2f}, com o reajuste passa a ganhar R${:.2f}'.format(salario, reajuste))
