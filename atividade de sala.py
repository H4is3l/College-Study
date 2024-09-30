#Exec01:

nome = str(input('Qual seu nome? '))

print(f'Olá {nome}!')

#Exec02:

b = float(input('Quantos CM de distância no mapa?'))
c = float(input('Qual a Escala do mapa? '))
dist = float(b * c)

print(f'A distância entre esses dois pontos em KM é de: {dist:.2f}.')

#Exec03:

d = float(input('Quantos litros foram colocados?'))
d1= float(d*2)

print(f'O veículo possui a capacidade de {d1:.2f} litros de combustível.')
