import tkinter as tk        #utilizada para os objetos da janela
from tkinter import ttk     #utilizada no objeto combobox
from tkinter import font    #utilizado para os objetos de fontes
import busca as busca       #arquivo com algoritmo da busca gulosa

# definindo coordenadas das cidades no plano cartesiano (mapa)
# ORDEM:
# indice da cidade
# nome da cidade
# posição (x, y) do ponto da cidade
# posição (x, y) do nome da cidade

eixoXY = [(0, 'Bogotá', 140, 161, 140, 145),
          (1, "Quito", 95, 208, 65, 208),
          (2, "Lima", 115, 300, 90, 298),
          (3, "Manaus",  250, 185, 270, 170),
          (4, "La Paz", 195, 285, 160, 277),
          (5, "Brasília", 290, 293, 255, 295),
          (6, "São Paulo", 387, 380, 435, 380),
          (7, "Santiago", 178, 515, 178, 540),
          (8, "Buenos Aires", 270, 485, 333, 480)]

# armazena os elementos "linha" da rota encontrada       
deletes = []

#função executada pelo botão BUSCAR
def aoClicar():
    
    for i in deletes:
        #se exister alguma rota desenhada no mapa ela será deletada antes de traçar outra rota
        canvas_mapa.delete(i)
   
    caminho = busca.nomeToCodigo(combobox_origem.get(), combobox_destino.get())
    caminho = busca.buscarRota(caminho[0], caminho[1])

    rota = []                       # armazena cidades que serão percorridas
    for i in caminho:               # busca coordenadas das cidades que serão percorridas
        rota.append(eixoXY[i][2])   
        rota.append(eixoXY[i][3])

    if(len(rota)>2): #se a origem for diferente do destino, os pontos das cidades e a rota entre elas serão pintadas de azul
        for i in range(len(caminho)-1):
            auxrota = rota[i*2:(i*2)+4]

            #pintando as rotas entre as cidades percorridas de azul
            deletes.append(0)
            deletes[-1] = canvas_mapa.create_line(auxrota, fill="blue", width=3)

            #pintando de azul os pontos das cidades de origem e intermediárias
            deletes.append(0)
            deletes[-1] = canvas_mapa.create_oval(rota[i*2]-5, rota[i*2+1]-5, rota[i*2]+5, rota[i*2+1]+5, fill="blue") 

        #pintando o ponto da cidade final de azul    
        deletes.append(0)
        deletes[-1] = canvas_mapa.create_oval(rota[len(rota)-2]-5, rota[len(rota)-1]-5, rota[len(rota)-2]+5, rota[len(rota)-1]+5, fill="blue")
                    
    else:  #adicionando um único ponto ao mapa quando vidade origem e destino são iguais.
        deletes.append(0) 
        deletes[-1] = canvas_mapa.create_oval(rota[0]-5, rota[1]-5, rota[0]+5, rota[1]+5, fill="blue")

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
label_destino.place(x=213, y=5)                                     #posição do label na tela
combobox_destino = ttk.Combobox(aplication, values=lista_de_cidades)#combobox com as opções de cidades de onde a busca irá finalizar
combobox_destino.place(x=213, y=30)                                 #posição do combobox na tela

# botão que executar a função "aoClicar"
button_viajar = tk.Button(aplication, command=aoClicar, width=10, height=1, text="Buscar")
button_viajar.place(x=416, y=25) #posição do botão na tela

# elemento que contem o mapa, cidades, e rotas
canvas_mapa = tk.Canvas(width=570, height=701) #definição do tamanho do canvas
canvas_mapa.place(x=10, y=60), #posição do canvas na tela

imagem_mapa = tk.PhotoImage(file="imagem/mapa.png") # carregando a imagem do mapa
canvas_mapa.create_image(0, 0, image=imagem_mapa, anchor='nw') #adicionando a imagem do mapa ao canvas

#definindo tipo e tamanho da fonte utilizada no mapa
font_mapa = font.Font(family='Comic Sans MS', size=13, weight='bold')

#Desenhado as rotas no mapa
for index, nome, eixoX, eixoY, eixoXT, eixoYT in eixoXY:            # buscando as cidades e suas coordenadas
    for i in range(len(busca.aresta[index])):                       # buscando as arestas
        if busca.aresta[index][i] != 0:                             # verificando quais arestas uma cidade possui
            auxrota = []                                            # armazena iformações das arestas para desenhas as rotas
            auxrota.append(eixoX)
            auxrota.append(eixoY)
            auxrota.append(eixoXY[i][2])
            auxrota.append(eixoXY[i][3])
            canvas_mapa.create_line(auxrota, fill="black", width=3) # criando desenho das rotas de uma cidade, defindo cor e tamanho
            
for index, nome, eixoX, eixoY, eixoXT, eixoYT in eixoXY:                                        #percorrendo listas com as cidades para adicionar pontos e nomes ao mapa
    canvas_mapa.create_oval(eixoX-5, eixoY-5, eixoX+5, eixoY+5, fill="white", outline='black' ) #inserindo cidade (ponto) no mapa
    canvas_mapa.create_text(eixoXT, eixoYT, text=nome, font = font_mapa)                        #inserindo nomes das cidades no mapa

aplication.mainloop() #método que faz a janela ficar rodando até que acione o botão FECHAR
