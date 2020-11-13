from tkinter import *
from tkinter import ttk
from main import *

app = Tk()
app.title("Busca Gulosa")
app.geometry("500x600")

listaCidades = ["Quito","Lima","Manaus","La Paz","Brasilia","São Paulo","Santiago","Buenos Aires"]

lb_origem = Label(app, text="Origem:")
lb_origem.place(x=20, y=5)

cb_origem = ttk.Combobox(app, values=listaCidades)
cb_origem.place(x=20, y=30)

lb_destino = Label(app, text="Destino:")
lb_destino.place(x=180, y=5)

cb_destino = ttk.Combobox(app, values=listaCidades)
cb_destino.place(x=180, y=30)

botao_1 = Button(app, width=8, text="Buscar", command=buscarRota(cb_destino.get(),cb_destino.get()), background="gray")
botao_1.place(x=330, y=28)

#Componente para exibir o mapa e rota encontrada
canvas = Canvas(width=480, height=515, bg="blue")
canvas.place(x=10, y=70)

#criando e adicionando mapa na canvas
imagem_1 = PhotoImage(file="img/america_sul.png")
mapa = Label(canvas, image = imagem_1)
canvas.create_image(0, 0, image=imagem_1, anchor='nw')

#Localização "geográfica" de cada cidade
bogota = [121, 75]
Quito = [83, 127]
Lima = [100, 220]
manaus = [353, 297]
laPaz = [185, 220]
brasilia = [265, 229]
saoPaulo = [240, 127]
Santiago = [134, 442]
buenoAires = [240,410]

#rsequencia de cidades (será retornado a partir do main)
caminho = [0, 0]

#transformando a caminho sequencia de pontos geometricos
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

canvas.create_line(rota, fill="blue", width=3)

app.mainloop()