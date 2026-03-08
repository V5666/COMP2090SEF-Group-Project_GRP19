from tkinter import*
import tkinter as tk
import sys,time,datetime,os
from time import strftime
import tkinter.font as tkFont
from tkinter import scrolledtext,messagebox

win = Tk()
win.title("")
current_time = time.localtime()

win.geometry("1280x720+250-170")
win.minsize(width=400,height=200)
win.maxsize(width=1980,height=1080)
win.resizable(False,False)
win.config(bg="skyblue")
win.attributes("-alpha",1)
win.attributes("-topmost",True)

fontStyle = tkFont.Font(family="Lucida Grande", size=40)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=25)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=60)

def tool_set():
    btn_NBBR = tk.Button(win,font=fontStyle1,text="New Books & Books Record",bg= 'skyblue',command=NBBR)
    btn_NBBR.place(anchor=CENTER,x=220,y=30)
    btn_SRCH = tk.Button(win,font=fontStyle1,text="Book searching",bg= 'skyblue',command=SRCH)
    btn_SRCH.place(anchor=CENTER,x=570,y=30)

def New_Books_Books_Record():
    lab_bt = tk.Label(win,font=fontStyle1,text="Adding New Books",bg= 'skyblue')
    lab_bt.place(anchor=CENTER,x=650,y=80)
    lab_bt = tk.Label(win,font=fontStyle1,text="Book Title",bg= 'skyblue')
    lab_bt.place(anchor=CENTER,x=100,y=170)
    ety_bt = tk.Entry(win,font=fontStyle1,bg= 'skyblue')
    ety_bt.place(anchor=CENTER,x=400,y=170)

    lab_at = tk.Label(win,font=fontStyle1,text="Author",bg= 'skyblue')
    lab_at.place(anchor=CENTER,x=680,y=170)
    ety_at = tk.Entry(win,font=fontStyle1,bg= 'skyblue')
    ety_at.place(anchor=CENTER,x=950,y=170)

    btn_enter = tk.Button(win,font=fontStyle1,text="Enter",bg='skyblue')#New book data input function required 
    btn_enter.place(anchor=CENTER,x=1200,y=170)

    lab_br = tk.Label(win,font=fontStyle1,text="Books Record",bg= 'skyblue')
    lab_br.place(anchor=CENTER,x=120,y=310)
    rec_box = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=70, height=10,bg='skyblue',font=fontStyle1)#Books data insert function required
    rec_box.place(anchor=CENTER,x=620,y=520)
    rec_box.config(state='disabled')

def Search():
    print("still building......")

def NBBR():
    clear()
    New_Books_Books_Record()

def SRCH():
    clear()
    Search()

def clear():
    x = win.winfo_children()
    for x in x:
        x.destroy()
    tool_set()

tool_set()
New_Books_Books_Record()
win.mainloop()