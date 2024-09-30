N = int(input("Forneça um valor inteiro: "))

if 1 < N < 1000:
    
    for i in range(1, N + 1):
        
        col1 = i
        col2 = i ** 2
        col3 = i ** 3
        
        print(f"{col1} {col2} {col3}")
else:
    print("O valor de N deve ser maior que 1 e menor que 1000.")