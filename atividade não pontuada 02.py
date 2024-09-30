#Exec01:

#Entrada de Dados:

qnt = float(input('Insira uma quantidade em dinheiro: '))

ptin = int(qnt)
cents = int((ptin - qnt) * 100)

#Processamento/Saída:

print('Notas')

nt_100 = ptin // 100
print(f'notas de 100 necessárias: {nt_100}')
ptin = ptin % 100

nt_50 = ptin // 50
print(f'notas de 50 necessárias: {nt_50}')
ptin = ptin % 50

nt_20 = ptin // 20
print(f'notas de 20 necessárias: {nt_20}')
ptin = ptin % 20

nt_10 = ptin // 10
print(f'notas de 10 necessárias: {nt_10}')
ptin = ptin % 10

nt_5 = ptin // 5
print(f'notas de 5 necessárias: {nt_5}')
ptin = ptin % 5

nt_2 = ptin // 2
print(f'notas de 2 necessárias: {nt_2}')
ptin = ptin % 2

print('Centavos')

md_1 = ptin
print(f'moedas de 1 necessárias: {md_1}')

md_50 = cents // 50
print(f'Moedas de 0.50 necessárias: {md_50}')
cents = cents % 50

md_25 = cents // 25
print(f'Moedas de 0.25 necessárias: {md_25}')
cents = cents % 25

md_10 = cents // 10
print(f'Moedas de 0.50 necessárias: {md_10}')
cents = cents % 10

md_5 = cents // 5
print(f'Moedas de 0.5 necessárias: {md_5}')
cents = cents % 5

md_1 = cents
print(f'Moedas de 0.1 necessárias: {md_1}')

#Exec02:

#Entrada de Dados:

x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))

#Processamento/Saída:

if x==0 and y==0:
    print('Origem')

elif x == 0:
    print('Eixo Y')

elif y == 0:
    print('Eixo X')

elif x > 0 and y > 0:
    print('1º Quadrante')  

elif x < 0 and y > 0:
    print('2º Quadrante')

elif x < 0 and y < 0:
    print('3º Quadrante')

elif x > 0 and y < 0:
    print('4º Quadrante')

#Exec03:

#Entrada de Dados:

n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite um valor inteiro: '))
n3 = int(input('Digite um valor inteiro: '))
n4 = int(input('Digite um valor inteiro: '))
n5 = int(input('Digite um valor inteiro: '))

#Processamento:

cont = 0

if n1%2==0:
    cont = +1
if n2%2==0:
    cont = +1
if n3%2==0:
    cont = +1
if n4%2==0:
    cont = +1
if n5%2==0:
    cont = +1

#Saída:

print(f'A quantidade de números pares é: {cont}')
