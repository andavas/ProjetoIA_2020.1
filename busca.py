# -*- coding: utf-8 -*-
vertice = [(0, 'Bogotá'),
           (1, "Quito"),
           (2, "Lima"),
           (3, "Manaus"),
           (4, "La Paz"),
           (5, "Brasília"),
           (6, "São Paulo"),
           (7, "Santiago"),
           (8, "Buenos Aires")]

aresta = [[0, 728, 0, 1783, 2435, 0, 0, 0, 0],
          [728, 0, 1326, 0, 0, 3777, 0, 0, 0],
          [0, 1326, 0, 0, 1077, 0, 0, 0, 0],
          [1783, 0, 0, 0, 1733, 1934, 2689, 0, 0],
          [2435, 0, 1077, 1733, 0, 0, 0, 2236, 1904],
          [0, 3777, 0, 1934, 0, 0, 876, 0, 2239],
          [0, 0, 0, 2689, 0, 876, 0, 2582, 1673],
          [0, 0, 0, 0, 2236, 0, 2582, 0, 1137],
          [0, 0, 0, 0, 1904, 2239, 1673, 1139, 0],
          [0, 0, 0, 0, 1904, 2239, 1673, 0, 0]]

heuristica = [[0, 728, 1879, 1783, 2435, 3663, 4319, 4249, 4659],
              [728, 0, 1326, 2081, 2138, 3777, 4308, 3788, 4359],
              [1879, 1326, 0, 2119, 1077, 3165, 3451, 2470, 3137],
              [1783, 2081, 2119, 0, 1733, 1932, 2689, 3552, 3505],
              [2435, 2138, 1077, 1733, 0, 2161, 2376, 1904, 2236],
              [3663, 3777, 3165, 1932, 2161, 0, 876, 3010, 2339],
              [4319, 4308, 3451, 2689, 2376, 876, 0, 2582, 1673],
              [4249, 3788, 2470, 3552, 1904, 3010, 2582, 0, 1137],
              [4659, 4359, 3137, 3505, 2236, 2339, 1673, 1137, 0]]


def nomeToCodigo(origem, destino):
    auxiliarVertice = []
    auxiliarVertice.append(0)
    auxiliarVertice.append(0)

    for i, value in vertice:
        if value == origem:
            auxiliarVertice[0] = i
        if value == destino:
            auxiliarVertice[1] = i
    return auxiliarVertice


def buscarRota(origem, destino):
    auxiliarVertice = []
    auxiliarHeuristica = []
    caminho = []
    cheguei = False

    caminho.append(origem)

    while not cheguei:

        auxiliarVertice = []
        auxiliarHeuristica = []

        cidadeAtual = caminho[-1]

        if cidadeAtual == destino:
            cheguei = True

        else:
            for i in range(len(aresta[cidadeAtual])):
                if aresta[cidadeAtual][i] != 0:
                    if i not in caminho:
                        auxiliarVertice.append(i)
            if len(auxiliarVertice) == 0:
                break

            for i in auxiliarVertice:
                if heuristica[destino][i] == 0:
                    cheguei = True
                    caminho.append(i)
                else:
                    auxiliarHeuristica.append((i, heuristica[destino][i]))

            if len(auxiliarVertice) != 0:
                temp = buscarMenor(auxiliarHeuristica)
            
            if len(auxiliarVertice) != 0:
                temp = buscarMenor(auxiliarHeuristica)

            if not cheguei:
                caminho.append(temp)
    return caminho


def buscarMenor(lista):
    menor = lista[0]
    for i, valor in lista:
        if valor < menor[1]:
            menor = (i, valor)

    return menor[0]