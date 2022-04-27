#Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço = float(input('Digite o valor inicial: R$'))

desconto = preço*0.95

print('O valor R${:.2f} com desconto de 5% fica R${:.2f}'.format(preço, desconto))