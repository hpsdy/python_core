#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *

def resize(ev=None):
    la.config(font='Helvetica -%d bold' % scale.get())
top = Tk()
top.geometry('500x500')
la = Label(top,text='hello world',font='Helvetica -12 bold')
la.pack(fill=X,expand=1)
scale = Scale(top,from_=10,to=140,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=X,expand=1)

quit = Button(top,text='QUIT',command=top.quit,activeforeground='white',activebackground='red')
quit.pack(fill=X)
mainloop()