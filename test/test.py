from tkinter import *
from tkinter import ttk


def calculate():
    try:
        value = int(number.get())
        prime.set(value * value)
    except ValueError:
        pass


window = Tk()
window.title("Laneway Coverage Calculator")

mainframe = ttk.Frame(window, padding="5 5 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

number = StringVar()
number_entry = ttk.Entry(mainframe, width=5, textvariable=number)
number_entry.grid(column=2, row=1, sticky=(W, E))

prime = StringVar()
ttk.Label(mainframe, textvariable=prime).grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=2, row=2, sticky=(W, E)
)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
number_entry.focus()
window.bind("<Return>", calculate)

window.mainloop()
