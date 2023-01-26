from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


root = Tk()
root.title("main_window")
root.geometry("400x400")
root.resizable(width=0, height=0)


def search(event):
    fenster = Tk()
    fenster.title("Window")
    fenster.geometry("500x500")
    fenster.resizable(width=0, height=0)
    if clicked.get() == 'Linear':

        von_label = Label(fenster, text="anfang: ")
        von_entry = Entry(fenster)
        bis_label = Label(fenster, text="ende: ")
        bis_entry = Entry(fenster)
        m_label = Label(fenster, text="m: ")
        m_entry = Entry(fenster)
        b_label = Label(fenster, text="b: ")
        b_entry = Entry(fenster)
        x_achse_label = Label(fenster, text="x-Achsenbeschriftung:")
        x_achse_entry = Entry(fenster)
        y_achse_label = Label(fenster, text="y-Achsenbeschriftung:")
        y_achse_entry = Entry(fenster)

        fig = plt.Figure(figsize=(10, 10))

        def rechnen()  :

            von = float(von_entry.get())
            bis = float(bis_entry.get())
            m = float(m_entry.get())
            b = float(b_entry.get())
            rg = np.arange(von, bis, 0.2)

        von_label.grid(row=0,column=0)
        von_entry.grid(row=0,column=1)
        bis_label.grid(row=1,column=0)
        bis_entry.grid(row=1,column=1)
        m_label.grid(row=2,column=0)
        m_entry.grid(row=2,column=1)
        b_label.grid(row=3,column=0)
        b_entry.grid(row=3,column=1)
        x_achse_label.grid(row=4,column=0)
        x_achse_entry.grid(row=4,column=1)
        y_achse_label.grid(row=5,column=0)
        y_achse_entry.grid(row=5,column=1)

        Button(fenster, command=rechnen, text="Anzeigen").grid(row=6,column=1)

    elif clicked.get() == "Qudratisch" :
        von_label = Label(fenster, text="anfang: ")
        von_entry = Entry(fenster)
        bis_label = Label(fenster, text="ende: ")
        bis_entry = Entry(fenster)

        von_label.grid(row=0, column=0)
        von_entry.grid(row=0, column=1)
        bis_label.grid(row=1, column=0)
        bis_entry.grid(row=1, column=1)
    elif clicked.get() == "Ganzrationale" :
        von_label = Label(fenster, text="anfang: ")
        von_entry = Entry(fenster)
        bis_label = Label(fenster, text="ende: ")
        bis_entry = Entry(fenster)

        von_label.grid(row=0, column=0)
        von_entry.grid(row=0, column=1)
        bis_label.grid(row=1, column=0)
        bis_entry.grid(row=1, column=1)
    elif clicked.get() == "Trigonometrische" :
        von_label = Label(fenster, text="anfang: ")
        von_entry = Entry(fenster)
        bis_label = Label(fenster, text="ende: ")
        bis_entry = Entry(fenster)

        von_label.grid(row=0, column=0)
        von_entry.grid(row=0, column=1)
        bis_label.grid(row=1, column=0)
        bis_entry.grid(row=1, column=1)
    elif clicked.get() =="Exponential" :
        von_label = Label(fenster, text="anfang: ")
        von_entry = Entry(fenster)
        bis_label = Label(fenster, text="ende: ")
        bis_entry = Entry(fenster)

        von_label.grid(row=0, column=0)
        von_entry.grid(row=0, column=1)
        bis_label.grid(row=1, column=0)
        bis_entry.grid(row=1, column=1)
    elif clicked.get() =="Einstieg-Differenzialrechnung":
        von_label = Label(fenster, text="anfang: ")
        von_entry = Entry(fenster)
        bis_label = Label(fenster, text="ende: ")
        bis_entry = Entry(fenster)

        von_label.grid(row=0, column=0)
        von_entry.grid(row=0, column=1)
        bis_label.grid(row=1, column=0)
        bis_entry.grid(row=1, column=1)
    elif clicked.get() =="Kurvendiskussion":
        von_label = Label(fenster, text="anfang: ")
        von_entry = Entry(fenster)
        bis_label = Label(fenster, text="ende: ")
        bis_entry = Entry(fenster)

        von_label.grid(row=0, column=0)
        von_entry.grid(row=0, column=1)
        bis_label.grid(row=1, column=0)
        bis_entry.grid(row=1, column=1)
    elif clicked.get() == "Integralrechnung":
        von_label = Label(fenster, text="anfang: ")
        von_entry = Entry(fenster)
        bis_label = Label(fenster, text="ende: ")
        bis_entry = Entry(fenster)

        von_label.grid(row=0, column=0)
        von_entry.grid(row=0, column=1)
        bis_label.grid(row=1, column=0)
        bis_entry.grid(row=1, column=1)
funktionen = ["Linear", "Qudratisch", "Ganzrationale", "Trigonometrische", "Exponential","Einstieg-Differenzialrechnung", "Kurvendiskussion", "Integralrechnung"]

clicked = StringVar()
clicked.set(funktionen[0])

OM = OptionMenu(root, clicked, *funktionen,command=search)
OM.pack(padx=10)

root.mainloop()
