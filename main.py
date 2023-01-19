from tkinter import *

root = Tk()
root.title("log in")
root.geometry("400x400")
root.resizable(width=0, height=0)

def login ():
    lnfenster = Tk()
    lnfenster.title("log in Fenster")
    lnfenster.geometry("600x600")
    lnfenster.resizable(width=0,height=0)
    Funktionen = StringVar(lnfenster)
    Funktionen.set("Funktionen")

    def show(selection):
        Auswahl = selection
        fenster = Tk()
        fenster.geometry("600x600")
        fenster.resizable(width=0,height=0)
        fenster.title(Auswahl)

        if Auswahl == "Linearefunktion":
            butoon1 = Button(fenster, text="Ausführen", )
            ytext = Entry(fenster, bd=5, width=7)
            xtext = Entry(fenster, bd=5, width=7)
            btext = Entry(fenster, bd=5, width=7)
            mtext = Entry(fenster, bd=5, width=7)

    drop = OptionMenu(root,"Lineare-Funktion" , "Quadratische-Funktion" ,
                      "Ganzrationale-Funktionen" ,"Trigonometrische-Funktionen" , "Exponential-Funktionen" ,
                      "Einstieg-Differenzialrechnung" , "Kurvendiskussion", "Integralrechnung",)
    drop.pack()
    drop.place(relx=0.0, rely=0.0)

root.mainloop()
