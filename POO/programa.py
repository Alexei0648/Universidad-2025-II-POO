import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import webbrowser
import json

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ARCHIVO_DATOS = "datos_guardados.json"

class VentanaGuardar:
    def __init__(self, parent, guardar_callback):
        self.parent = parent
        self.guardar_callback = guardar_callback
        self.datos_guardados = {}

        self.window = ctk.CTkToplevel(parent)
        self.window.title("Guardar Archivos o Link")
        self.window.geometry("500x300")

        self.campos = {}

        self.crear_campo("Imagen", ["*.png", "*.jpg", "*.jpeg"])
        self.crear_campo("PDF", ["*.pdf"])
        self.crear_campo("PPT", ["*.pptx"])
        self.crear_campo("Link", tipo="entrada")

        btn_aceptar = ctk.CTkButton(self.window, text="Aceptar", command=self.guardar_datos)
        btn_aceptar.pack(pady=15)

    def crear_campo(self, nombre, extensiones=None, tipo="archivo"):
        frame = ctk.CTkFrame(self.window)
        frame.pack(padx=10, pady=5, fill="x")

        label = ctk.CTkLabel(frame, text=nombre + ": ", width=10, anchor="w")
        label.pack(side="left")

        entry = ctk.CTkEntry(frame, width=300)
        entry.pack(side="left", padx=5)

        if tipo == "archivo":
            btn = ctk.CTkButton(frame, text="Seleccionar", command=lambda: self.seleccionar_archivo(nombre, entry, extensiones))
            btn.pack(side="left")
            self.campos[nombre] = (entry, btn)
        else:
            self.campos[nombre] = (entry, None)

    def seleccionar_archivo(self, nombre, entry, extensiones):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos válidos", extensiones)])
        if archivo:
            entry.delete(0, "end")
            entry.insert(0, archivo)

    def guardar_datos(self):
        self.datos_guardados.clear()
        for nombre, (entry, _) in self.campos.items():
            valor = entry.get().strip()
            if valor:
                self.datos_guardados[nombre] = valor

        if "Link" in self.datos_guardados:
            webbrowser.open(self.datos_guardados["Link"])

        # Guardar en archivo
        with open(ARCHIVO_DATOS, "w") as f:
            json.dump(self.datos_guardados, f)

        self.guardar_callback(self.datos_guardados)
        self.window.destroy()


class AppPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación Principal")
        self.root.geometry("500x300")

        self.datos_guardados = self.cargar_datos()

        self.frame_central = ctk.CTkFrame(root)
        self.frame_central.pack(expand=True)

        self.btn_guardar = ctk.CTkButton(self.frame_central, text="Guardar", width=200, height=50, command=self.abrir_ventana_guardar)
        self.btn_guardar.pack(pady=10)

        self.btn_ejecutar = ctk.CTkButton(self.frame_central, text="Ejecutar", width=200, height=50, command=self.ejecutar_datos)
        self.btn_ejecutar.pack(pady=10)

    def abrir_ventana_guardar(self):
        VentanaGuardar(self.root, self.recibir_datos_guardados)

    def recibir_datos_guardados(self, datos):
        self.datos_guardados = datos
        messagebox.showinfo("Guardado", "Los datos fueron guardados exitosamente.")

    def ejecutar_datos(self):
        if not self.datos_guardados:
            messagebox.showwarning("Sin datos", "No se han ingresado datos aún.")
            return

        for tipo, ruta in self.datos_guardados.items():
            try:
                if tipo == "Link":
                    webbrowser.open(ruta)
                else:
                    os.startfile(ruta)  # Solo funciona en Windows
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir {tipo}: {e}")

    def cargar_datos(self):
        if os.path.exists(ARCHIVO_DATOS):
            try:
                with open(ARCHIVO_DATOS, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}


if __name__ == "__main__":
    root = ctk.CTk()
    app = AppPrincipal(root)
    root.mainloop()
