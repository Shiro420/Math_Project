from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

Anmeldung = Tk()
Anmeldung.title("Login")
Anmeldung.geometry("400x400")
Anmeldung.resizable(width=0, height=0)

def Funktion():
    Anmeldung.destroy()
    root = Tk()
    root.title("main_window")
    root.geometry("900x900")
    root.resizable(width=0, height=0)

    def search(event):
        fenster = Tk()
        fenster.title("Window")
        fenster.geometry("900x900")
        fenster.resizable(width=0, height=0)

        if clicked.get() == 'Linear':

            y_label = Label(fenster,text="y Achse")
            y_entry = Entry(fenster)
            x_label = Label(fenster,text="x Achse")
            x_entry = Entry(fenster)
            von_label = Label(fenster, text="anfang: ")
            von_entry = Entry(fenster)
            bis_label = Label(fenster, text="ende: ")
            bis_entry = Entry(fenster)
            m_label = Label(fenster, text=" m: ")
            m_entry = Entry(fenster)
            b_label = Label(fenster, text=" b: ")
            b_entry = Entry(fenster)

            def rechnen():
                von = von_entry.get()
                von = float(von)
                bis = bis_entry.get()
                bis = float(bis)
                m = m_entry.get()
                m = float(m)
                b = b_entry.get()
                b = float(b)

                fig = plt.Figure(figsize=(10, 20), dpi=100)
                ax = fig.add_subplot()

                ax.set_xlim([von,bis])
                ax.set_ylim([von,bis])

                x = np.linspace(von, bis, 100)
                y = m * x + b

                ax.set_xlabel(x_entry.get())
                ax.set_ylabel(y_entry.get())
                ax.plot(x, y, 'r', label='f(x)='+ m_entry.get()+'*x+'+ b_entry.get())
                ax.legend(loc='upper left')
                ax.set_title('Funktion f(x)=m*x+b')
                fig.set_size_inches(5, 5)

                cv = FigureCanvasTkAgg(fig, master=fenster)
                cv.draw()
                cv.get_tk_widget().grid(row=7, column=0)

            def bsp():
                fig = plt.Figure(figsize=(10, 20), dpi=100)
                ax = fig.add_subplot()

                ax.set_xlim([-5, 5])
                ax.set_ylim([-5, 5])

                x = np.linspace(-5, 5, 100)
                y = 1 * x + 1

                ax.set_xlabel("x")
                ax.set_ylabel("y")
                ax.plot(x, y,  label='f(x)=1*x+1')
                ax.legend(loc='upper left')
                ax.set_title('Funktion f(x)=m*x+b')
                fig.set_size_inches(5, 5)
                cv = FigureCanvasTkAgg(fig, master=fenster)
                cv.draw()
                cv.get_tk_widget().grid(row=7, column=0)

            von_label.grid(row=0, column=0)
            von_entry.grid(row=0, column=1)
            bis_label.grid(row=1, column=0)
            bis_entry.grid(row=1, column=1)
            m_label.grid(row=2,column=0)
            m_entry.grid(row=2,column=1)
            b_label.grid(row=3,column=0)
            b_entry.grid(row=3,column=1)
            y_label.grid(row=4,column=0)
            y_entry.grid(row=4,column=1)
            x_label.grid(row=5,column=0)
            x_entry.grid(row=5,column=1)

            Button(fenster, command=rechnen, text="Anzeigen").grid(row=6,column=1)
            Button(fenster, command=bsp, text="Beispiel").grid(row=0, column=4)
            Button(fenster,text="close",command=fenster.destroy).grid(row=0,column=9)

        elif clicked.get() == "Qudratisch":
            #Noramalfunkion
            ya_label = Label(fenster, text="y Achse")
            ya_entry = Entry(fenster)
            xa_label = Label(fenster, text="x Achse")
            xa_entry = Entry(fenster)
            von_label = Label(fenster, text="anfang: ")
            von_entry = Entry(fenster)
            bis_label = Label(fenster, text="ende: ")
            bis_entry = Entry(fenster)
            a_label = Label(fenster, text="a: ")
            a_entry = Entry(fenster)
            b_label = Label(fenster, text="b: ")
            b_entry = Entry(fenster)
            c_label = Label(fenster, text="c: ")
            c_entry = Entry(fenster)

            def rechnen():
                von = von_entry.get()
                von = float(von)
                bis = bis_entry.get()
                bis = float(bis)
                a = a_entry.get()
                a = float(a)
                b = b_entry.get()
                b = float(b)
                c = b_entry.get()
                c = float(c)

                fig = plt.Figure(figsize=(10, 20), dpi=100)
                ax = fig.add_subplot()

                ax.set_xlim([von,bis])
                ax.set_ylim([von,bis])

                x = np.linspace(von,bis,100)
                y = a * x**2 + b * x + c

                ax.set_xlabel(x_entry.get())
                ax.set_ylabel(y_entry.get())
                ax.set_title('Funktion $ax^2 + bx + c$')
                fig.set_size_inches(5, 5)
                ax.plot(x,y,'r',label='f(x)='+a_entry.get() + 'x^2'+'+' + b_entry.get() +'x'+'+'+ c_entry.get())
                ax.legend(loc='upper left')
                cv = FigureCanvasTkAgg(fig, master=fenster)
                cv.draw()
                cv.get_tk_widget().grid(row=10, column=0)


            #normalfunktion
            von_label.grid(row=0, column=0)
            von_entry.grid(row=0, column=1)
            bis_label.grid(row=1, column=0)
            bis_entry.grid(row=1, column=1)
            a_label.grid(row=2, column=0)
            a_entry.grid(row=2, column=1)
            b_label.grid(row=3, column=0)
            b_entry.grid(row=3, column=1)
            c_label.grid(row=4, column=0)
            c_entry.grid(row=4, column=1)
            ya_label.grid(row=5, column=0)
            ya_entry.grid(row=5, column=1)
            xa_label.grid(row=6, column=0)
            xa_entry.grid(row=6, column=1)


            Button(fenster, command=rechnen, text="Anzeigen").grid(row=7, column=1)
            Button(fenster, text="close", command=fenster.destroy).grid(row=0, column=8)

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

    label1 = Label(root,text="Funktionen Auswahl")
    label1.grid(row=0,column=0)

    OM = OptionMenu(root, clicked, *funktionen,command=search)
    OM.grid(row=1,column=0)

    root.mainloop()

def inpAnmeldung():
    current_input = Entry1.get()
    current_input2 = Entry2.get()
    print(current_input, current_input2)

Label(Anmeldung, text="Benutzername").grid(row=1,column=9)
Entry1= Entry(Anmeldung).grid(row=2, column=9)

Label(Anmeldung,text="Passwort").grid(row=3,column=9)
Entry2= Entry(Anmeldung).grid(row=4,column=9)

Button(Anmeldung,text="Login",command=Funktion).grid(row=0,column=9)

Anmeldung.mainloop()
