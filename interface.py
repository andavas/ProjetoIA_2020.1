import tkinter as tk
from tkinter import ttk
import busca as busca

eixoXY = [(0, 'Bogotá', 140, 161),
          (1, "Quito", 95, 208),
          (2, "Lima", 0, 0),
          (3, "Manaus", 0, 0),
          (4, "La Paz", 0, 0),
          (5, "Brasilia", 0, 0),
          (6, "São Paulo", 0, 0),
          (7, "Santiago", 0, 0),
          (8, "Buenos Aires", 0, 0)]


aplication = tk.Tk()
aplication.title("Busca Gulosa")
aplication.geometry("570x761")
aplication.resizable(width=0, height=0)

lista_de_cidades = ['Bogotá', 'Brasília', 'Buenos Aires',
                    'La Paz', 'Lima', 'Manaus', 'Quito', 'Santiago', 'São Paulo']

label_origem = tk.Label(aplication, text="Origem:")
label_origem.place(x=10, y=5)
combobox_origem = ttk.Combobox(aplication, values=lista_de_cidades)
combobox_origem.place(x=10, y=30)

label_destino = tk.Label(aplication, text="Destino:")
label_destino.place(x=213, y=5)
combobox_destino = ttk.Combobox(aplication, values=lista_de_cidades)
combobox_destino.place(x=213, y=30)

button_viajar = tk.Button(aplication, width=19, height=1,
                          text="Viajar por Busca Gulosa")
button_viajar.place(x=416, y=25)

canvas_mapa = tk.Canvas(width=570, height=701)
canvas_mapa.place(x=10, y=60),
imagem_mapa = tk.PhotoImage(file="imagem/teste.png")
canvas_mapa.create_image(0, 0, image=imagem_mapa, anchor='nw')

for index, nome, eixoX, eixoY in eixoXY:
    canvas_mapa.create_oval(eixoX-5, eixoY-5, eixoX+5, eixoY+5, fill="white", outline='black' )
    canvas_mapa.create_text(eixoX, eixoY, text=nome)


aplication.mainloop()
