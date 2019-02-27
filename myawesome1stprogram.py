from tkinter import *

okno = Tk()
okno.geometry('1600x600')
okno.title("Zajebiste okienko")
lbl = Label(okno, text="Hello")
lbl.grid(column=4, row=3)
btn = Button(okno, text="Click Me")
btn.grid(column=1, row=0)

okno.mainloop()

