#Kauan Silva Santos 

# Leitura dos valores
D = int(input("Forneca o valor de D: "))
R = int(input("Forneca o valor de R: "))
L = int(input("Forneca o valor de L: "))
P = int(input("Forneca o valor de P: "))
G = int(input("Forneca o valor de G: "))

def pode_viajar(D, R, L, P, G):
    km_por_litro = 10
    max_km_tanque = L * km_por_litro
    
    if max_km_tanque >= D:
        print(f"Pode viajar.\nR$: {R}")
        return
   
    litros_necessarios = D / km_por_litro
    
    # Reabastecimentos necessários:
    litros_por_reabastecimento = max_km_tanque / km_por_litro
    num_reabastecimentos = -(-litros_necessarios // litros_por_reabastecimento)
    
    custo_total = (num_reabastecimentos - 1) * (L * G)
    
    if custo_total <= R:
        print(f"Pode viajar.\nR$: {R - custo_total}")
    else:
        print("Nao pode viajar.")

pode_viajar(D, R, L, P, G)