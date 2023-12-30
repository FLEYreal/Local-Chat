import tkinter as tk
import os 


#window

window = tk.Tk()
window.title('chat')
window.geometry('400x300')

#icon
icon=tk.PhotoImage(file="view\\assets\icon.png") #иконка сжимается. нужно потом решить 
window.iconphoto(True,icon)
#title




window.mainloop()