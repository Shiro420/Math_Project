from tkinter import *
from tkinter import ttk

root = Tk()
root.title("main_window")
root.geometry("400x400")
root.resizable(width=0, height=0)

def search(selection):
    fenster = Tk()
    fenster.title("main window")
    fenster.geometry("400x400")
    fenster.resizable(width=0, height=0)


    if cmb.get() == "linear":
        
    elif cmb.get() == "Qudratisch":


    elif cmb.get() == "Ganzrationale":


    elif cmb.get() == "Trigonometrische":


    elif cmb.get() == "Exponentail":


    elif cmb.get() == "Einstig-Defferenzilrechnung":


    elif cmb.get() == "Kurvendiskussion":


    elif cmb.get() == "Integralrechnung":

    return


funktionen = ("Linear", "Qudratisch", "Ganzrationale", "Trigonometrische", "Exponential",
              "Einstieg-Differenzialrechnung", "Kurvendiskussion", "Integralrechnung")

l1 = Label(root, text="Funktionenen auswahl")
cmb = ttk.Combobox(root, value=funktionen, width=15)
cmb.set('Funktionen')
button1 = Button(root, text="Ausführen",command=search(selection=funktionen))

l1.grid(row=0, column=0)
button1.grid(row=1,column=1)
cmb.grid(row=1, column=0)
root.mainloop()
