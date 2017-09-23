#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from tkinter import *
tk = Tk()

label = Label(tk,text='hello world')
label.pack()
bu = Button(tk,text='QUIT',command=tk.quit,bg='red',fg='white')
#bu.pack(fill=X)
#bu.pack(expand=1)
bu.pack(fill=X,expand=1)
mainloop()