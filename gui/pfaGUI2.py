#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from tkinter import *
from functools import partial
from tkinter.messagebox import showinfo,showwarning,showerror
from collections import OrderedDict
INFO='提示'
WARN='警告'
ERROR='致命'
map = OrderedDict()
map['limit50']='INFO'
map['limit100']='WARN'
map['died']='ERROR'
infoW = lambda:showinfo(INFO,INFO)
warnW = lambda:showwarning(WARN,WARN)
errorW = lambda:showerror(ERROR,ERROR)
top = Tk()
top.title('告示')
B = partial(Button,top)
INFOB = partial(B,command=infoW,bg='white',fg='black')
WARNB = partial(B,command=warnW,bg='yellow',fg='black')
ERRORB = partial(B,command=errorW,bg='white',fg='red')
Button(top,text='QUIT',command=top.quit).pack(fill=X,expand=True)
for k in map:
    t = map[k]
    cmd = "%sB(text='%s').pack(fill=X,expand=True)" % (t,k)
    print(cmd)
    eval(cmd)
top.mainloop()

