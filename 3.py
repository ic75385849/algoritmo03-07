import tkinter as tk
from tkinter import messagebox

def click(button, entry):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(button))

def clear(entry):
    entry.delete(0, tk.END)

def calcular(entry):
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero")
    except Exception:
        messagebox.showerror("Error", "Por favor ingrese una expresión válida")

root = tk.Tk()
root.title("Calculadora")
root.geometry("600x600")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=40, pady=20, command=lambda entry=entry: calcular(entry))
    else:
        btn = tk.Button(root, text=button, padx=40, pady=20, command=lambda button=button, entry=entry: click(button, entry))
    btn.grid(row=row, column=col)
    col += 1
    if col == 4:
        col = 0
        row += 1

clear_button = tk.Button(root, text='C', padx=40, pady=20, command=lambda entry=entry: clear(entry))
clear_button.grid(row=row, column=0, columnspan=2)
        
root.mainloop()