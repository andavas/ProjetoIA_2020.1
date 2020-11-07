# -*- coding: utf-8 -*-
#Cidade
# valores: id, nome, lista de id das cidades que tem rota
#bogota =       [0,'Bogotá',      [1,2,4]]
#quito =        [1,'Quito',       [0,2,5]]
#lima =         [2,'Lima',        [1,4]]
#manaus =       [3,'Manaus',      [0,4,5,6]]
#laPaz =        [4,'La Paz',      [0,2,3,7,8]]
#brasilia =     [5,'Brasilia',    [1,3,6,8]]
#saoPaulo =     [6,'Sao Paulo',   [3,5,7,8]]
#santiago =     [7,'Santiago',    [4,6,8]]
#buenosAires =  [8,'Buenos Aires',[4,5,6]]

#lista com a matriz de arestas de cada cidade
# valores : custo em km, de acordo com o índice de cada cidade (descritas acima)
matArestas = [
    [0,728,0,1783,2435,0,0,0,0], #0 = bogotá
    [728,0,1326,0,0,3777,0,0,0], #1 = quito
    [0,1326,0,0,1077,0,0,0,0],
    [1783,0,0,0,1733,1934,2689,0,0],
    [2435,0,1077,1733,0,0,0,2236,1904],
    [0,3777,0,1934,0,0,876,0,2239],
    [0,0,0,2689,0,876,0,2582,1673],
    [0,0,0,0,2236,0,2582,0,1137],
    [0,0,0,0,1904,2239,1673,0,0]
    ]


#lista de tuplas contendo as distancias de cadas cidade em linha reta
# valores : distancias em linha reta, em relação a cada cidade (descrita pelo índice)
matHeuristica = [
    [0,728,1879,1783,2435,3663,4319,4249,4659], #0 = bogotá
    [728,0,1326,2081,2138,3777,4308,3788,4359], #1 = quito
    [1879,1326,0,2119,1077,3165,3451,2470,3137],
    [1783,2081,2119,0,1733,1932,2689,3552,3505],
    [2435,2138,1077,1733,0,2161,2376,1904,2236],
    [3663,3777,3165,1932,2161,0,876,3010,2339],
    [4319,4308,3451,2689,2376,876,0,2582,1673],
    [4249,3788,2470,3552,1904,3010,2582,0,1137],
    [4659,4359,3137,3505,2236,2339,1673,1137,0]
    ]

# representa o código da cidade de início e fim
tuplaEstados = [(0,'Bogotá'),
                (1,"Quito"),
                (2,"Lima"),
                (3,"Manaus"),
                (4,"La Paz"),
                (5,"Brasilia"),
                (6,"São Paulo"),
                (7,"Santiago"),
                (8,"Buenos Aires")]

# Guarda as cidades que tem a rota para a cidade atual, em relação a cidade fim
# ex: la paz vai para as cidades=> auxArestas=[0,2,3,7,8]
auxArestas=[]

# Guarda as distâncias em linha reta de cada cidade na auxArestas
# ex: auxHeuristica=[4659,3137,3505,1137,0]
auxHeuristica = []

# Guarda as cidades percorridas 
# ex: bogota>la paz>buenos aires => vetCaminhos = [0,4,8]
vetCaminhos = []


#Estado inicio e fim são recebidos da interface
estadoInicio=int(input("Insira o codigo da cidade inicio: "))
estadoFim=int(input("Insira o codigo da cidade fim: "))

# coloca a cidade inicial na lista de cidades percorridas
vetCaminhos.append(estadoInicio)

###
# verificações a serem feitas no algoritmo
#verificar ao chegar na cidade
# é igual ao final?
# já passei?
#senão? roda algoritmo
###
# função externa

def menorValor(lista):
    temp = (-1,float("inf"))
    for index,item in lista:
        if temp[1] > item:
            temp = (index,item)
    return temp

encontrei=False

while not encontrei:
    auxArestas = []
    auxHeuristica = []

    cidadeAtual=vetCaminhos[-1]

    if cidadeAtual == estadoFim:
        encontrei=True
        print(vetCaminhos)

    else:
        for i,item in enumerate(matArestas[cidadeAtual]): # verifica as rotas disponíveis na matriz de arestas
            if matArestas[cidadeAtual][i] != 0: # se verdadeiro, existe rota da cidade atual para a cidade de indice i
                if i not in vetCaminhos: # verifica se já existe no vetor de caminhos
                    auxArestas.append(i)
        print("Aux Arestas------------------------------------------------------")
        print(auxArestas)
        print("------------------------------------------------------")
        if len(auxArestas) == 0:  # se auxArestas estiver vazio, não há mais rotas disponíveis
            break 
        for i in auxArestas: # verifica a menor distância entre a cidade fim e cada cidade que tem rota para a cidade atual
            if matHeuristica[estadoFim][i] == 0: # já estamos na cidade final 
                print('terminou')
                encontrei=True
                vetCaminhos.append(i)
                break
            else:
                auxHeuristica.append((i,matHeuristica[estadoFim][i]))
        
        print("Aux Heuristica------------------------------------------------------")
        print(auxHeuristica)
        print("------------------------------------------------------")
        temp = menorValor(auxHeuristica)
        print("temp------------------------------------------------------")
        print(temp)
        print("------------------------------------------------------")
        if not encontrei:
            vetCaminhos.append(temp[0])
        print(vetCaminhos)