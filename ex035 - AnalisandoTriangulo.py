a = float(input('Informe o comprimento da primeira reta: '))

b = float(input('Informe o comprimento da segunda reta: '))

c = float(input('Informe o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < b + a:
    print('Os lados {}, {} e {} podem formar um triângulo.'.format(a, b, c))
else:
    print('Os lados {}, {} e {} não podem formar um triângulo.'.format(a, b, c))

