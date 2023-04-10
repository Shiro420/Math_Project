
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math as math
from database import *

login = Tk()
login.title("Login")
login.geometry("400x400")
login.resizable(width=0, height=0)

def input_Anmeldung():
    input = Benutzername_login.get()
    input2 = Passwort_login.get()
    print(input, input2)
    root = Tk()
    def OkButtonClick():
        Error.destroy()

    if anmeldung(input,input2):
        login.destroy()

        root.title("main_window")
        root.geometry("400x400")
        root.resizable(width=0, height=0)


    else:
        Error = Tk()
        Error.title("Error")
        Error.geometry("500x50")
        Error.resizable(width=0, height=0)
        Button(Error, text="Ok", command=OkButtonClick).grid(row=1,column=0)
        Label(Error,text="Dieser Account existiert nicht! Bitte versuchen sie es erneut").grid(row=0,column=0)

    def search(event):
        fenster = Tk()
        fenster.title("Window")
        fenster.geometry("900x900")
        fenster.resizable(width=0, height=0)

        if clicked.get() == 'Linear':

            y_label = Label(fenster, text="y Achse")
            y_entry = Entry(fenster)
            x_label = Label(fenster, text="x Achse")
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

                ax.set_xlim([von, bis])
                ax.set_ylim([von, bis])

                x = np.linspace(von, bis, 100)
                y = m * x + b
                # Nullstelle
                try:
                    x1 =(-b/m)
                    y1 = 0
                    x1_1 = str(x1)
                    ax.scatter(x1, y1, label="Nullstelle " + x1_1)
                except:

                    ax.set_xlim([von, bis])
                    ax.set_ylim([von, bis])

                    x = np.linspace(von, bis, 100)
                    y = m * x + b

                ax.set_xlabel(x_entry.get())
                ax.set_ylabel(y_entry.get())
                ax.plot(x, y, 'r', label='f(x)=' + m_entry.get() + '*x+' + b_entry.get())
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
                #Nullstelle

                x1=-1
                y1=0
                x1_1=str(x1)

                ax.scatter(x1,y1,label="Nullstelle "+x1_1)
                ax.set_xlabel("x")
                ax.set_ylabel("y")
                ax.plot(x, y, label='f(x)=1*x+1')
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
            m_label.grid(row=2, column=0)
            m_entry.grid(row=2, column=1)
            b_label.grid(row=3, column=0)
            b_entry.grid(row=3, column=1)
            y_label.grid(row=4, column=0)
            y_entry.grid(row=4, column=1)
            x_label.grid(row=5, column=0)
            x_entry.grid(row=5, column=1)

            Button(fenster, command=rechnen, text="Anzeigen").grid(row=6, column=1)
            Button(fenster, command=bsp, text="Beispiel").grid(row=0, column=4)
            Button(fenster, text="Schließen", command=fenster.destroy).grid(row=0, column=9)

        elif clicked.get() == "Qudratisch":
            # Noramalfunkion
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

                ax.set_xlim([von, bis])
                ax.set_ylim([von, bis])

                x = np.linspace(von, bis, 100)
                y = a * x ** 2 + b * x + c
                #Nullstellen
                try:
                    b1=b/a
                    c1=c/a

                    n1 =-b1/2 +math.sqrt((b1/2)**2-(c1))
                    n2 =-b1/2 -math.sqrt((b1/2)**2-(c1))

                    yy=[0,0]
                    xx=[n1,n2]

                except:

                    ax.set_xlim([von, bis])
                    ax.set_ylim([von, bis])

                    x = np.linspace(von, bis, 100)
                    y = a * x ** 2 + b * x + c
                try:
                 n1_1 = str(n1)
                 n2_1 = str(n2)
                 ax.scatter(xx, yy,label="Nullstelle1 " + n1_1+" und "+"Nullstelle2 " + n2_1)
                except:
                 ax.plot(x,y,"b",label="Keine Nullstellen")

                ax.set_xlabel(xa_entry.get())
                ax.set_ylabel(ya_entry.get())
                ax.set_title('Funktion $ax^2 + bx + c$')
                fig.set_size_inches(7, 7)
                ax.plot(x, y, 'r',label='f(x)=' + a_entry.get() + 'x^2' + '+' + b_entry.get() + 'x' + '+' + c_entry.get())
                ax.legend(loc='upper left')
                cv = FigureCanvasTkAgg(fig, master=fenster)
                cv.draw()
                cv.get_tk_widget().grid(row=10, column=5)

            def bsp():
                fig = plt.Figure(figsize=(10, 20), dpi=100)
                ax = fig.add_subplot()

                ax.set_xlim([-10, 10])
                ax.set_ylim([-10, 10])

                x = np.linspace(-10, 10, 100)
                y = 1 * x ** 2 + -4 * x + 2

                # Nullstellen

                n1 = 4 / 2 + math.sqrt((-4 / 2) ** 2 - (2))
                n2 = 4 / 2 - math.sqrt((-4 / 2) ** 2 - (2))
                n1_1 = str(n1)
                n2_1 = str(n2)
                yy = [0, 0]
                xx = [n1, n2]

                ax.scatter(xx, yy,label="Nullstelle1 " + n1_1+" und "+"Nullstelle2 " + n2_1)
                ax.set_xlabel(xa_entry.get())
                ax.set_ylabel(ya_entry.get())
                ax.set_title('Funktion $ax^2 + bx + c$')
                fig.set_size_inches(7, 7)
                ax.plot(x, y, 'r',label="f(x)=x^2-4x+2")
                ax.legend(loc='upper left')
                cv = FigureCanvasTkAgg(fig, master=fenster)
                cv.draw()
                cv.get_tk_widget().grid(row=10, column=5)

            # normalfunktion
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

            Button(fenster, command=rechnen, text="Anzeigen").grid(row=7, column=0)
            Button(fenster, text="Schließen", command=fenster.destroy).grid(row=8, column=0)
            Button(fenster, command=bsp, text="Beispiel").grid(row=7, column=1)

        if clicked.get() == 'Ganzrationale':

            von_label = Label(fenster, text="anfang: ")
            von_entry = Entry(fenster)
            bis_label = Label(fenster, text="ende: ")
            bis_entry = Entry(fenster)

            def rechnen():
                von = von_entry.get()
                von = float(von)
                bis = bis_entry.get()
                bis = float(bis)

                fig = plt.Figure(figsize=(10, 20), dpi=100)
                ax = fig.add_subplot()


                ax.set_xlim([von, bis])
                ax.set_ylim([von, bis])

                x = np.linspace(von, bis, 100)
                y = 1*x+1
                #Nullstellen

                ax.set_xlim([-10, 10])
                ax.set_ylim([-10, 10])
                ax.scatter()
                ax.set_xlabel(xa_entry.get())
                ax.set_ylabel(ya_entry.get())
                ax.set_title()
                fig.set_size_inches(7, 7)
                ax.plot(x,y)
                ax.legend(loc='upper left')
                cv = FigureCanvasTkAgg(fig, master=fenster)
                cv.draw()
                cv.get_tk_widget().grid(row=10, column=5)

            #def bsp():

            von_label.grid(row=0, column=0)
            von_entry.grid(row=0, column=1)
            bis_label.grid(row=1, column=0)
            bis_entry.grid(row=1, column=1)

            Button(fenster, command=rechnen, text="Anzeigen").grid(row=3, column=0)
            Button(fenster, text="Schließen", command=fenster.destroy).grid(row=2, column=0)
            #Button(fenster, command=bsp, text="Beispeil").grid(row=0, column=0)

        if clicked.get() == 'Trigonometrische Funktionen':
            a_label = Label(fenster, text="Amplitude:")
            a_entry = Entry(fenster)
            t_label = Label(fenster, text="Frequenz:")
            t_entry = Entry(fenster)
            ph_label = Label(fenster, text="Phase:")
            ph_entry = Entry(fenster)
            function_type_var = StringVar(value='sin')
            sin_radio = Radiobutton(fenster, text='Sinus', variable=function_type_var, value='sin')
            cos_radio = Radiobutton(fenster, text='Cosinus', variable=function_type_var, value='cos')
            tan_radio = Radiobutton(fenster, text='Tangens', variable=function_type_var, value='tan')

            fig = plt.Figure(figsize=(10, 10), dpi=100)
            ax = fig.add_subplot()

            cv = FigureCanvasTkAgg(fig, master=fenster)
            cv.draw()

            def rechnen():

                a= a_entry.get()
                a = float(a)
                t = t_entry.get()
                t = float(t)
                ph = ph_entry.get()
                ph = float(ph)

                x = np.linspace(0, 2 * np.pi, 1000)
                if function_type_var == 'sin':
                    y = a * np.sin(t * x + ph)
                    title = 'Sinusfunktion'
                elif function_type_var == 'cos':
                    y = a * np.cos(t * x + ph)
                    title = 'Cosinusfunktion'
                elif function_type_var == 'tan':
                    y = a * np.tan(t * x + ph)
                    title = 'Tangensfunktion'


                ax.plot(x, y)
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_title(title)
                cv.draw()

                cv.get_tk_widget().grid(row=10, column=5)

            a_label.grid(row=0,column=0)
            a_entry.grid(row=0,column=1)
            t_label.grid(row=1,column=0)
            t_entry.grid(row=1,column=1)
            ph_label.grid(row=2,column=0)
            ph_entry.grid(row=2,column=1)
            sin_radio.grid(row=3,column=0)
            cos_radio.grid(row=4,column=0)
            tan_radio.grid(row=5,column=0)
            Button(fenster, command=rechnen, text="Anzeigen").grid(row=0, column=4)

    label1 = Label(root, text="Funktionen Auswahl")
    label1.grid(row=0, column=0)

    clicked = StringVar(root)
    clicked.set(clicked)

    OM = OptionMenu(root, clicked, "Linear", "Qudratisch","Ganzrationale","Trigonometrische Funktionen", command=search)
    OM.grid(row=1, column=0)

    def Logout():
        root.destroy()
        login.deiconify()

    Button(root, text="Abmelden", command=Logout).grid(row=0, column=3)
    root.mainloop()

def Logout():
    login.destroy()

def Register():
    Registerfenster = Tk()
    Registerfenster.title("Registration")
    def Regristierungs_input():
        new_Benutzername = Benutzername_input.get()
        new_Passwort = Passwort_input.get()
        new_Passwort_bestägung = Passwort_bestätigung_input.get()

        if new_Passwort == new_Passwort_bestägung and new_Benutzername != "":
            if regristierungs_prüfen(new_Benutzername):
                print(new_Benutzername,new_Passwort ,new_Passwort_bestägung)
                NewAcc(Benutzername_input.get(),Passwort_input.get())
                Ausgabe()
                Registerfenster.destroy()
            else:
                def OkButtonClick():
                    Error.destroy()
                Error = Tk()
                Error.title("Error")
                Error.geometry("500x50")
                Error.resizable(width=0, height=0)
                Button(Error, text="Ok", command=OkButtonClick).grid(row=0,column=0)
                Label(Error,text="Dieser Benutzername existiert bereits! Bitte wählen Sie einen anderen!").grid(row=1,column=0)

        else:
            print("Das Passwort und die Bestätigung des Passworts stimmen nicht überein")
            RegisterFail = Tk()
            RegisterFail.title("Error")
            RegisterFail.geometry("500x50")
            RegisterFail.resizable(width=0, height=0)

            def OkButtonClick():
                    RegisterFail.destroy()

            Button(RegisterFail, text="Ok", command=OkButtonClick).grid(row=0,column=0)
            Label(RegisterFail,text="Das Passwort und die Bestätigung des Passwortes stimmen nicht überein!").grid(row=1,column=0)

    new_Benutzername = Label(Registerfenster, text="Benutzername")
    Benutzername_input = Entry(Registerfenster, bd=5, width=40)
    new_Passwort = Label(Registerfenster, text="Passwort")
    Passwort_input = Entry(Registerfenster, bd=5, width=40)
    new_Passwort_bestägung = Label(Registerfenster, text="Bestätigung des Passworts")
    Passwort_bestätigung_input = Entry(Registerfenster, bd=5, width=40)

    Button(Registerfenster, text="Registrieren", command=Regristierungs_input).grid(row=6, column=0)

    new_Benutzername.grid(row=0, column=0)
    Benutzername_input.grid(row=0, column=1)
    new_Passwort.grid(row=1, column=0)
    Passwort_input.grid(row=1, column=1)
    new_Passwort_bestägung.grid(row=2, column=0)
    Passwort_bestätigung_input.grid(row=2, column=1)

Label(login, text="Benutzername").grid(row=1, column=0)
Benutzername_login = Entry(login)
Benutzername_login.grid(row=1, column=1)

Label(login, text="Passwort").grid(row=2, column=0)
Passwort_login = Entry(login)
Passwort_login.grid(row=2, column=1)

Button(login,text="Abmelden", command=Logout).grid(row=5,column=1)
Button(login, text="Anmelden", command=input_Anmeldung).grid(row=0, column=1)
Button(login, text="Registrieren", command=Register).grid(row=0,column=0)

login.mainloop()
