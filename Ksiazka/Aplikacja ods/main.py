import tkinter as tk
from tkinter import messagebox


def about():
    tk.messagebox.showinfo("Powitanie", "Hej!")

def window1():

    window1 = tk.Tk()
    window1.title("Window1")
    window1.geometry("400x300")

def window2():
    window2 = tk.Tk()
    window2.title("Window1")
    window2.geometry("400x300")

gui = tk.Tk()
gui.title("Przykładowa aplikacja")
gui.geometry("1500x900")

butt_ref_start = tk.Button(gui, command=window1, text="rozpoczecie ref", fg="black", font = "Verdana 24", bd = 2, bg = "blue", relief = "groove", width = 14, height = 2)
butt_ref_start.grid(row=1, column=1)
butt_ref_end = tk.Button(gui, command=about, text="Zakoncenie ref", fg="black", font = "Verdana 24", bd = 2, bg = "pink", relief = "groove", width = 14, height = 2)
butt_ref_end.grid(row=1, column=4)

butt_prod = tk.Button(gui, command=about, text="Produkcja", fg="black", font = "Verdana 36", bd = 2, bg = "blue", relief = "groove", width = 10, height = 2)
butt_prod.grid(row=3, column=1, padx=5, pady=5)
butt_prze = tk.Button(gui, command=about, text="Przezbrojenie", fg="black", font = "Verdana 36", bd = 2, bg = "pink", relief = "groove", width = 10, height = 2)
butt_prze.grid(row=3, column=2, padx=5, pady=5)
butt_pomi = tk.Button(gui, command=about, text="Pomiary", fg="black", font = "Verdana 36", bd = 2, bg = "red", relief = "groove", width = 10, height = 2)
butt_pomi.grid(row=3, column=3, padx=5, pady=5)
butt_awa = tk.Button(gui, command=about, text="Awaria", fg="black", font = "Verdana 36", bd = 2, bg = "orange", relief = "groove", width = 10, height = 2)
butt_awa.grid(row=3, column=4, padx=5, pady=5)
butt_przes = tk.Button(gui, command=about, text="Przestoj", fg="black", font = "Verdana 36", bd = 2, bg = "violet", relief = "groove", width = 21, height = 2)
butt_przes.grid(row=4, column=1, padx=5, pady=5, columnspan=2)
butt_uwag = tk.Button(gui, command=about, text="Uwagii", fg="black", font = "Verdana 36", bd = 2, bg = "green", relief = "groove", width = 21, height = 2)
butt_uwag.grid(row=4, column=3, padx=5, pady=5, columnspan=2)

gui.mainloop()
