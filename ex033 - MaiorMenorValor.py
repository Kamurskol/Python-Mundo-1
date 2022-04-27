#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

menor = a

if b<c and b<c:
    menor = b

if c<a and c<b:
    menor = c

maior = a

if b>a and b>c:
    menor = b

if c>b and c>a:
    maior = c

print('O menor valor digitado foi {} e o maior valor digitado foi {}'.format(menor, maior))
