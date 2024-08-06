# from tkinter import*
# root=Tk()
# #root.iconbitmap("abc.ico")
# root.tittle("login")
# root.geometry("300x400")
# root.resizable(0,0)
# mainloop()

# from tkinter import
# win=Tk()
# win.tittle("system")
# from tkinter import *
# root = Tk()
# redbutton = Button(root,text = "LEFT", fg = "green")
# redbutton.pack( side= LEFT )
# greenbutton = Button(root,text = "RIGHT",fg = "black")
# greenbutton.pack(side = RIGHT)
# bluebutton=Button(root,text = "Top", fg = "blue")
# bluebutton.pack( side = TOP)
# blackbutton = Button(root , text = "BOTTOM",fg="red")
# blackbutton.pack( side = BOTTOM)
# root.mainloop()


from tkinter import*

top = Tk()
top.geometry("400x250")

name=Label(top, text = "Name").place(x=30, y=50)
address = Label(top, text = "Address").place(x = 30, y = 90)
contact = Label(top, text = "Contact ").place(x=30, y=130)
e1=Entry(top).place(x=80, y=50)
e2=Entry(top).place(x = 80, y=90)
e3=Entry(top).place(x = 95, y = 130)
