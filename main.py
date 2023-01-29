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
        root.destroy()
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

            ax.set_xticks(range(-10, 10, 1))
            ax.set_yticks(range(-10, 10, 1))
            ax.set_xlim([von,bis])
            ax.set_ylim([von,bis])

            ax.spines['top'].set_color('none')
            ax.spines['bottom'].set_position('zero')
            ax.spines['left'].set_position('zero')
            ax.spines['right'].set_color('none')

            x = np.linspace(-5, 5, 100)
            y = m * x + b

            plt.plot(x,y)
            plt.title('Linear')
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
        
        Button(fenster, command=rechnen, text="Anzeigen").grid(row=4,column=1)


    elif clicked.get() == "Qudratisch" :
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

            x = np.arange(-100, 100, 0.1)
            y = a * x ** 2 + b * x + c
            
            plt.xlabel('x-Werte')
            plt.ylabel('y-Werte')
            plt.plot(x, y)
            plt.title('Quadratisch')
            plt.grid()
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

        Button(fenster, command=rechnen, text="Anzeigen").grid(row=5, column=1)

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
