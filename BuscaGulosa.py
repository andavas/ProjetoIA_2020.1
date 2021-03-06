import tkinter as tk        #utilizada para os objetos da janela
from tkinter import ttk     #utilizada no objeto combobox
from tkinter import font    #utilizado para os objetos de fontes
import Algoritmo as busca   #arquivo com algoritmo da busca gulosa
from tkinter import messagebox

# definindo coordenadas das cidades no plano cartesiano (mapa)
# ORDEM:
# indice da cidade
# nome da cidade
# posição (x, y) do ponto da cidade
# posição (x, y) do nome da cidade


#coluna:  0     1            2    3    4    5    6    7
eixoXY = [(0, 'Bogotá',      140, 161, 140, 145, 140, 128),
          (1, "Quito",       95,  208, 65,  208, 65,  225),
          (2, "Lima",        115, 300, 90,  298, 90,  315),
          (3, "Manaus",      250, 185, 270, 170, 270, 152),
          (4, "La Paz",      195, 285, 160, 277, 160, 260),
          (5, "Brasília",    290, 293, 255, 295, 255, 310),
          (6, "São Paulo",   387, 380, 435, 380, 435, 395),
          (7, "Santiago",    178, 515, 178, 540, 178, 560),
          (8, "Buenos Aires",270, 485, 333, 480, 333, 500)]

# armazena os elementos "linha" da rota encontrada       
deletes = []
# armazena os elemtentos os valores das heurística da busca atual
deletesHeuristica = []

#Função para exibir a heurística
def exibirHeuristica():
    
    if deletesHeuristica == []:
        destino = combobox_destino.get()
        for i in eixoXY:
            if destino == i[1]:
                auxDestino = i[0]

        heuristicaAtual = busca.heuristica

        if deletes != []:
            for index, nome, eixoX, eixoY, eixoXT, eixoYT, heuristicaX, heuristicaY in eixoXY: 
                deletesHeuristica.append(0)
                #inserindo heuristicas no mapa
                deletesHeuristica[-1] = canvas_mapa.create_text(heuristicaX, heuristicaY,                                                                fill="blue",
                                                                text=heuristicaAtual[auxDestino][index],
                                                                font = font_mapa) 
    else:
        for i in deletesHeuristica:
            # se exister alguma heuristica escrita no mapa ela será deletada antes de exibir novos valores
            canvas_mapa.delete(i)
        deletesHeuristica.clear()
            
#função executada pelo botão BUSCAR
def aoClicar():
    
    for i in deletes:
        # deletando rota da busca anterior
        canvas_mapa.delete(i)

    for i in deletesHeuristica:
        # sdeletando heurística da busca anterior
        canvas_mapa.delete(i)
    deletesHeuristica.clear()
   
    origem = combobox_origem.get()
    destino = combobox_destino.get()
    if origem != "" and destino != "":
        #buscando rota a partir da origem e destino
        #buscando cidades que serão percorridas
        caminho = busca.nomeToCodigo(origem, destino)
        caminho = busca.buscarRota(caminho[0], caminho[1])
        
        #calculando custo da rota
        custo = busca.calculaCusto(caminho)
        custo = 'Custo: '+str(custo)+' km'
        text_custo.set(custo) 

        #convertendo o caminho (cidades) em uma lista de coordenadas geográficas
        rota = []                       
        for i in caminho:               
            rota.append(eixoXY[i][2])   #eixo X
            rota.append(eixoXY[i][3])   #eixo Y

        #rota possui mais de uma cidade
        if(len(rota)>2): 
            for i in range(len(caminho)-1):
                #fransformando em pares de coordenadas
                auxrota = rota[i*2:(i*2)+4]

                #adicionando rota ao mapa
                deletes.append(0)
                deletes[-1] = canvas_mapa.create_line(auxrota, fill="blue", width=3)

                #destacando as cidades contidas na rota
                deletes.append(0)
                deletes[-1] = canvas_mapa.create_oval(rota[i*2]-5, rota[i*2+1]-5, rota[i*2]+5, rota[i*2+1]+5, fill="blue")

            #destacando a cidade destino    
            deletes.append(0)
            deletes[-1] = canvas_mapa.create_oval(rota[len(rota)-2]-5, rota[len(rota)-1]-5, rota[len(rota)-2]+5, rota[len(rota)-1]+5, fill="blue")
                        
        else:  #destacando cidade no mapa
            deletes.append(0) 
            deletes[-1] = canvas_mapa.create_oval(rota[0]-5, rota[1]-5, rota[0]+5, rota[1]+5, fill="blue")
    else:
        messagebox.showinfo("Erro", "Informe cidades de origem e destino!")


# criando o objeto "aplication" (que é uma janela)
aplication = tk.Tk()
aplication.title("Busca Gulosa") #Título exibido no topo da janela
aplication.geometry("570x761") #tamanho da janela
aplication.resizable(width=0, height=0) #o tamanho da janela não poderar ser alterado "maximizar/restaurar tamanho"

#lsita das cidades utilizadas para exibição no combobox
lista_de_cidades = ['Bogotá', 'Brasília', 'Buenos Aires','La Paz', 'Lima', 'Manaus', 'Quito', 'Santiago', 'São Paulo']

label_origem = tk.Label(aplication, text="Origem:")                 #label exibido como descrição do combobox
label_origem.place(x=10, y=5)                                       #posição do label na tela
combobox_origem = ttk.Combobox(aplication, values=lista_de_cidades) #combobox com as opções de cidades de onde a busca irá iniciar
combobox_origem.place(x=10, y=30)                                   #posição do combobox na tela

label_destino = tk.Label(aplication, text="Destino:")               #label exibido como descrição do combobox
label_destino.place(x=190, y=5)                                     #posição do label na tela
combobox_destino = ttk.Combobox(aplication, values=lista_de_cidades)#combobox com as opções de cidades de onde a busca irá finalizar
combobox_destino.place(x=190, y=30)                                 #posição do combobox na tela    

text_custo = tk.StringVar()               
text_custo.set("Custo: ") 
label_custo = tk.Label(aplication, textvariable=text_custo)         #label exibido como descrição do custo da rota         
label_custo.place(x=385, y=5)

# botão que executar a função "aoClicar()"
button_viajar = tk.Button(aplication, command=aoClicar, width=10, height=1, text="Buscar")
button_viajar.place(x=385, y=25) #posição do botão na tela

# botão que executar a função "exibirHeuristica()"
button_heuristica = tk.Button(aplication, command=exibirHeuristica, width=10, height=1, text="heurística")
button_heuristica.place(x=480, y=25) #posição do botão na tela

# elemento que contem o mapa, cidades, e rotas
canvas_mapa = tk.Canvas(width=550, height=701) #definição do tamanho do canvas
canvas_mapa.place(x=10, y=60), #posição do canvas na tela

imagem_mapa = tk.PhotoImage(file="mapa.png") # carregando a imagem do mapa
canvas_mapa.create_image(0, 0, image=imagem_mapa, anchor='nw') #adicionando a imagem do mapa ao canvas

#definindo tipo e tamanho da fonte utilizada no mapa
font_mapa = font.Font(family='Comic Sans MS', size=13, weight='bold')

#Desenhado as rotas no mapa
for index, nome, eixoX, eixoY, eixoXT, eixoYT, x, y in eixoXY:      # buscando as cidades e suas coordenadas
    for i in range(len(busca.aresta[index])):                       # matriz de aresta definida no back
        if busca.aresta[index][i] != 0:                             # verificando quais arestas uma cidade possui
            auxrota = []                                            # armazena iformações das arestas para desenhar as rotas
            auxrota.append(eixoX)
            auxrota.append(eixoY)
            auxrota.append(eixoXY[i][2])
            auxrota.append(eixoXY[i][3])
            canvas_mapa.create_line(auxrota, fill="black", width=3) # criando desenho das rotas de uma cidade, defindo cor e tamanho
            
for index, nome, eixoX, eixoY, eixoXT, eixoYT, x, y in eixoXY:                                  
    canvas_mapa.create_oval(eixoX-5, eixoY-5, eixoX+5, eixoY+5, fill="white", outline='black' ) #inserindo cidade (ponto) no mapa
    canvas_mapa.create_text(eixoXT, eixoYT, text=nome, font = font_mapa)                        #inserindo nomes das cidades no mapa

aplication.mainloop() #método que faz a janela ficar rodando até que acione o botão FECHAR
