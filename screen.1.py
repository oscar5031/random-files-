from tkinter import *
#key functions

##main:
window = Tk()
window.title("Prep team")
window.configure (width=3000, height=6000, background="black")
##Labels:
Label (window, text="Toast go").grid(row=10, column = 5)

##create a text entry box
textentry = Entry(window, width =30, bg="white")
textentry.grid(row=1, column =2)
window.configure (width=3000, height=6000, background="black")

window.mainloop()
