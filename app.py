from tkinter import *
from tkinter import ttk

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

botao_1 = Button(app, width=8, text="Buscar", command="buscar", background="gray")
botao_1.place(x=330, y=28)

#criando e adicionando mapa na tela
#imagem_1 = PhotoImage(file="img/america_sul.png")
#mapa = Label(canvas, image = imagem_1)
#mapa.place(x=10, y=70)

canvas = Canvas(width=480, height=515, bg="blue")
canvas.place(x=10, y=70)

#criando e adicionando mapa na tela
imagem_1 = PhotoImage(file="img/america_sul.png")
mapa = Label(canvas, image = imagem_1)
canvas.create_image(0, 0, image=imagem_1, anchor='nw')

#Rota encontrada

#bogota la paz buenos Aires
rota_1 = [121, 75, 185, 220, 240, 410]

#manaus brasilia sao paulo
rota_2 = [353, 297, 265, 229, 240, 127]
#adicionando a rota na tela

canvas.create_line(rota_2, fill="red", width=3)


app.mainloop()