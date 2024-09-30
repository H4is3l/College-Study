#Kauan Silva Santos 

from itertools import permutations, combinations

# Entrada dos créditos:
c1 = int(input("Forneca o valor do credito 1: "))
c2 = int(input("Forneca o valor do credito 2: "))
c3 = int(input("Forneca o valor do credito 3: "))

def pode_voltar_ao_presente(c1, c2, c3):
    creditos = [c1, c2, c3]
    
    # Gerando combinações de crédito:
    for i in range(1, 4):
        for comb in combinations(creditos, i):
           
            for perm in permutations(comb):
                
                if sum(perm) == 0:
                    return "Sim"
               
                if sum(perm[::2]) -sum(perm[1::2]) == 0:
                    return "Sim"
    
    return "Nao"
    
resultado = pode_voltar_ao_presente(c1, c2, c3)
print(resultado)