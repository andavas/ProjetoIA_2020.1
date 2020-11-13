import tkinter as tk
from tkinter import ttk
import main as ma

caminho = []

def aoClicar():
    caminho = ma.buscarRota(cb_origem.get(), cb_destino.get())
    rota = []
    for i in caminho:
        if i == 0:
            rota += bogota
        elif i== 1:
            rota += Quito
        elif i== 2:
            rota += Lima
        elif i== 3:
            rota += manaus
        elif i== 4:
            rota += laPaz
        elif i== 5:
            rota += brasilia
        elif i== 6:
            rota += saoPaulo
        elif i== 7:
            rota += Santiago
        else:
            rota += buenoAires

    if(len(rota)>2):
        for i in range(len(caminho)-1):
            auxrota = rota[i*2:(i*2)+4]
            print(auxrota)
            canvas.create_line(auxrota, fill="blue", width=3)
    else:
        canvas.create_oval(rota[0]-4, rota[1]-4, rota[0]+4, rota[1]+4, fill="blue")


app = tk.Tk()
app.title("Busca Gulosa")
app.geometry("500x600")

listaCidades = ["Quito","Lima","Manaus","La Paz","Brasilia","São Paulo","Santiago","Buenos Aires"]

lb_origem = tk.Label(app, text="Origem:")
lb_origem.place(x=20, y=5)

cb_origem = ttk.Combobox(app, values=listaCidades)
cb_origem.place(x=20, y=30)

lb_destino = tk.Label(app, text="Destino:")
lb_destino.place(x=180, y=5)

cb_destino = ttk.Combobox(app, values=listaCidades)
cb_destino.place(x=180, y=30)

caminho1 = []

botao_1 = tk.Button(app, width=8, text="Buscar", command=aoClicar, background="gray")
botao_1.place(x=330, y=28)


#Componente para exibir o mapa e rota encontrada
canvas = tk.Canvas(width=480, height=515, bg="blue")
canvas.place(x=10, y=70)

#criando e adicionando mapa na canvas
imagem_1 = tk.PhotoImage(file="img/america_sul.png")
mapa = tk.Label(canvas, image = imagem_1)
canvas.create_image(0, 0, image=imagem_1, anchor='nw')

#Localização "geográfica" de cada cidade
bogota = [121, 75]
Quito = [83, 127]
Lima = [100, 220]
manaus = [240, 127]
laPaz = [185, 220]
brasilia = [265, 229]
saoPaulo = [353, 297]
Santiago = [134, 442]
buenoAires = [240,410]

app.mainloop()