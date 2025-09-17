# form.py
import tkinter as tk
from tkinter import messagebox
from cursor import insertar_factura  # Importa la función de inserción

class Formulario(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulario de Compra")

        # Widgets
        tk.Label(self, text="Nombre del producto:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Precio del producto:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_precio = tk.Entry(self)
        self.entry_precio.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Cantidad:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_cantidad = tk.Entry(self)
        self.entry_cantidad.grid(row=2, column=1, padx=10, pady=5)

        btn_guardar = tk.Button(self, text="Guardar Compra", command=self.calcular_y_guardar)
        btn_guardar.grid(row=3, column=0, columnspan=2, pady=10)

        self.label_resultado = tk.Label(self, text="", fg="blue", justify="left")
        self.label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

    def calcular_y_guardar(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            messagebox.showerror("Error", "El nombre del producto no puede estar vacío.")
            return

        try:
            precio = float(self.entry_precio.get())
            if precio <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Precio inválido.")
            return

        try:
            cantidad = int(self.entry_cantidad.get())
            if cantidad < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida.")
            return

        subtotal = precio * cantidad
        total = subtotal  # Aquí puedes aplicar impuestos si deseas

        self.label_resultado.config(
            text=f"Producto: {nombre}\nCantidad: {cantidad}\nSubtotal: ${subtotal:,.2f}\nTotal: ${total:,.2f}"
        )

        # Guardar en BD
        insertar_factura(nombre, cantidad, precio, subtotal, total)

# Ejecutar si es archivo principal
if __name__ == "__main__":
    app = Formulario()
    app.mainloop()
