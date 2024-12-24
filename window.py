from tkinter import *
win=Tk()
win.title("my Project")
win.geometry('600x400')
win.resizable(0,0)

lbl1=Label(win,Text="Name:")
lbl1.place(x=50,y=30)
lbl2=Label(win,Text="Last Name:")
lbl2.place(x=50,y=80)
lbl3=Label(win,Text="National code:")
lbl3.place(x=50,y=100)
lbl4=Label(win,Text="Date of Birth:")
lbl4.place(x=50,y=120)
lbl5=Label(win,Text="Father's name:")
lbl5.place(x=50,y=140)
lbl6=Label(win,Text="degree of Education:")
lbl6.place(x=50,y=160)
lbl7=Label(win,Text="Phone namber:")
lbl7.place(x=50,y=180)

txtn=Entry(win)
txtn.place(x=120,y=30)

txtln=Entry(win)
txtln.place(x=120,y=80)
btn=Button(win,text="Submit")
btn.place(x=120,y=130)




