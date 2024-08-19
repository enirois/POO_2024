import bcrypt
import hashlib
from datetime import datetime
import mysql.connector
import tkinter as tk
from tkinter import messagebox

try:
    # Conectar con la BD en MySQL
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bisuteria_db'
    )
    # Crear un objeto de tipo cursor que tenga un parámetro que permita reutilizar el objeto 
    cursor = conexion.cursor(buffered=True)
except:
    messagebox.showerror(f"Ocurrió un error con el Sistema, por favor verifique...")    


class Usuario:
    def __init__(self, nombre, apellidoP, apellidoM, celular, email, direccion, tipo_usuario, password=None):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.celular = celular
        self.email = email
        self.direccion = direccion
        self.tipo_usuario = tipo_usuario
        self.password = self.hash_password(password) if password else None

    def registrar_usuario(self, cursor, conexion):
        if self.password:
            # Hashear la contraseña
            hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Insertar en la tabla de usuarios
            cursor.execute('''
                INSERT INTO usuarios (nombre, apellidoP, apellidoM, celular, email, direccion, tipo_usuario, contraseña_hash)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (self.nombre, self.apellidoP, self.apellidoM, self.celular, self.email, self.direccion, self.tipo_usuario, hashed_password))

            conexion.commit()
            messagebox.showinfo(f"{self.tipo_usuario.capitalize()} registrado exitosamente con email: {self.email}")
        else:
            print("Error: No se puede registrar un usuario sin contraseña.")
            messagebox.showerror("Error: No se puede registrar un usuario sin contraseña")

    @staticmethod
    def verificar_login(cursor, email, password_ingresada):
        cursor.execute("SELECT contraseña_hash FROM usuarios WHERE email = %s", (email,))
        resultado = cursor.fetchone()

        if resultado:
            hashed_password = resultado[0]
            # Verificar la contraseña ingresada con la hasheada
            if bcrypt.checkpw(password_ingresada.encode('utf-8'), hashed_password.encode('utf-8')):
                print("Login exitoso")
                return True
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario no encontrado")
        return False
    
    def hash_password(self, password):
        # Generar el hash de la contraseña
        return hashlib.sha256(password.encode()).hexdigest()

    def verificar_password(self, password):
        # Verificar si la contraseña ingresada coincide con el hash almacenado
        return self.hash_password(password) == self.password


class Empleado(Usuario):
    def __init__(self, nombre, apellidoP, apellidoM, celular, email, direccion, salario, cargo, password):
        super().__init__(nombre, apellidoP, apellidoM, celular, email, direccion, 'empleado', password)
        self.salario = salario
        self.cargo = cargo

    def registrar_empleado(self, cursor, conexion):
        # Hash de la contraseña
        contraseña_hash = bcrypt.hashpw(self.contraseña.encode('utf-8'), bcrypt.gensalt())

        query = """INSERT INTO empleados (nombre, apellidoP, apellidoM, celular, email, direccion, salario, cargo, contraseña_hash)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (self.nombre, self.apellidoP, self.apellidoM, self.celular, self.email, self.direccion, self.salario, self.cargo, contraseña_hash)

        cursor.execute(query, values)
        conexion.commit()

    def modificar_empleado(self, cursor, conexion):
        # Hash de la contraseña si se ha cambiado
        if self.contraseña:
            contraseña_hash = bcrypt.hashpw(self.contraseña.encode('utf-8'), bcrypt.gensalt())
            query = """UPDATE empleados
                       SET nombre = %s, apellidoP = %s, apellidoM = %s, celular = %s, email = %s, direccion = %s, salario = %s, cargo = %s, contraseña_hash = %s
                       WHERE id_empleado = %s"""
            values = (self.nombre, self.apellidoP, self.apellidoM, self.celular, self.email, self.direccion, self.salario, self.cargo, contraseña_hash, self.id_empleado)
        else:
            query = """UPDATE empleados
                       SET nombre = %s, apellidoP = %s, apellidoM = %s, celular = %s, email = %s, direccion = %s, salario = %s, cargo = %s
                       WHERE id_empleado = %s"""
            values = (self.nombre, self.apellidoP, self.apellidoM, self.celular, self.email, self.direccion, self.salario, self.cargo, self.id_empleado)

        cursor.execute(query, values)
        conexion.commit()

    def eliminar_empleado(self, cursor, conexion):
        query = """DELETE FROM empleados WHERE id_empleado = %s"""
        cursor.execute(query, (self.id_empleado,))
        conexion.commit()

    @staticmethod
    def listarEmpleados(cursor):
        query = """SELECT * FROM empleados"""
        cursor.execute(query)
        return cursor.fetchall()
        while True:
            Empleado.listarEmpleados(cursor)
            
            empleado_id = input("Ingrese el ID del empleado que desea eliminar o '0' para cancelar: ")

            if empleado_id.isdigit():
                empleado_id = int(empleado_id)
                if empleado_id == 0:
                    print("Cancelando operación de eliminación.")
                    break
                
                cursor.execute("SELECT * FROM empleados WHERE id_empleado = %s", (empleado_id,))
                empleado = cursor.fetchone()
                
                if empleado:
                    cursor.execute("DELETE FROM empleados WHERE id_empleado = %s", (empleado_id,))
                    conexion.commit()
                    print(f"Empleado con ID {empleado_id} eliminado correctamente.")
                    break
                else:
                    print("Empleado no encontrado.")
            else:
                print("ID no válido. Por favor, ingrese un número válido.")

class Cliente(Usuario):
    def __init__(self, nombre, apellidoP, apellidoM, celular, email, direccion, id_cliente, password):
        super().__init__(nombre, apellidoP, apellidoM, celular, email, direccion, 'cliente', password)
        self.id_cliente = id_cliente

    def registrarCliente(self, cursor, conexion, nombre, apellidoP, apellidoM, celular, email, direccion, password):
        # Hashear la contraseña
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Registrar primero en la tabla usuarios
        cursor.execute('''
            INSERT INTO usuarios (email, contraseña_hash, tipo_usuario)
            VALUES (%s, %s, %s)
        ''', (email, hashed_password, 'cliente'))

        # Ahora registrar en la tabla clientes
        cursor.execute('''
            INSERT INTO clientes (nombre, apellidoP, apellidoM, celular, email, direccion)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (nombre, apellidoP, apellidoM, celular, email, direccion))

        conexion.commit()

        # Obtén el ID auto-incrementado
        self.id_cliente = cursor.lastrowid


    @staticmethod
    def listarClientes(cursor):
        cursor.execute("SELECT id_cliente, nombre FROM clientes")
        return cursor.fetchall()

    def modificarCliente(self, cursor, conexion, id_cliente, nombre=None, apellidoP=None, apellidoM=None, celular=None, email=None, direccion=None, password=None):
        if password:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            cursor.execute('''
                UPDATE usuarios
                SET contraseña_hash = %s
                WHERE email = %s
            ''', (hashed_password, email))

        # Modificar los datos del cliente
        cursor.execute('''
            UPDATE clientes
            SET nombre = %s, apellidoP = %s, apellidoM = %s, celular = %s, email = %s, direccion = %s
            WHERE id_cliente = %s
        ''', (nombre, apellidoP, apellidoM, celular, email, direccion, id_cliente))

        conexion.commit()

    def eliminar_cliente(self, cursor, conexion, id_cliente):
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_cliente,))
        cursor.execute("DELETE FROM usuarios WHERE email = (SELECT email FROM clientes WHERE id_cliente = %s)", (id_cliente,))
        conexion.commit()

class Productos():
    def __init__(self, codigo=None, nombre=None, descripcion=None, cantidad=None, precio_compra=None, precio_venta=None):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta

    def agregar_producto(nombre, descripcion, cantidad, precio_compra, precio_venta, cursor, conexion):
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio_compra, precio_venta)
            VALUES (%s, %s, %s, %s, %s)
        ''', (nombre, descripcion, cantidad, precio_compra, precio_venta))

        conexion.commit()

        codigo = cursor.lastrowid
        print("Producto registrado exitosamente con código:", codigo)
        return codigo

    @staticmethod
    def listar_productos(cursor):
        cursor.execute("SELECT codigo, nombre, cantidad, precio_venta FROM productos")
        return cursor.fetchall()


    def modificar_producto(codigo, nombre, descripcion, cantidad, precio_compra, precio_venta, cursor, conexion):
        cursor.execute('''
            UPDATE productos
            SET nombre = %s, descripcion = %s, cantidad = %s, precio_compra = %s, precio_venta = %s
            WHERE codigo = %s
        ''', (nombre, descripcion, cantidad, precio_compra, precio_venta, codigo))
        
        conexion.commit()
        print("Datos actualizados correctamente.")
        
    @staticmethod
    def eliminar_producto(codigo, cursor, conexion):
        cursor.execute("DELETE FROM productos WHERE codigo = %s", (codigo,))
        conexion.commit()
        print("Producto eliminado correctamente.")
        
    def agregar_cantidad(self, cursor, conexion):
        Productos.listar_productos(cursor)

        producto_codigo = input("Seleccione el código del producto al que desea agregar cantidad: ")

        if producto_codigo.isdigit():
            producto_codigo = int(producto_codigo)
            cursor.execute("SELECT cantidad FROM productos WHERE codigo = %s", (producto_codigo,))
            cantidad_actual = cursor.fetchone()

            if cantidad_actual:
                cantidad_a_agregar = int(input("Cantidad a agregar: "))
                nueva_cantidad = cantidad_actual[0] + cantidad_a_agregar
                cursor.execute("UPDATE productos SET cantidad = %s WHERE codigo = %s", (nueva_cantidad, producto_codigo))
                conexion.commit()
                print(f"Cantidad actualizada. Nueva cantidad: {nueva_cantidad}")
            else:
                print("Producto no encontrado.")
        else:
            print("Código no válido.")

    def modificar_cantidad(self, cursor, conexion):
        Productos.listar_productos(cursor)

        producto_codigo = input("Seleccione el código del producto al que desea modificar la cantidad: ")

        if producto_codigo.isdigit():
            producto_codigo = int(producto_codigo)
            nueva_cantidad = int(input("Nueva cantidad: "))
            cursor.execute("UPDATE productos SET cantidad = %s WHERE codigo = %s", (nueva_cantidad, producto_codigo))
            conexion.commit()
            print(f"Cantidad actualizada a: {nueva_cantidad}")
        else:
            print("Código no válido.")

class Servicios():
    def __init__(self, codigo = None, nombre = None, descripcion = None, precio = None):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    @staticmethod
    def agregar_servicio(nombre, descripcion, precio, cursor, conexion):
        cursor.execute('''
            INSERT INTO servicios (nombre, descripcion, precio)
            VALUES (%s, %s, %s)
        ''', (nombre, descripcion, precio))

        conexion.commit()
        codigo = cursor.lastrowid
        print("Servicio agregado exitosamente con Código:", codigo)
        return codigo

    @staticmethod
    def listar_servicios(cursor):
        cursor.execute("SELECT codigo, nombre, descripcion, precio FROM servicios")
        return cursor.fetchall()

    @staticmethod
    def modificar_servicio(codigo, nombre, descripcion, precio, cursor, conexion):
        cursor.execute('''
            UPDATE servicios
            SET nombre = %s, descripcion = %s, precio = %s
            WHERE codigo = %s
        ''', (nombre, descripcion, precio, codigo))
        
        conexion.commit()
        print("Datos actualizados correctamente.")

    @staticmethod
    def eliminar_servicio(codigo, cursor, conexion):
        cursor.execute("DELETE FROM servicios WHERE codigo = %s", (codigo,))
        conexion.commit()
        print("Servicio eliminado correctamente.")
        while True:
            Servicios.listarServicios(cursor)
            
            servicio_codigo = input("Ingrese el Código del servicio que desea eliminar o '0' para cancelar: ")

            if servicio_codigo.isdigit():
                servicio_codigo = int(servicio_codigo)
                if servicio_codigo == 0:
                    print("Cancelando operación de eliminación.")
                    break
                
                cursor.execute("SELECT * FROM servicios WHERE codigo = %s", (servicio_codigo,))
                servicio = cursor.fetchone()
                
                if servicio:
                    cursor.execute("DELETE FROM servicios WHERE codigo = %s", (servicio_codigo,))
                    conexion.commit()
                    print(f"Servicio con Código {servicio_codigo} eliminado correctamente.")
                    break
                else:
                    print("Servicio no encontrado.")
            else:
                print("Código no válido. Por favor, ingrese un número válido.")

class Venta:
    def __init__(self, productos, total):
        self.productos = productos
        self.total = total
        self.fecha = datetime.datetime.now()
        self.id = None

    def guardar(self):
        query = "INSERT INTO ventas (fecha, total) VALUES (?, ?)"
        self.id = cursor.ejecutar(query, (self.fecha, self.total))
        for producto in self.productos:
            cursor.ejecutar("INSERT INTO venta_productos (venta_id, producto_id) VALUES (?, ?)", (self.id, producto.id))

class Ticket:
    def __init__(self, venta_id, fecha):
        self.venta_id = venta_id
        self.fecha = fecha

    def guardar(self):
        query = "INSERT INTO tickets (venta_id, fecha) VALUES (?, ?)"
        cursor.ejecutar(query, (self.venta_id, self.fecha))
        
class Pedido:
    def __init__(self, id_pedido=None, cliente_id=None, fecha=None, estado=None, total=None):
        self.id_pedido = id_pedido
        self.cliente_id = cliente_id
        self.fecha = fecha if fecha else datetime.now()
        self.estado = estado if estado else "pendiente"  # Establece un estado predeterminado, como "pendiente"
        self.total = total

    def registrar_pedido(self, cursor, conexion, cliente_id, servicios):
        """
        Registra un nuevo pedido de servicios.
        :param cursor: objeto cursor para ejecutar consultas SQL.
        :param conexion: objeto conexión a la base de datos.
        :param cliente_id: ID del cliente que realiza el pedido.
        :param servicios: lista de tuplas (servicio_codigo, cantidad, precio_unitario).
        """
        # Calcular el total del pedido
        self.total = sum(cantidad * precio_unitario for _, cantidad, precio_unitario in servicios)
        
        # Insertar pedido en la base de datos
        cursor.execute('''
            INSERT INTO pedidos (id_cliente, fecha, estado)
            VALUES (%s, %s, %s)
        ''', (cliente_id, self.fecha, self.estado))
        
        self.id_pedido = cursor.lastrowid  # Obtener el ID del pedido recién insertado

        # Insertar detalles del pedido en la tabla de detalles de pedido
        for servicio_codigo, cantidad, precio_unitario in servicios:
            cursor.execute('''
                INSERT INTO detalles_pedido (pedido_id, servicio_codigo, cantidad, precio_unitario)
                VALUES (%s, %s, %s, %s)
            ''', (self.id_pedido, servicio_codigo, cantidad, precio_unitario))

        conexion.commit()
        print(f"Pedido registrado con éxito. ID del pedido: {self.id_pedido}")

    @staticmethod
    def listar_pedidos(cursor):
        """
        Lista todos los pedidos registrados.
        :param cursor: objeto cursor para ejecutar consultas SQL.
        """
        cursor.execute("SELECT id_pedido, id_cliente, fecha, estado FROM pedidos")
        pedidos = cursor.fetchall()
        if pedidos:
            print("Pedidos registrados:")
            for pedido in pedidos:
                print(f"ID: {pedido[0]}, Cliente ID: {pedido[1]}, Fecha: {pedido[2]}, Estado: {pedido[3]}")
        else:
            print("No hay pedidos registrados.")
