from tkinter import *

root = Tk()

root.title("ASCII")
root.geometry("400x400")

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

lbl = Label(root, text = "Name in ASCII : ", bg="light yellow", fg = "black")

def asciiconverter():
   input_word = enter_word.get()
    
    for letter in input_word:
        lbl["text"] += str(ord(letter)) + " "
    
    btn = Button(root, text = "Show name in ASCII",command=asciiconverter, bg = "gold", fg = "black")
    btn.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    lbl.place(relx=0.5,rely=0.6,anchor=CENTER)
    root.mainloop()