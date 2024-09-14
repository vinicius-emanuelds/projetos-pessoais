import math

def menu():
    print("\n ============ Menu ============ ")
    print("\n 1 - Converta ângulos em graus para radianos")
    print("\n 2 - Converta ângulos em radianos para graus")
    print("\n 3 - Sair")
    print("\n")

def opcao1():
    deg = float(input("Digite o ângulo, em graus:"))
    resultado = (deg * math.pi) / 180.0

    print(f"O ângulo mede, aproximadamente, {resultado: .4f} rad.")
    
def opcao2():
    rad = float(input("Digite o ângulo, em radianos:"))
    resultado = (rad * 180.0) / math.pi

    print(f"O ângulo mede, aproximadamente, {resultado: .4f} graus.")
    
def opcao3():
    print("Saindo do programa...")

def opcao_invalida():
    print("Opção inválida. Por favor, escolha uma opção válida.")

def switch_case_match_case(value): 
    match value: 
    
        case 1:
            opcao1 ()
    
        case 2: 
            opcao2 ()
        
        case 3: 
            opcao3 ()
    
        case _: 
            opcao_invalida ()
        
        
opcao = 0

while opcao != 3:
    menu ()
    
    try:
        opcao = int(input("Digite a opção desejada: "))
    except:
        print("Entrada inválida. Por favor, digite um número.")
        continue

    funcao = switch_case_match_case(opcao)