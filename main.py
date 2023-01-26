from tkinter import *
from tkinter import ttk

root = Tk()
root.title("main_window")
root.geometry("400x400")
root.resizable(width=0, height=0)


def search(selection):
    fenster = Tk()
    fenster.title("naja")
    fenster.geometry("400x400")
    fenster.resizable(width=0, height=0)
   


funktionen = ("Linear", "Qudratisch", "Ganzrationale", "Trigonometrische", "Exponential",
              "Einstieg-Differenzialrechnung", "Kurvendiskussion", "Integralrechnung")


l1 = Label(root, text="Funktionenen auswahl")
cmb = ttk.Combobox(root, value=funktionen, width=15)
cmb.set('Funktionen')
cmb.bind("<<ComboboxSelected>>",search)

l1.grid(row=0, column=0)
cmb.grid(row=1, column=0)
root.mainloop()

