import tkinter as tk
from tkinter import messagebox

def sumar(entry1, entry2, result):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        suma = num1 + num2
        result.set(suma)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido")

def restar(entry1, entry2, result):
    try:
        num1= float(entry1.get())
        num2= float(entry2.get())
        resta= num1-num2
        result.set(resta)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido")

def multiplicar(entry1, entry2, result):
    try:
        num1= float(entry1.get())
        num2= float(entry2.get())
        multiplicacion= num1*num2
        result.set(multiplicacion)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido")

def dividir(entry1, entry2, result):
    try:
        num1= float(entry1.get())
        num2= float(entry2.get())
        division= num1/num2
        result.set(division)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido")


root = tk.Tk()
root.title("Sumador de números")
root.geometry("600x400") 

label1 = tk.Label(root, text="Número 1:")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Número 2:")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

label_result = tk.Label(root, text="Resultado:")
label_result.pack(pady=5)

result = tk.StringVar()
entry_result = tk.Entry(root, textvariable=result, state="readonly")
entry_result.pack(pady=5)

button_suma = tk.Button(root, text="Sumar", command=lambda: sumar(entry1, entry2, result))
button_suma.pack(pady=5)

button_resta = tk.Button(root, text="restar", command=lambda: restar(entry1, entry2, result))
button_resta.pack(pady=5)

button_multiplicacion = tk.Button(root, text="multiplicar", command=lambda: multiplicar(entry1, entry2, result))
button_multiplicacion.pack(pady=5)

button_division = tk.Button(root, text="dividir", command=lambda: dividir(entry1, entry2, result))
button_division.pack(pady=5)


root.mainloop()
