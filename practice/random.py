from tkinter import *
root = Tk()

lb1 = Label(root, text='name')
lb1.pack()

txt = Entry(root)
txt.pack()

btn = Button(root, text="ok" )
btn.pack()

root.mainloop()