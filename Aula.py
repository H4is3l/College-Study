import math

a= float(input('Insira um Valor a: '))
b=float(input('Insira um Valor b: '))
c= float(input('Insira um Valor c: '))

delta= float((b**2)-(4*a)*c)

if (delta<0) or (a==0):
    print('Impossivel Calcular!')
    
else:
    x=float((-b+math.sqrt(delta))/(2*a))
    y=float((-b-math.sqrt(delta))/(2*a))
    
    print(f'As raizes desses números são: {x:.5f} e {y:.5f}')
    
#exec02

#exec03        

a=float(input('Valor de a:'))
b=float(input('Valor de b:'))
c=float(input('Valor de c:'))

