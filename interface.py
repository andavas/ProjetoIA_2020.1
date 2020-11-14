import tkinter as tk
from tkinter import ttk
from tkinter import font
import busca as busca

eixoXY = [(0, 'Bogotá', 140, 161, 140, 145),
          (1, "Quito", 95, 208, 65, 208),
          (2, "Lima", 115, 300, 90, 298),
          (3, "Manaus",  250, 185, 270, 170),
          (4, "La Paz", 195, 285, 160, 277),
          (5, "Brasília", 290, 293, 255, 295),
          (6, "São Paulo", 387, 380, 435, 380),
          (7, "Santiago", 178, 515, 178, 540),
          (8, "Buenos Aires", 270, 485, 333, 480)]
        
deletes = []

def aoClicar():
    
    for i in deletes:
        canvas_mapa.delete(i)
   
    caminho = busca.nomeToCodigo(combobox_origem.get(), combobox_destino.get())
    caminho = busca.buscarRota(caminho[0], caminho[1])

    rota = []
    for i in caminho:
        rota.append(eixoXY[i][2])
        rota.append(eixoXY[i][3])

    if(len(rota)>2):
        for i in range(len(caminho)-1):
            auxrota = rota[i*2:(i*2)+4]

            deletes.append(0)
            deletes[-1] = canvas_mapa.create_line(auxrota, fill="blue", width=3)

            deletes.append(0)
            deletes[-1] = canvas_mapa.create_oval(rota[i*2]-5, rota[i*2+1]-5, rota[i*2]+5, rota[i*2+1]+5, fill="blue")
            
        deletes.append(0)
        deletes[-1] = canvas_mapa.create_oval(rota[len(rota)-2]-5, rota[len(rota)-1]-5, rota[len(rota)-2]+5, rota[len(rota)-1]+5, fill="blue")
        
    else:
        deletes.append(0)
        deletes[-1] = canvas_mapa.create_oval(rota[0]-5, rota[1]-5, rota[0]+5, rota[1]+5, fill="blue")

aplication = tk.Tk()
aplication.title("Busca Gulosa")
aplication.geometry("570x761")
aplication.resizable(width=0, height=0)

lista_de_cidades = ['Bogotá', 'Brasília', 'Buenos Aires','La Paz', 'Lima', 'Manaus', 'Quito', 'Santiago', 'São Paulo']

label_origem = tk.Label(aplication, text="Origem:")
label_origem.place(x=10, y=5)
combobox_origem = ttk.Combobox(aplication, values=lista_de_cidades)
combobox_origem.place(x=10, y=30)

label_destino = tk.Label(aplication, text="Destino:")
label_destino.place(x=213, y=5)
combobox_destino = ttk.Combobox(aplication, values=lista_de_cidades)
combobox_destino.place(x=213, y=30)


button_viajar = tk.Button(aplication, command=aoClicar, width=19, height=1, text="Viajar por Busca Gulosa")
button_viajar.place(x=416, y=25)

canvas_mapa = tk.Canvas(width=570, height=701)
canvas_mapa.place(x=10, y=60),

imagem_mapa = tk.PhotoImage(file="imagem/mapa.png")
canvas_mapa.create_image(0, 0, image=imagem_mapa, anchor='nw')

font_mapa = font.Font(family='Comic Sans MS', size=13, weight='bold')


for index, nome, eixoX, eixoY, eixoXT, eixoYT in eixoXY:
    for i in range(len(busca.aresta[index])):
        if busca.aresta[index][i] != 0:
            auxrota = []
            auxrota.append(eixoX)
            auxrota.append(eixoY)
            auxrota.append(eixoXY[i][2])
            auxrota.append(eixoXY[i][3])
            canvas_mapa.create_line(auxrota, fill="black", width=3)
            
for index, nome, eixoX, eixoY, eixoXT, eixoYT in eixoXY:    
    canvas_mapa.create_oval(eixoX-5, eixoY-5, eixoX+5, eixoY+5, fill="white", outline='black' )
    canvas_mapa.create_text(eixoXT, eixoYT, text=nome, font = font_mapa)

aplication.mainloop()
