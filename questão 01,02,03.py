#questao 01
N = int(input("Forneça um valor inteiro: "))

if 1 < N < 1000:
    
    for i in range(1, N + 1):
        
        col1 = i
        col2 = i ** 2
        col3 = i ** 3
        
        print(f"{col1} {col2} {col3}")
else:
    print("O valor de N deve ser maior que 1 e menor que 1000.")
    
#questao 02
def main():
    print("Forneça o valor dos depósitos:")
    valores = [float(input()) for _ in range(7)]
    
    total_poupado = 0.0
    dias_cumpridos = 0
    
    valor_anterior = valores[0]
    total_poupado += valor_anterior
    
    for i in range(1, 7):
        valor_atual = valores[i]
        total_poupado += valor_atual
        if valor_atual >= valor_anterior + 0.50:
            dias_cumpridos += 1
        valor_anterior = valor_atual
    
    print(f"Poliana conseguiu economizar R$ {total_poupado:.2f}")
    print(f"Ela cumpriu a meta {dias_cumpridos} vezes")
    
#questao 3    

if __name__ == "__main__":
    main()
def verificar_capacidade_maxima():
    import sys
    input = sys.stdin.read
    dados = input().splitlines()

    N, C = map(int, dados[0].split())
    
    passageiros_atual = 0

    capacidade_excedida = False
    for i in range(1, N + 1):
        S, E = map(int, dados[i].split())
        passageiros_atual -= S
        passageiros_atual += E
        
        if passageiros_atual > C:
            capacidade_excedida = True
            break

    if capacidade_excedida:
        print("A quantidade de passageiros excedeu o limite maximo")
    else:
        print("A quantidade de passageiros nao excedeu o limite maximo")

import io
import sys

entrada = """5 10
5 0
2 7
3 2
0 2
0 1"""
sys.stdin = io.StringIO(entrada)

verificar_capacidade_maxima()