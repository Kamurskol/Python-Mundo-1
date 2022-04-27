#Crie um programa que mostre o dobro, o triplo e a raiz quadrada de um número

n1 = int(input('Digite um número: '))

dobro = n1+n1
triplo = n1*3
raiz = n1**(1/2)

print('O dobro desse número é: {}'.format(dobro))
print('O triplo é: {}'.format(triplo))
print('A raiz quadrada é: {:.2f}'.format(raiz))