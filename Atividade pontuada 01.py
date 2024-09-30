#Exec01:

#Entrada de dados:

a = float(input('Digite o valor A:'))
b = float(input('Digite o valor B:'))
c = float(input('Digite o valor C:'))

#processamento de Dados

#Triângulo Retângulo:
tr = (a*c)/2

#Raio:
pi = 3.14159
cr = pi * c**2

#trapézio:
tp = (a + b) * c/2

#Quadrado:
qr = b**2

#Retângulo:
rt = a * b

#Saída de Dados:

print(f'Triângulo: {tr}')
print(f'Círculo: {cr:.2f}')
print(f'Trapézio: {tp}')
print(f'Quadrado: {qr}')
print(f'Retângulo: {rt}')

#Exec02:

#Entrada de Dados:

nome = str(input('Nome do Funcionário: '))
salario = float(input('Salário Base: '))
vendas = float(input('Total de Vendas Mensais: '))

#Processamento de Dados:

pctg = vendas * 15/ 100
tf = salario + pctg

#Saída:

print(f'O total que {nome} vai receber no final de mês é: {tf}')

#Exec03:

#Entrada de Dados:

segds = int(input('Digite o tempo em segundos: '))

#Processamento de dados:

horas = segds//3600
minutos =  (segds % 3600)//60
segundos = segds%60

#Saída:

print(f'O tempo de {segds} convertido é: {horas}:{minutos}:{segundos}')
