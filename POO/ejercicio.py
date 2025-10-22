import tkinter as tk
from tkinter import ttk, messagebox
import random

def generar_matriz(filas, columnas, rango=(-10, 10)):
    return [[random.randint(rango[0], rango[1]) for _ in range(columnas)] for _ in range(filas)]

def matriz_a_str(matriz):
    return "\n".join("  ".join(f"{num:4d}" for num in fila) for fila in matriz)

def sumar_matrices(matrices):
    filas = len(matrices[0])
    columnas = len(matrices[0][0])
    suma = [[0]*columnas for _ in range(filas)]
    for matriz in matrices:
        for i in range(filas):
            for j in range(columnas):
                suma[i][j] += matriz[i][j]
    return suma

def multiplicar_matrices(matriz1, matriz2):
    filas1, cols1 = len(matriz1), len(matriz1[0])
    filas2, cols2 = len(matriz2), len(matriz2[0])
    if filas1 != cols2 or cols1 != filas2:
        raise ValueError("Para multiplicar, filas de matriz1 deben ser igual a columnas de matriz2\n"
                         "y columnas de matriz1 deben ser igual a filas de matriz2")
    resultado = [[0]*cols2 for _ in range(filas1)]
    for i in range(filas1):
        for j in range(cols2):
            for k in range(cols1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Operaciones con Matrices")
        self.geometry("700x600")
        self.configure(bg="#f0f0f0")
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Segoe UI', 11))
        self.style.configure('TLabel', font=('Segoe UI', 11))
        self.style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'))
        
        self.crear_widgets()

    def crear_widgets(self):
        ttk.Label(self, text="Dimensiones Matriz 1", style='Header.TLabel').pack(pady=(10,0))
        frame_dim1 = ttk.Frame(self)
        frame_dim1.pack(pady=5)
        ttk.Label(frame_dim1, text="Filas:").grid(row=0, column=0, padx=5)
        self.filas1_entry = ttk.Entry(frame_dim1, width=5)
        self.filas1_entry.grid(row=0, column=1, padx=5)
        ttk.Label(frame_dim1, text="Columnas:").grid(row=0, column=2, padx=5)
        self.columnas1_entry = ttk.Entry(frame_dim1, width=5)
        self.columnas1_entry.grid(row=0, column=3, padx=5)

        ttk.Label(self, text="Dimensiones Matriz 2", style='Header.TLabel').pack(pady=(15,0))
        frame_dim2 = ttk.Frame(self)
        frame_dim2.pack(pady=5)
        ttk.Label(frame_dim2, text="Filas:").grid(row=0, column=0, padx=5)
        self.filas2_entry = ttk.Entry(frame_dim2, width=5)
        self.filas2_entry.grid(row=0, column=1, padx=5)
        ttk.Label(frame_dim2, text="Columnas:").grid(row=0, column=2, padx=5)
        self.columnas2_entry = ttk.Entry(frame_dim2, width=5)
        self.columnas2_entry.grid(row=0, column=3, padx=5)

        # Botones de acción
        frame_botones = ttk.Frame(self)
        frame_botones.pack(pady=20)
        self.btn_sumar = ttk.Button(frame_botones, text="Sumar matrices (mismo tamaño)", command=self.sumar_matrices)
        self.btn_sumar.grid(row=0, column=0, padx=10)
        self.btn_multiplicar = ttk.Button(frame_botones, text="Multiplicar matrices (condición especial)", command=self.multiplicar_matrices)
        self.btn_multiplicar.grid(row=0, column=1, padx=10)

        # Texto para mostrar matrices y resultado
        self.texto_matrices = tk.Text(self, width=80, height=20, font=("Consolas", 10))
        self.texto_matrices.pack(pady=10)

    def leer_dimensiones(self):
        try:
            f1 = int(self.filas1_entry.get())
            c1 = int(self.columnas1_entry.get())
            f2 = int(self.filas2_entry.get())
            c2 = int(self.columnas2_entry.get())
            if f1 <= 0 or c1 <= 0 or f2 <= 0 or c2 <= 0:
                raise ValueError
            return f1, c1, f2, c2
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese dimensiones válidas (enteros positivos).")
            return None

    def sumar_matrices(self):
        dims = self.leer_dimensiones()
        if not dims:
            return
        f1, c1, f2, c2 = dims
        if f1 != f2 or c1 != c2:
            messagebox.showerror("Error", "Para sumar matrices, ambas deben tener las mismas dimensiones.")
            return
        m1 = generar_matriz(f1, c1)
        m2 = generar_matriz(f2, c2)
        resultado = sumar_matrices([m1, m2])
        self.mostrar_matrices_y_resultado([m1, m2], resultado, operacion="Suma")

    def multiplicar_matrices(self):
        dims = self.leer_dimensiones()
        if not dims:
            return
        f1, c1, f2, c2 = dims
        try:
            m1 = generar_matriz(f1, c1)
            m2 = generar_matriz(f2, c2)
            resultado = multiplicar_matrices(m1, m2)
            self.mostrar_matrices_y_resultado([m1, m2], resultado, operacion="Multiplicación")
        except ValueError as e:
            messagebox.showerror("Error en multiplicación", str(e))

    def mostrar_matrices_y_resultado(self, matrices, resultado, operacion):
        self.texto_matrices.delete("1.0", tk.END)
        for idx, m in enumerate(matrices, start=1):
            self.texto_matrices.insert(tk.END, f"Matriz {idx}:\n{matriz_a_str(m)}\n\n")
        self.texto_matrices.insert(tk.END, f"Resultado de la {operacion}:\n{matriz_a_str(resultado)}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
