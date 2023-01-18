import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *

root = Tk()

def base_Tk(size="900x600", name="") -> Tk:
    root.geometry(size)
    root.title(name)
    return root

def lineare_funktion():

    von_label = Label(root, text="anfang: ")
    von_entry = Entry(root)

    bis_label = Label(root, text="ende: ")
    bis_entry = Entry(root)

    m_Label = Label(root, text="m").grid(row=0)
    m_entry = Entry(root)

    b_label = Label(root,text="b").grid(row=1)
    b_entry = Entry(root)

    x_label = Label(root, text="x").grid(row=2)
    x_entry = Entry(root)

    y_label = Label(root, text="y").grid(row=3)
    y_entry = Entry(root)

    x_achse_label = Label(root, text="x_Achse")
    x_achse_entry = Entry(root)

    y_achse_label = Label(root, text="y_achse")
    y_achse_entry = Entry(root)

    fig = plt.Figure(figsize=(10, 10), dpi=100)
    ax = fig.add_subplot()
    cv = FigureCanvasTkAgg(fig, master=root)
    cv.draw()

    def recchnen():
        von = float(von_entry.get())
        bis = float(bis_entry.get())
        m = float(m_entry.get())
        b = float(b_entry.get())


def Menu() :
    
    menu = tk.menu(root,tearoff = 0)
    root.config(menu = menu)
    menu.add_cascade(label = "lineare",command = lineare_funktion)
    menu.add_cascade(label = "Quadratische")
    menu.add_cascade(label = "Ganzrationale")
    menu.add_command(label="Trigonometrische")
    menu.add_command(label="Exponential")
    menu.add_command(label="Differenzial")
    menu.add_command(label="Kurvendiskusion")
    menu.add_command(label="Integralrechnung")
    
    
root.mainloop








