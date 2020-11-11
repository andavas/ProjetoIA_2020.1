import Tkinter as tk

class Application:
    def __init__(self, master=None):
        l1 = tk.Label(text="Test", fg="black", bg="white")


root = tk.Tk()
Application(root)
root.mainloop()