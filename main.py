from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

Anmeldung = Tk()
Anmeldung.title("Login")
Anmeldung.geometry("400x400")
Anmeldung.resizable(width=0, height=0)

def Funktion():
    Anmeldung.destroy()
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

                ax = plt.gca()
                plt.gca().set_aspect('equal')

                ax.set_xlim([von,bis])
                ax.set_ylim([von,bis])

                x = np.linspace(-5, 5, 100)
                y = m * x + b

                plt.xlabel(x_entry.get())
                plt.ylabel(y_entry.get())
                plt.plot(x,y,'r')
                plt.title('Linear')
                plt.grid()
                plt.show()

            def bsp():

                ax = plt.gca()
                plt.gca().set_aspect('equal')

                ax.set_xlim([-10, 10])
                ax.set_ylim([-10,10])


                x = np.linspace(-5, 5, 100)
                y = 2 * x + 1

                plt.plot(x, y, 'r', label='2*x+1')
                plt.title('Linearfunktion')
                plt.legend(loc='upper left')
                plt.grid()
                plt.show()

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

        elif clicked.get() == "Qudratisch" :
            root.destroy()
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
            Alabel = Label(fenster,text="a")
            Aentry = Entry(fenster)
            x1label = Label(fenster,text="x")
            x1entry = Entry(fenster)
            xSlabel = Label(fenster,text="xS")
            xSentry = Entry(fenster)
            ySlabel = Label(fenster,text="yS")
            ySentry = Entry(fenster)

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

                ax = plt.gca()
                plt.gca().set_aspect('equal')

                ax.set_xlim([von,bis])
                ax.set_ylim([von,bis])

                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                x = np.linspace(-5, 5, 100)
                y = a * x**2 + b * x + c

                plt.xlabel(x_entry.get())
                plt.ylabel(y_entry.get())
                plt.title('Funktion $ax^2 + bx + c$')
                plt.plot(x, y)
                plt.show()
            def scheitelpunkt():
                von = von_entry.get()
                von = float(von)
                bis = bis_entry.get()
                bis = float(bis)
                A = Aentry.get()
                A = float(A)
                x1 = x1entry.get()
                x1 = float(x1)
                xS = xSentry.get()
                xS = float(xS)
                yS = ySentry.get()
                yS = float(yS)

                ax = plt.gca()
                plt.gca().set_aspect('equal')

                ax.set_xlim([von, bis])
                ax.set_ylim([von, bis])

                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_position('zero')
                ax.spines['left'].set_position('zero')
                ax.spines['right'].set_color('none')

                x = np.linspace(-5, 5, 100)
                y = A(x1 - xS)**2+yS

                plt.xlabel(x_entry.get())
                plt.ylabel(y_entry.get())
                plt.title('Funktion $ax^2 + bx + c$')
                plt.plot(x, y)
                plt.show()

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

            Alabel.grid(row=0,column=6)
            Aentry.grid(row=0,column=7)
            x1label.grid(row=1,column=6)
            x1entry.grid(row=1,column=7)
            xSlabel.grid(row=2,column=6)
            xSentry.grid(row=2,column=7)
            ySlabel.grid(row=3,column=6)
            ySentry.grid(row=3,column=7)

            Button(fenster, command=rechnen, text="Anzeigen").grid(row=7, column=1)
            Button(fenster, command=scheitelpunkt(), text="Anzeigen").grid(row=4, column=7)

        elif clicked.get() == "Ganzrationale" :
            root.destroy()
            von_label = Label(fenster, text="anfang: ")
            von_entry = Entry(fenster)
            bis_label = Label(fenster, text="ende: ")
            bis_entry = Entry(fenster)

            von_label.grid(row=0, column=0)
            von_entry.grid(row=0, column=1)
            bis_label.grid(row=1, column=0)
            bis_entry.grid(row=1, column=1)
        elif clicked.get() == "Trigonometrische" :
            root.destroy()
            von_label = Label(fenster, text="anfang: ")
            von_entry = Entry(fenster)
            bis_label = Label(fenster, text="ende: ")
            bis_entry = Entry(fenster)

            von_label.grid(row=0, column=0)
            von_entry.grid(row=0, column=1)
            bis_label.grid(row=1, column=0)
            bis_entry.grid(row=1, column=1)
        elif clicked.get() =="Exponential" :
            root.destroy()
            von_label = Label(fenster, text="anfang: ")
            von_entry = Entry(fenster)
            bis_label = Label(fenster, text="ende: ")
            bis_entry = Entry(fenster)

            von_label.grid(row=0, column=0)
            von_entry.grid(row=0, column=1)
            bis_label.grid(row=1, column=0)
            bis_entry.grid(row=1, column=1)
        elif clicked.get() =="Einstieg-Differenzialrechnung":
            root.destroy()
            von_label = Label(fenster, text="anfang: ")
            von_entry = Entry(fenster)
            bis_label = Label(fenster, text="ende: ")
            bis_entry = Entry(fenster)

            von_label.grid(row=0, column=0)
            von_entry.grid(row=0, column=1)
            bis_label.grid(row=1, column=0)
            bis_entry.grid(row=1, column=1)
        elif clicked.get() =="Kurvendiskussion":
            root.destroy()
            von_label = Label(fenster, text="anfang: ")
            von_entry = Entry(fenster)
            bis_label = Label(fenster, text="ende: ")
            bis_entry = Entry(fenster)

            von_label.grid(row=0, column=0)
            von_entry.grid(row=0, column=1)
            bis_label.grid(row=1, column=0)
            bis_entry.grid(row=1, column=1)
        elif clicked.get() == "Integralrechnung":
            root.destroy()
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
Label(Anmeldung, text="Benutzername").grid(row=1,column=9)
Entry(Anmeldung).grid(row=2, column=9)
Label(Anmeldung,text="Passwort").grid(row=3,column=9)
Entry(Anmeldung).grid(row=4,column=9)
Button(Anmeldung,text="Login",command=Funktion).grid(row=0,column=9)
Anmeldung.mainloop()
