import os
import tkinter as tk
import time
root = tk.Tk()
root.title("jam digital")
root.geometry("300x100")
root.resizable(False,False)

label = tk.Label(root,font=("calibri",40,'bold'),
bg= "#000000",
fg = "#FFFFFF",
bd = 8,
relief = 'solid',)
label.pack(anchor="center")

def update_clock():
    label.config(text=time.strftime("%H:%M:%S"))
    label.after(1000, update_clock)
update_clock()
root.mainloop()