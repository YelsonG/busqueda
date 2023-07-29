import tkinter as tk
from tkinter import messagebox

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def search():
    try:
        target = int(entry.get())
        result = binary_search(sorted_array, target)
        if result != -1:
            messagebox.showinfo("Resultado", f"El número {target} fue encontrado en la posición {result}.")
        else:
            messagebox.showinfo("Resultado", f"El número {target} no fue encontrado en el arreglo.")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número entero válido.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Búsqueda Binaria")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Ingresa los números separados por comas:")
label.pack()

entry = tk.Entry(frame)
entry.pack()

search_button = tk.Button(frame, text="Buscar", command=search)
search_button.pack()

sorted_array = []  # El arreglo debe estar ordenado para aplicar la búsqueda binaria.

root.mainloop()
