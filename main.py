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
    Auswahl = cmb.get()
    if Auswahl == "linear":
        butoon1 = Button(fenster, text="Ausführen", )
        butoon2 = Button(fenster, text="Beispiele", )
        butoon3 = Button(fenster, text="Zoom-in", )
        butoon4 = Button(fenster, text="Zoom-out", )
        ytext = Entry(fenster, bd=5, width=7)
        xtext = Entry(fenster, bd=5, width=7)
        btext = Entry(fenster, bd=5, width=7)
        mtext = Entry(fenster, bd=5, width=7)
        xbeschriftung = Entry(fenster, bd=5, width=7)
        ybeschriftung = Entry(fenster, bd=5, width=7)

        ytext.pack()
        xtext.pack()
        btext.pack()
        mtext.pack()
        xbeschriftung.pack()
        ybeschriftung.pack()
        butoon4.pack()
        butoon3.pack()
        butoon2.pack()
        butoon1.pack()

        ytext.place(relx=2.1, rely=7.8), xtext.place(relx=4.1, rely=6.8)
    elif Auswahl == "Qudratisch":


    elif Auswahl == "Ganzrationale":


    elif Auswahl == "Trigonometrische":


    elif Auswahl == "Exponentail":


    elif Auswahl == "Einstig-Defferenzilrechnung":


    elif Auswahl == "Kurvendiskussion":


    elif Auswahl == "Integralrechnung":

    return


funktionen = ("Linear", "Qudratisch", "Ganzrationale", "Trigonometrische", "Exponential",
              "Einstieg-Differenzialrechnung", "Kurvendiskussion", "Integralrechnung")


l1 = Label(root, text="Funktionenen auswahl")
cmb = ttk.Combobox(root, value=funktionen, width=15)
cmb.set('Funktionen')
cmb.bind("<<ComboboxSelected>>",search)

l1.grid(row=0, column=0)
cmb.grid(row=1, column=0)
root.mainloop()

