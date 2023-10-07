import tkinter
from tkinter import messagebox

import IOT

def Control_Hardware():
    IOT.HW_control()

def Control_Software():
    IOT.SW_control()

def About():
    m = tkinter.Tk(className='About')
    m.geometry('260x170')
    l1 = tkinter.Label(m, text = "Raspberry Pi Project to control software \nand hardware using hand gestures.", bg = "#040c5c",bd=5, fg = "#f77c00", font = ('Helvetica',11))
    l2 = tkinter.Label(m, width=260, text = "Developed by", bg = "#040c5c", fg = "#f77c00", font = ('Helvetica',14, 'bold'))
    l3 = tkinter.Label(m, width=260, text = "Aniket Mandrekar", bg = "#040c5c", fg = "#f77c00",bd=10, font = ('Helvetica',11, 'bold'))
    l1.pack()
    l2.pack()
    l3.pack()
    m.mainloop()

if __name__=='__main__':
    top = tkinter.Tk(className='Aniket')
    top.configure(bg='#040c5c')
    top.geometry("400x150")

    label = tkinter.Label(top, text = "Hand Gestures Control using Rpi", bg = "#040c5c",bd=10, fg = "white", font = ('Helvetica', 18, 'bold'))
    label.pack()

    b1=tkinter.Button(top,width=50, text="Control Hardware",fg='white', bg='#f77c00', command=Control_Hardware)
    b2=tkinter.Button(top,width=50, text="Control Software",fg='white', bg='#f77c00',command=Control_Software)
    b3=tkinter.Button(top,width=50, text="About",fg='white', bg='#f77c00', command = About)

    b1.pack()
    b2.pack()
    b3.pack()

    top.mainloop()
