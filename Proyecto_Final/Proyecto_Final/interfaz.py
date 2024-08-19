import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from main import *
from Modelos.modelos import *
from hashlib import sha256
import getpass
import bcrypt
from db import *
def login():
    email = email_entry.get()
    password = password_entry.get()

    try:
        # Verificar si el usuario existe en la tabla usuarios
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        
        if usuario:
            tipo_usuario = usuario[7]  # El tipo de usuario está en la posición 7
            hashed_password = usuario[8]  # El hash de la contraseña está en la posición 8
            
            # Verificar la contraseña ingresada con la hasheada
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                login_window.destroy()
                abrir_punto_venta()
            else:
                messagebox.showerror("Error", "Contraseña incorrecta.")
        else:
            messagebox.showerror("Error", "Usuario no encontrado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Función que abre la ventana principal del punto de venta
def abrir_punto_venta():
    global tree_venta, total_value  # Hacer tree_venta y total_value accesibles globalmente

    def agregar_producto_a_venta(producto):
        item_id = tree_venta.insert("", tk.END, values=producto)
        actualizar_total()

    def actualizar_total():
        total = 0
        for child in tree_venta.get_children():
            cantidad = int(tree_venta.item(child, 'values')[2])
            precio = float(tree_venta.item(child, 'values')[3])
            total += cantidad * precio
        total_value.config(text=f"$ {total:.2f}")

    def completar_venta():
        # Eliminar todos los elementos del Treeview
        for item in tree_venta.get_children():
            tree_venta.delete(item)
        
        # Restablecer el total a 0.00
        total_value.config(text="$ 0.00")

    root = tk.Tk()
    root.title("Punto de Venta")
    root.attributes('-fullscreen', True)
    root.config(bg='lightblue')

    title_label = tk.Label(root, text="PUNTO DE VENTA", font=("Arial", 24, "bold"), fg="blue", bg="lightblue")
    title_label.pack(pady=10)

    user_label = tk.Label(root, text="Usuario: Diego Antunez", font=("Arial", 12), bg="lightblue")
    user_label.pack(anchor='ne', padx=10)

    frame_nav = tk.Frame(root, bg="lightgrey")
    frame_nav.pack(fill="x", padx=10, pady=10)

    buttons = {
        "PRODUCTOS": lambda: abrir_ventana_productos(agregar_producto_a_venta, actualizar_total),
        "SERVICIOS": lambda: abrir_ventana_servicios(),
        "CLIENTES": lambda: abrir_ventana_clientes(),
        "EMPLEADOS": lambda: abrir_ventana_empleados(),
        "TICKETS": lambda: print("Tickets"),
    }
    for btn_text, btn_command in buttons.items():
        tk.Button(frame_nav, text=btn_text, font=("Arial", 12, "bold"), bg="lightgrey", command=btn_command).pack(side="left", padx=5, pady=5)

    frame_table = tk.Frame(root, bg="lightblue")
    frame_table.pack(fill="both", expand=True, padx=10)

    cols = ["ID", "PRODUCTO / SERVICIO", "CANTIDAD", "PRECIO", "TOTAL"]
    tree_venta = ttk.Treeview(frame_table, columns=cols, show="headings")
    for col in cols:
        tree_venta.heading(col, text=col, anchor='center')
        tree_venta.column(col, anchor='center')
    tree_venta.pack(fill="both", expand=True)

    frame_bottom = tk.Frame(root, bg="lightgrey")
    frame_bottom.pack(fill="x", padx=10, pady=10)

    btn_completar = tk.Button(frame_bottom, text="COMPLETAR VENTA", font=("Arial", 12, "bold"), bg="grey", command=completar_venta)
    btn_completar.pack(side="left", padx=10, pady=10)

    total_label = tk.Label(frame_bottom, text="TOTAL DE VENTA", font=("Arial", 18, "bold"), fg="blue", bg="lightgrey")
    total_label.pack(side="left", padx=20)

    total_value = tk.Label(frame_bottom, text="$ 0.00", font=("Arial", 18, "bold"), fg="blue", bg="lightgrey")
    total_value.pack(side="left")

    root.bind("<F11>", lambda event: toggle_fullscreen(root, event))
    root.bind("<Escape>", lambda event: exit_fullscreen(root, event))

    root.mainloop()

def abrir_ventana_productos(agregar_producto_a_venta, actualizar_total):
    def actualizar_tabla_productos():
        for item in tree.get_children():
            tree.delete(item)
        
        productos = Productos.listar_productos(cursor)
        for producto in productos:
            tree.insert("", tk.END, values=producto)

    def abrir_formulario_agregar_producto():
        def agregar():
            nombre = entry_nombre.get()
            descripcion = entry_descripcion.get()
            cantidad = int(entry_cantidad.get())
            precio_compra = float(entry_precio_compra.get())
            precio_venta = float(entry_precio_venta.get())

            Productos.agregar_producto(nombre, descripcion, cantidad, precio_compra, precio_venta, cursor, conexion)
            formulario_window.destroy()
            actualizar_tabla_productos()

        formulario_window = tk.Toplevel()
        formulario_window.title("Agregar Producto")
        formulario_window.geometry("400x300")
        formulario_window.config(bg="lightgrey")

        tk.Label(formulario_window, text="Nombre:", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_window)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Descripción:", bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
        entry_descripcion = tk.Entry(formulario_window)
        entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Cantidad:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
        entry_cantidad = tk.Entry(formulario_window)
        entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Precio Compra:", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
        entry_precio_compra = tk.Entry(formulario_window)
        entry_precio_compra.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Precio Venta:", bg="lightgrey").grid(row=4, column=0, padx=5, pady=5)
        entry_precio_venta = tk.Entry(formulario_window)
        entry_precio_venta.grid(row=4, column=1, padx=5, pady=5)

        btn_agregar = tk.Button(formulario_window, text="Agregar", command=agregar)
        btn_agregar.grid(row=5, columnspan=2, pady=10)

    def abrir_formulario_modificar_producto(codigo):
        def modificar():
            nombre = entry_nombre.get()
            descripcion = entry_descripcion.get()
            cantidad = int(entry_cantidad.get())
            precio_compra = float(entry_precio_compra.get())
            precio_venta = float(entry_precio_venta.get())

            Productos.modificar_producto(codigo, nombre, descripcion, cantidad, precio_compra, precio_venta, cursor, conexion)
            formulario_window.destroy()
            actualizar_tabla_productos()

        formulario_window = tk.Toplevel()
        formulario_window.title("Modificar Producto")
        formulario_window.geometry("400x300")
        formulario_window.config(bg="lightgrey")

        tk.Label(formulario_window, text="Nombre:", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_window)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Descripción:", bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
        entry_descripcion = tk.Entry(formulario_window)
        entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Cantidad:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
        entry_cantidad = tk.Entry(formulario_window)
        entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Precio Compra:", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
        entry_precio_compra = tk.Entry(formulario_window)
        entry_precio_compra.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Precio Venta:", bg="lightgrey").grid(row=4, column=0, padx=5, pady=5)
        entry_precio_venta = tk.Entry(formulario_window)
        entry_precio_venta.grid(row=4, column=1, padx=5, pady=5)

        btn_modificar = tk.Button(formulario_window, text="Modificar", command=modificar)
        btn_modificar.grid(row=5, columnspan=2, pady=10)

        cursor.execute("SELECT * FROM productos WHERE codigo = %s", (codigo,))
        producto = cursor.fetchone()
        if producto:
            entry_nombre.insert(0, producto[1])
            entry_descripcion.insert(0, producto[2])
            entry_cantidad.insert(0, producto[3])
            entry_precio_compra.insert(0, producto[4])
            entry_precio_venta.insert(0, producto[5])

    def on_modificar():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            codigo = item_values[0]
            abrir_formulario_modificar_producto(codigo)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un producto para modificar.")

    def on_eliminar():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            codigo = item_values[0]
            confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que deseas eliminar el producto con código {codigo}?")
            if confirmacion:
                Productos.eliminar_producto(codigo, cursor, conexion)
                actualizar_tabla_productos()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar.")

    def on_doble_click(event):
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            agregar_producto_a_venta(item_values)
    
    # Función para aumentar o disminuir la cantidad del producto en la venta
    def modificar_cantidad(item_id, incremento):
        item = tree_venta.item(item_id)
        cantidad = int(item['values'][2]) + incremento
        if cantidad < 0:
            cantidad = 0
        precio = float(item['values'][3])
        total = cantidad * precio
        tree_venta.item(item_id, values=(item['values'][0], item['values'][1], cantidad, precio, total))
        actualizar_total()

    # Crear ventana principal de productos
    ventana_productos = tk.Toplevel()
    ventana_productos.title("Productos")
    ventana_productos.geometry("600x400")
    ventana_productos.config(bg="lightgrey")

    title_label = tk.Label(ventana_productos, text="PRODUCTOS", font=("Arial", 24, "bold"), bg="lightgrey")
    title_label.pack(pady=10)

    frame_table = tk.Frame(ventana_productos, bg="lightgrey")
    frame_table.pack(fill="both", expand=True, padx=10, pady=10)

    cols = ["CODIGO", "NOMBRE", "CANTIDAD", "PRECIO"]
    tree = ttk.Treeview(frame_table, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col, anchor='center')
        tree.column(col, anchor='center', width=100)
    tree.pack(fill="both", expand=True)

    actualizar_tabla_productos()

    tree.bind("<Double-1>", on_doble_click)

    frame_buttons = tk.Frame(ventana_productos, bg="lightgrey")
    frame_buttons.pack(fill="x", padx=10, pady=10)

    btn_añadir = tk.Button(frame_buttons, text="AÑADIR", font=("Arial", 12, "bold"), bg="grey", command=abrir_formulario_agregar_producto)
    btn_añadir.pack(side="left", padx=10)

    btn_modificar = tk.Button(frame_buttons, text="MODIFICAR", font=("Arial", 12, "bold"), bg="grey", command=on_modificar)
    btn_modificar.pack(side="left", padx=10)

    btn_eliminar = tk.Button(frame_buttons, text="ELIMINAR", font=("Arial", 12, "bold"), bg="grey", command=on_eliminar)
    btn_eliminar.pack(side="left", padx=10)

    # Ventana emergente para modificar la cantidad
    def ventana_modificar_cantidad(item_id):
        def aumentar():
            modificar_cantidad(item_id, 1)
        
        def disminuir():
            modificar_cantidad(item_id, -1)
        
        cantidad_window = tk.Toplevel()
        cantidad_window.title("Modificar Cantidad")
        cantidad_window.geometry("200x100")
        cantidad_window.config(bg="lightgrey")

        tk.Button(cantidad_window, text="+", font=("Arial", 16, "bold"), command=aumentar).pack(side="left", padx=10, pady=10)
        tk.Button(cantidad_window, text="-", font=("Arial", 16, "bold"), command=disminuir).pack(side="left", padx=10, pady=10)

    # Agregar evento para modificar la cantidad
    def on_modificar_cantidad():
        selected_item = tree_venta.selection()
        if selected_item:
            ventana_modificar_cantidad(selected_item[0])
        else:
            messagebox.showwarning("Advertencia", "Seleccione un producto para modificar la cantidad.")
    frame_bottom = tk.Frame(ventana_productos, bg="lightgrey")
    frame_bottom.pack(fill="x", padx=10, pady=10)        
            
    btn_modificar_cantidad = tk.Button(frame_bottom, text="MODIFICAR CANTIDAD", font=("Arial", 12, "bold"), bg="grey", command=on_modificar_cantidad)
    btn_modificar_cantidad.pack(side="left", padx=10, pady=10)

def abrir_ventana_servicios():
    def actualizar_tabla_servicios():
        for item in tree.get_children():
            tree.delete(item)
        
        servicios = Servicios.listar_servicios(cursor)
        for servicio in servicios:
            tree.insert("", tk.END, values=servicio)

    def abrir_formulario_agregar_servicio():
        def agregar():
            nombre = entry_nombre.get()
            descripcion = entry_descripcion.get()
            precio = float(entry_precio.get())

            Servicios.agregar_servicio(nombre, descripcion, precio, cursor, conexion)
            
            formulario_window.destroy()
            actualizar_tabla_servicios()

        formulario_window = tk.Toplevel()
        formulario_window.title("Agregar Servicio")
        formulario_window.geometry("400x300")
        formulario_window.config(bg="lightgrey")

        tk.Label(formulario_window, text="Nombre:", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_window)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Descripción:", bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
        entry_descripcion = tk.Entry(formulario_window)
        entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Precio:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
        entry_precio = tk.Entry(formulario_window)
        entry_precio.grid(row=2, column=1, padx=5, pady=5)

        btn_agregar = tk.Button(formulario_window, text="Agregar", command=agregar)
        btn_agregar.grid(row=3, columnspan=2, pady=10)

    def abrir_formulario_modificar_servicio(codigo):
        def modificar():
            nombre = entry_nombre.get()
            descripcion = entry_descripcion.get()
            precio = float(entry_precio.get())

            Servicios.modificar_servicio(codigo, nombre, descripcion, precio, cursor, conexion)
            
            formulario_window.destroy()
            actualizar_tabla_servicios()

        formulario_window = tk.Toplevel()
        formulario_window.title("Modificar Servicio")
        formulario_window.geometry("400x300")
        formulario_window.config(bg="lightgrey")

        tk.Label(formulario_window, text="Nombre:", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_window)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Descripción:", bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
        entry_descripcion = tk.Entry(formulario_window)
        entry_descripcion.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Precio:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
        entry_precio = tk.Entry(formulario_window)
        entry_precio.grid(row=2, column=1, padx=5, pady=5)

        btn_modificar = tk.Button(formulario_window, text="Modificar", command=modificar)
        btn_modificar.grid(row=3, columnspan=2, pady=10)

        cursor.execute("SELECT * FROM servicios WHERE codigo = %s", (codigo,))
        servicio = cursor.fetchone()
        if servicio:
            entry_nombre.insert(0, servicio[1])
            entry_descripcion.insert(0, servicio[2])
            entry_precio.insert(0, servicio[3])

    def on_modificar():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            codigo = item_values[0]
            abrir_formulario_modificar_servicio(codigo)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un servicio para modificar.")

    def on_eliminar():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            codigo = item_values[0]
            confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que deseas eliminar el servicio con código {codigo}?")
            if confirmacion:
                Servicios.eliminar_servicio(codigo, cursor, conexion)
                actualizar_tabla_servicios()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un servicio para eliminar.")

    ventana_servicios = tk.Toplevel()
    ventana_servicios.title("Servicios")
    ventana_servicios.geometry("600x400")
    ventana_servicios.config(bg="lightgrey")

    title_label = tk.Label(ventana_servicios, text="SERVICIOS", font=("Arial", 24, "bold"), bg="lightgrey")
    title_label.pack(pady=10)

    frame_table = tk.Frame(ventana_servicios, bg="lightgrey")
    frame_table.pack(fill="both", expand=True, padx=10, pady=10)

    cols = ["CÓDIGO", "NOMBRE", "DESCRIPCIÓN", "PRECIO"]
    tree = ttk.Treeview(frame_table, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col, anchor='center')
        tree.column(col, anchor='center', width=120)
    tree.pack(fill="both", expand=True)

    actualizar_tabla_servicios()

    frame_buttons = tk.Frame(ventana_servicios, bg="lightgrey")
    frame_buttons.pack(fill="x", padx=10, pady=10)

    btn_añadir = tk.Button(frame_buttons, text="AÑADIR", font=("Arial", 12, "bold"), bg="grey", command=abrir_formulario_agregar_servicio)
    btn_añadir.pack(side="left", padx=10)

    btn_modificar = tk.Button(frame_buttons, text="MODIFICAR", font=("Arial", 12, "bold"), bg="grey", command=on_modificar)
    btn_modificar.pack(side="left", padx=10)

    btn_eliminar = tk.Button(frame_buttons, text="ELIMINAR", font=("Arial", 12, "bold"), bg="grey", command=on_eliminar)
    btn_eliminar.pack(side="left", padx=10)
  
def abrir_ventana_clientes():
    def actualizar_tabla_clientes():
        for item in tree.get_children():
            tree.delete(item)
        
        clientes = Cliente.listarClientes(cursor)
        for cliente in clientes:
            tree.insert("", tk.END, values=cliente)

    def abrir_formulario_agregar_cliente():
        def agregar():
            nombre = entry_nombre.get()
            apellidoP = entry_apellidoP.get()
            apellidoM = entry_apellidoM.get()
            celular = entry_celular.get()
            email = entry_email.get()
            direccion = entry_direccion.get()
            password = entry_password.get()

            Cliente.registrarCliente(cursor, conexion, nombre, apellidoP, apellidoM, celular, email, direccion, password)
            
            formulario_window.destroy()
            actualizar_tabla_clientes()

        formulario_window = tk.Toplevel()
        formulario_window.title("Agregar Cliente")
        formulario_window.geometry("400x300")
        formulario_window.config(bg="lightgrey")

        tk.Label(formulario_window, text="Nombre:", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_window)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Apellido Paterno:", bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
        entry_apellidoP = tk.Entry(formulario_window)
        entry_apellidoP.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Apellido Materno:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
        entry_apellidoM = tk.Entry(formulario_window)
        entry_apellidoM.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Celular:", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
        entry_celular = tk.Entry(formulario_window)
        entry_celular.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Email:", bg="lightgrey").grid(row=4, column=0, padx=5, pady=5)
        entry_email = tk.Entry(formulario_window)
        entry_email.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Dirección:", bg="lightgrey").grid(row=5, column=0, padx=5, pady=5)
        entry_direccion = tk.Entry(formulario_window)
        entry_direccion.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Contraseña:", bg="lightgrey").grid(row=6, column=0, padx=5, pady=5)
        entry_password = tk.Entry(formulario_window, show='*')
        entry_password.grid(row=6, column=1, padx=5, pady=5)

        btn_agregar = tk.Button(formulario_window, text="Agregar", command=agregar)
        btn_agregar.grid(row=7, columnspan=2, pady=10)

    def abrir_formulario_modificar_cliente(id_cliente):
        def modificar():
            nombre = entry_nombre.get()
            apellidoP = entry_apellidoP.get()
            apellidoM = entry_apellidoM.get()
            celular = entry_celular.get()
            email = entry_email.get()
            direccion = entry_direccion.get()
            password = entry_password.get()

            Cliente.modificarCliente(cursor, conexion, id_cliente, nombre, apellidoP, apellidoM, celular, email, direccion, password)
            
            formulario_window.destroy()
            actualizar_tabla_clientes()

        formulario_window = tk.Toplevel()
        formulario_window.title("Modificar Cliente")
        formulario_window.geometry("400x300")
        formulario_window.config(bg="lightgrey")

        tk.Label(formulario_window, text="Nombre:", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_window)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Apellido Paterno:", bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
        entry_apellidoP = tk.Entry(formulario_window)
        entry_apellidoP.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Apellido Materno:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
        entry_apellidoM = tk.Entry(formulario_window)
        entry_apellidoM.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Celular:", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
        entry_celular = tk.Entry(formulario_window)
        entry_celular.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Email:", bg="lightgrey").grid(row=4, column=0, padx=5, pady=5)
        entry_email = tk.Entry(formulario_window)
        entry_email.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Dirección:", bg="lightgrey").grid(row=5, column=0, padx=5, pady=5)
        entry_direccion = tk.Entry(formulario_window)
        entry_direccion.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Contraseña:", bg="lightgrey").grid(row=6, column=0, padx=5, pady=5)
        entry_password = tk.Entry(formulario_window, show='*')
        entry_password.grid(row=6, column=1, padx=5, pady=5)

        btn_modificar = tk.Button(formulario_window, text="Modificar", command=modificar)
        btn_modificar.grid(row=7, columnspan=2, pady=10)

        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_cliente,))
        cliente = cursor.fetchone()
        if cliente:
            entry_nombre.insert(0, cliente[1])
            entry_apellidoP.insert(0, cliente[2])
            entry_apellidoM.insert(0, cliente[3])
            entry_celular.insert(0, cliente[4])
            entry_email.insert(0, cliente[5])
            entry_direccion.insert(0, cliente[6])
            entry_password.insert(0, cliente[8])

    def on_modificar():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            id_cliente = item_values[0]
            abrir_formulario_modificar_cliente(id_cliente)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para modificar.")

    def on_eliminar():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            id_cliente = item_values[0]
            confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que deseas eliminar el cliente con ID {id_cliente}?")
            if confirmacion:
                Cliente.eliminar_cliente(cursor, conexion, id_cliente)
                actualizar_tabla_clientes()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para eliminar.")

    ventana_clientes = tk.Toplevel()
    ventana_clientes.title("Clientes")
    ventana_clientes.geometry("600x400")
    ventana_clientes.config(bg="lightgrey")

    title_label = tk.Label(ventana_clientes, text="CLIENTES", font=("Arial", 24, "bold"), bg="lightgrey")
    title_label.pack(pady=10)

    frame_table = tk.Frame(ventana_clientes, bg="lightgrey")
    frame_table.pack(fill="both", expand=True, padx=10, pady=10)

    cols = ["ID", "NOMBRE", "APELLIDO P", "APELLIDO M", "CELULAR", "EMAIL", "DIRECCIÓN"]
    tree = ttk.Treeview(frame_table, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col, anchor='center')
        tree.column(col, anchor='center', width=120)
    tree.pack(fill="both", expand=True)

    actualizar_tabla_clientes()

    frame_buttons = tk.Frame(ventana_clientes, bg="lightgrey")
    frame_buttons.pack(fill="x", padx=10, pady=10)

    btn_añadir = tk.Button(frame_buttons, text="AÑADIR", font=("Arial", 12, "bold"), bg="grey", command=abrir_formulario_agregar_cliente)
    btn_añadir.pack(side="left", padx=10)

    btn_modificar = tk.Button(frame_buttons, text="MODIFICAR", font=("Arial", 12, "bold"), bg="grey", command=on_modificar)
    btn_modificar.pack(side="left", padx=10)
    
    btn_eliminar = tk.Button(frame_buttons, text="ELIMINAR", font=("Arial", 12, "bold"), bg="grey", command=on_eliminar)
    btn_eliminar.pack(side="left", padx=10)

def abrir_ventana_empleados():
    def actualizar_tabla_empleados():
        for item in tree.get_children():
            tree.delete(item)
        
        empleados = Empleado.listarEmpleados(cursor)
        for empleado in empleados:
            tree.insert("", tk.END, values=empleado)

    def abrir_formulario_agregar_empleado():
        def agregar():
            nombre = entry_nombre.get()
            apellidoP = entry_apellidoP.get()
            apellidoM = entry_apellidoM.get()
            celular = entry_celular.get()
            email = entry_email.get()
            direccion = entry_direccion.get()
            salario = entry_salario.get()
            cargo = entry_cargo.get()
            password = entry_password.get()

            empleado = Empleado(nombre, apellidoP, apellidoM, celular, email, direccion, salario, cargo, password)
            empleado.registrar_empleado(cursor, conexion, nombre, apellidoP, apellidoM, celular, email, direccion, salario, cargo, password)

            formulario_window.destroy()
            actualizar_tabla_empleados()

        formulario_window = tk.Toplevel()
        formulario_window.title("Agregar Empleado")
        formulario_window.geometry("400x500")
        formulario_window.config(bg="lightgrey")

        tk.Label(formulario_window, text="Nombre:", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_window)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Apellido Paterno:", bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
        entry_apellidoP = tk.Entry(formulario_window)
        entry_apellidoP.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Apellido Materno:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
        entry_apellidoM = tk.Entry(formulario_window)
        entry_apellidoM.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Celular:", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
        entry_celular = tk.Entry(formulario_window)
        entry_celular.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Email:", bg="lightgrey").grid(row=4, column=0, padx=5, pady=5)
        entry_email = tk.Entry(formulario_window)
        entry_email.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Dirección:", bg="lightgrey").grid(row=5, column=0, padx=5, pady=5)
        entry_direccion = tk.Entry(formulario_window)
        entry_direccion.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Salario:", bg="lightgrey").grid(row=6, column=0, padx=5, pady=5)
        entry_salario = tk.Entry(formulario_window)
        entry_salario.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Cargo:", bg="lightgrey").grid(row=7, column=0, padx=5, pady=5)
        entry_cargo = tk.Entry(formulario_window)
        entry_cargo.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Contraseña:", bg="lightgrey").grid(row=8, column=0, padx=5, pady=5)
        entry_password = tk.Entry(formulario_window, show='*')
        entry_password.grid(row=8, column=1, padx=5, pady=5)

        btn_agregar = tk.Button(formulario_window, text="Agregar", command=agregar)
        btn_agregar.grid(row=9, columnspan=2, pady=10)

    def abrir_formulario_modificar_empleado(id_empleado):
        def modificar():
            nombre = entry_nombre.get()
            apellidoP = entry_apellidoP.get()
            apellidoM = entry_apellidoM.get()
            celular = entry_celular.get()
            email = entry_email.get()
            direccion = entry_direccion.get()
            salario = entry_salario.get()
            cargo = entry_cargo.get()
            password = entry_password.get()

            empleado = Empleado(nombre, apellidoP, apellidoM, celular, email, direccion, salario, cargo, password)
            empleado.id_empleado = id_empleado
            empleado.modificar_empleado(cursor, conexion)

            formulario_window.destroy()
            actualizar_tabla_empleados()

        formulario_window = tk.Toplevel()
        formulario_window.title("Modificar Empleado")
        formulario_window.geometry("400x500")
        formulario_window.config(bg="lightgrey")

        tk.Label(formulario_window, text="Nombre:", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_window)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Apellido Paterno:", bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
        entry_apellidoP = tk.Entry(formulario_window)
        entry_apellidoP.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Apellido Materno:", bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
        entry_apellidoM = tk.Entry(formulario_window)
        entry_apellidoM.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Celular:", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
        entry_celular = tk.Entry(formulario_window)
        entry_celular.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Email:", bg="lightgrey").grid(row=4, column=0, padx=5, pady=5)
        entry_email = tk.Entry(formulario_window)
        entry_email.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Dirección:", bg="lightgrey").grid(row=5, column=0, padx=5, pady=5)
        entry_direccion = tk.Entry(formulario_window)
        entry_direccion.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Salario:", bg="lightgrey").grid(row=6, column=0, padx=5, pady=5)
        entry_salario = tk.Entry(formulario_window)
        entry_salario.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Cargo:", bg="lightgrey").grid(row=7, column=0, padx=5, pady=5)
        entry_cargo = tk.Entry(formulario_window)
        entry_cargo.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(formulario_window, text="Contraseña:", bg="lightgrey").grid(row=8, column=0, padx=5, pady=5)
        entry_password = tk.Entry(formulario_window, show='*')
        entry_password.grid(row=8, column=1, padx=5, pady=5)

        btn_modificar = tk.Button(formulario_window, text="Modificar", command=modificar)
        btn_modificar.grid(row=9, columnspan=2, pady=10)

        cursor.execute("SELECT * FROM empleados WHERE id_empleado = %s", (id_empleado,))
        empleado = cursor.fetchone()
        if empleado:
            entry_nombre.insert(0, empleado[1])
            entry_apellidoP.insert(0, empleado[2])
            entry_apellidoM.insert(0, empleado[3])
            entry_celular.insert(0, empleado[4])
            entry_email.insert(0, empleado[5])
            entry_direccion.insert(0, empleado[6])
            entry_salario.insert(0, empleado[7])
            entry_cargo.insert(0, empleado[8])
            # Nota: La contraseña no se muestra por seguridad, pero puedes permitir al usuario cambiarla si es necesario

    def on_modificar():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            id_empleado = item_values[0]
            abrir_formulario_modificar_empleado(id_empleado)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para modificar.")

    def on_eliminar():
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, 'values')
            id_empleado = item_values[0]

            confirm = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este empleado?")
            if confirm:
                empleado = Empleado(None, None, None, None, None, None, None, None, None)
                empleado.eliminar_empleado(cursor, conexion)
                actualizar_tabla_empleados()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un empleado para eliminar.")

    ventana_empleados = tk.Toplevel()
    ventana_empleados.title("Empleados")
    ventana_empleados.geometry("600x400")
    ventana_empleados.config(bg="lightgrey")

    # Título
    title_label = tk.Label(ventana_empleados, text="EMPLEADOS", font=("Arial", 24, "bold"), bg="lightgrey")
    title_label.pack(pady=10)

    # Frame para la tabla de empleados
    frame_table = tk.Frame(ventana_empleados, bg="lightgrey")
    frame_table.pack(fill="both", expand=True, padx=10, pady=10)

    # Tabla de empleados
    cols = ["CODIGO", "NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO", "CELULAR"]
    tree = ttk.Treeview(frame_table, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col, anchor='center')
        tree.column(col, anchor='center', width=100)
    tree.pack(fill="both", expand=True)

    # Frame para los botones de acción
    frame_buttons = tk.Frame(ventana_empleados, bg="lightgrey")
    frame_buttons.pack(fill="x", padx=10, pady=10)

    # Botones de acción
    btn_añadir = tk.Button(frame_buttons, text="AÑADIR", font=("Arial", 12, "bold"), bg="grey", command=abrir_formulario_agregar_empleado)
    btn_añadir.pack(side="left", padx=10)

    btn_modificar = tk.Button(frame_buttons, text="MODIFICAR", font=("Arial", 12, "bold"), bg="grey", command=on_modificar)
    btn_modificar.pack(side="left", padx=10)

    btn_eliminar = tk.Button(frame_buttons, text="ELIMINAR", font=("Arial", 12, "bold"), bg="grey", command=on_eliminar)
    btn_eliminar.pack(side="left", padx=10)

    actualizar_tabla_empleados()
# Función para completar la venta
def completar_venta():
    messagebox.showinfo("Venta completada!")

# Función para cambiar a pantalla completa o salir de ella
def toggle_fullscreen(root, event=None):
    is_fullscreen = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not is_fullscreen)

# Función para salir del modo de pantalla completa
def exit_fullscreen(root, event=None):
    root.attributes('-fullscreen', False)

# Ventana de login
login_window = tk.Tk()
login_window.title("Inicio de Sesión")
login_window.geometry("300x200")

# Etiquetas y entradas de texto para email y password
tk.Label(login_window, text="Email:").pack(pady=5)
email_entry = tk.Entry(login_window)
email_entry.pack()

tk.Label(login_window, text="Password:").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Botón de login
login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=20)

login_window.mainloop()
