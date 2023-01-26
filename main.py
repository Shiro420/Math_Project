from tkinter import *

root = Tk()
root.title("main_window")
root.geometry("400x400")
root.resizable(width=0, height=0)


def search(event):
    if clicked.get() == 'Linear':
        fenster = Tk()
        fenster.title("naja")
        fenster.geometry("400x400")
        fenster.resizable(width=0, height=0)




funktionen = ["Linear", "Qudratisch", "Ganzrationale", "Trigonometrische", "Exponential","Einstieg-Differenzialrechnung", "Kurvendiskussion", "Integralrechnung"]
clicked = StringVar()
clicked.set(funktionen[0])

OM = OptionMenu(root, clicked, *funktionen,command=search)
OM.pack(padx=10)


root.mainloop()
