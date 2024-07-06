import tkinter as tk
from tkinter import messagebox

def sumar (entry1, entry2, result):
    try:
        num1= float (entry1.get())
        num2= float (entry2.get())
        suma= num1 + num2
        result.set(suma)
    except ValueError:
        messagebox.showerror("error", "porfavor ingresar un numero valido")


root= tk. Tk()
root.title("sumador de numeros")
root.geometry("600x400")

label1= tk.Label(root, text="numero 1: ")
label1.pack(pady=5)

entry1= tk.Entry(root)
entry1.pack(pady=5)


label2= tk.Label(root, text="numero 2: ")
label2.pack(pady=5)

entry2= tk.Entry(root)
entry2.pack(pady=5)

label_result= tk.Label(root, text="resultado: ")
label_result.pack(pady=5)
result= tk.StringVar()
entry_result= tk.Entry(root, textvariable=result , state="readonly")
entry_result.pack(pady=5)


button_sum= tk.Button(root, text="sumar", command=lambda: sumar(entry1, entry2, result))
button_sum.pack(pady=10)

root.mainloop()                    