#Escreva um programa que converta uma temperatura digitada em °C e converta para °F
#Fórmula: ( °C × 9/5) + 32 = °F

c = int(input('Informe a temperatura em °C: '))

f = (c * 9/5) + 32

print('{}°C equivale a {}°F'.format(c, f))

