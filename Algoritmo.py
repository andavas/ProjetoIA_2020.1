# -*- coding: utf-8 -*-

# Cidades mapeadas e seus respectivos códigos

vertice = [(0, 'Bogotá'),
           (1, "Quito"),
           (2, "Lima"),
           (3, "Manaus"),
           (4, "La Paz"),
           (5, "Brasília"),
           (6, "São Paulo"),
           (7, "Santiago"),
           (8, "Buenos Aires")]

# Matriz de arestas 
# Em cada posição desta lista contém outra lista, uma para cada cidade mapeada.
# Estas listas internas representam a conexão entre cada cidade com todas as outras.
# Se o valor é 0, não há conexão entre a cidade representada na lista externa, com a cidade
# representada na lista interna
# Se é diferente de 0, há uma conexão entre as duas cidades, e o valor representa a distância
# em linha reta entre elas.

# Ex: aresta[3][4] => representa uma aresta entre a cidade de índice 3 (Manaus) 
# e a cidade de índice 4 (La Paz). Seu o custo é 1733 km

aresta = [[0, 728, 0, 1783, 2435, 0, 0, 0, 0],                      # 0 - Bogotá
          [728, 0, 1326, 0, 0, 3777, 0, 0, 0],                      # 1 - Quito
          [0, 1326, 0, 0, 1077, 0, 0, 0, 0],                        # 2 - Lima
          [1783, 0, 0, 0, 1733, 1934, 2689, 0, 0],
          [2435, 0, 1077, 1733, 0, 0, 0, 2236, 1904],
          [0, 3777, 0, 1934, 0, 0, 876, 0, 2239],
          [0, 0, 0, 2689, 0, 876, 0, 2582, 1673],
          [0, 0, 0, 0, 2236, 0, 2582, 0, 1137],
          [0, 0, 0, 0, 1904, 2239, 1673, 1139, 0],
          [0, 0, 0, 0, 1904, 2239, 1673, 0, 0]]                     # 8 - Buenos Aires

# Matriz heurística
# Semelhante a lista de arestas, mas esta matriz precisa guardar as distâncias em linha reta 
# entre cada uma outras cidades mapeadas, mesmo que não haja conexão direta entre elas.
# A representação e a disposição dos dados é igual a da matriz de arestas

heuristica = [[0, 728, 1879, 1783, 2435, 3663, 4319, 4249, 4659],   # 0 - Bogotá
              [728, 0, 1326, 2081, 2138, 3777, 4308, 3788, 4359],   # 1 - Quito
              [1879, 1326, 0, 2119, 1077, 3165, 3451, 2470, 3137],  # 2 - Lima
              [1783, 2081, 2119, 0, 1733, 1932, 2689, 3552, 3505],
              [2435, 2138, 1077, 1733, 0, 2161, 2376, 1904, 2236],
              [3663, 3777, 3165, 1932, 2161, 0, 876, 3010, 2339],
              [4319, 4308, 3451, 2689, 2376, 876, 0, 2582, 1673],
              [4249, 3788, 2470, 3552, 1904, 3010, 2582, 0, 1137],
              [4659, 4359, 3137, 3505, 2236, 2339, 1673, 1137, 0]]  # 8 - Buenos Aires


# Recebe o código das cidades de origem e destino, 
# e devolve uma lista com o nome das cidades

def nomeToCodigo(origem, destino):
    auxiliarVertice = [0,0] 

    for i, value in vertice:         
        if value == origem:
            auxiliarVertice[0] = i
        if value == destino:
            auxiliarVertice[1] = i
    return auxiliarVertice


# Recebe o código das cidades de origem e destino,
# e devolve uma lista com rota entre as cidades

def buscarRota(origem, destino):
    auxiliarVertice = [] 
    auxiliarHeuristica = []
    caminho = []
    cheguei = False

    caminho.append(origem) # adiciona a cidade de origem na rota

    while not cheguei:

        auxiliarVertice = []
        auxiliarHeuristica = []

        cidadeAtual = caminho[-1] # a cidade atual é sempre a última que foi adicionada na rota

        if cidadeAtual == destino: # Testa se a cidade de origem é o destino 
            cheguei = True

        else:
            # varre a lista de arestas disponíveis da cidade atual 
            for i in range(len(aresta[cidadeAtual])): 
                if aresta[cidadeAtual][i] != 0:     # se existe uma aresta até aquela cidade,
                    if i not in caminho:            # e ainda não foi percorrida,
                        auxiliarVertice.append(i)   # ela é adicionada a lista de arestas da cidade atual
            if len(auxiliarVertice) == 0: 
                break # se não houverem arestas disponíveis, o programa termina

            # varre a lista de arestas encontradas para a cidade atual 
            for i in auxiliarVertice:
                if heuristica[destino][i] == 0: # se a distância entre a cidade vizinha da atual e o destino for 0,
                    cheguei = True              # então, esta cidade vizinha é o destino,
                    caminho.append(i)           # e a cidade é inserida na rota
                else:
                    auxiliarHeuristica.append((i, heuristica[destino][i])) # caso contrário, o índice desta cidade vizinha é armazenada
                                                                           # juntamente com sua distância em linha reta da cidade destino

            temp = buscarMenor(auxiliarHeuristica)  # temp recebe o índice da cidade mais próxima do destino                                                 

            if not cheguei: # se o destino ainda não foi encontrado,
                caminho.append(temp) # adicionamos esta cidade na rota,
            # e o ciclo se repete

    return caminho # por fim, a rota entre as cidades é retornada

# recebe uma lista de tuplas, contendo o índice das cidades e suas distâncias até o destino,
# devolve o índice da cidade com a menor distância entre o destino e 

def buscarMenor(lista):    
    menor = lista[0]
    for i, valor in lista:
        if valor < menor[1]:
            menor = (i, valor)

    return menor[0]


# [8,5,1,2]
def calculaCusto(caminho):
    aux = 0
    for i in range(len(caminho)-1):
        aux = aresta[caminho[i]][caminho[i+1]] + aux
    return aux