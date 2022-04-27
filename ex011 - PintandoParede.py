#Faça um programa que leia a largura e altura de uma parede em metros, caucule sua área e a quantidade necessária de tinta para pinta-lá
#Considere que um litro de tinta pinta uma área de 2 metros quadrados

larg = float(input('Qual é a largura da parede em metros? '))
alt = float(input('Qual é a altura da parede em metros? '))
area = larg * alt

tinta = area / 2


print('Sua parede possui a dimensão de {}x{} metros e {}m²'.format(larg, alt, area))

print('Você precisa de {:.2f} litros de tinta para pintar a sua parede'.format(tinta))