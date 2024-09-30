#Exec01:

#módulos:

import math

#Entrada de dados:

a = float(input('Digite o valor a: '))
b = float(input('Digite o valor b: '))
c = float(input('Digite o valor c: '))

#processamento de dados:

delta = b**2 - 4 * a * c


if a == 0:

    print('Impossivel de Calcular')

elif delta<0:
     
     print('Impossivel de Calcular')

else:

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    #Saída:

    print(f'As raízes são: {x1:.5f} e {x2:.5f}')
