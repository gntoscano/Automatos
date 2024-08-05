#AFD -- Automatos Finitos Determinísticos

#Definindo estruturas
estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_aceitacao = []

#Receber dados do automato

estados = input("Informe o conjunto de estados: ").split() #Armazenar os estados como uma lista de estados

alfabeto = input("Informe o alfabeto de entrada: ").split() #Define o alfabeto a ser utilizado pelo automato

estado_inicial = input("Informe o estado inicial: ") #Define o estado incial

estados_aceitacao = input("Informe os conjuntos de estados de aceitação: ").split() #define os possiveis estados de aceitação

print("Defina as funções de transição: ")
for estado in estados:
    for simbolo in alfabeto: #Checar cada estado com cada possivel simbolo digitado
        print(f"\t {simbolo}")
        print(f"{estado}\t----->\t", end="")
        proximo_estado = input()

        if proximo_estado == ".": #Caso um estado nao faça nada
            func_transicao[(estado, simbolo)] = None
        else:
            func_transicao[(estado, simbolo)] = proximo_estado

#Reconhecer linguagens
entrada = input("\nInforme a linguagem a ser reconhecida: ") #Pede o texto que o automato analisará se é possível

estado_atual = estado_inicial #Inicia pelo estado incial

for simbolo in entrada: #Checa cada simbolo do texto
    print(f"Estado atual: {estado_atual}") 
    print(f"Entrada atual: {simbolo}")

    print(f"Proximo estado: {func_transicao[(estado_atual, simbolo)]} \n")

    estado_atual = func_transicao[(estado_atual, simbolo)]

    if estado_atual == None:
        print("O automato nao reconheceu essa linguagem!")
        break

if estado_atual in estados_aceitacao:
    print("Reconheceu!")
else:
    print("Não reconheceu!")