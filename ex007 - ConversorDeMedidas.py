#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

medida = float(input('Digite uma distância em metros: '))

dam = medida / 10
dm = medida * 10
cm = medida * 100
km = medida / 1000
mm = medida * 1000

print('A medida de {}m corresponde a\n {}mm\n {}cm\n {}dm\n {}dam\n {}km. '.format(medida, mm, cm, dm, dam, km))