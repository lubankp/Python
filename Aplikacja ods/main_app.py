import tkinter as tk
from tkinter import messagebox


def about():
    tk.messagebox.showinfo("Powitanie", "Hej!")


gui = tk.Tk()
gui.title("Przykładowa aplikacja")
gui.geometry("200x100")
btn = tk.Button(gui, command=about, text="Kliknij mnie!")
btn.grid(row=0, column=0)
gui.mainloop()