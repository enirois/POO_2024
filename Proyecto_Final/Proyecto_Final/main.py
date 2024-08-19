from db import *  # Importa todo desde db.py (o importa funciones específicas si es posible)
from funciones import *  # Importa todo desde funciones.py (o importa funciones específicas si es posible)
from Modelos.modelos import *  # Importa todo desde modelos.py en la carpeta Modelos
from hashlib import sha256
import getpass
import bcrypt

def login():
    while True:
        print("\n--- LOGIN ---")
        email = input("Ingrese su email: ")
        password = input("Ingrese su contraseña: ")
        
        # Verificar si el usuario existe en la tabla usuarios
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        
        if usuario:
            tipo_usuario = usuario[7]  # El tipo de usuario está en la posición 7
            hashed_password = usuario[8]  # El hash de la contraseña está en la posición 8
            
            # Verificar la contraseña ingresada con la hasheada
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                if tipo_usuario == 'cliente':
                    cliente_menu(usuario)
                elif tipo_usuario == 'empleado':
                    empleado_menu(usuario)
            else:
                print("Contraseña incorrecta.")
        else:
            print("Usuario no encontrado.")


# Función para registrar un cliente
def registrar_cliente():
    cliente = Cliente(None, None, None, None, None, None, None, None)
    cliente.registrarCliente(cursor, conexion)
    if cliente:
        print("Cliente registrado exitosamente.")
    else:
        print("Error al registrar el cliente.")

# Funciones para clientes y empleados

def cliente_menu(cliente):
    while True:
        print("\n--- MENÚ CLIENTE ---")
        print("1. Ver productos y comprar")
        print("2. Ver servicios y hacer un pedido")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            productos = Productos()
            productos.listar_productos(cursor)
            
        elif opcion == "2":
            servicios = Servicios()
            servicios.listarServicios(cursor)
            
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def empleado_menu(empleado):
    while True:
        print("\n--- MENÚ EMPLEADO ---")
        print("1. Registrar Producto")
        print("2. Eliminar Producto")
        print("3. Modificar Producto")
        print("4. Listar Productos")
        print("5. Registrar Servicio")
        print("6. Eliminar Servicio")
        print("7. Modificar Servicio")
        print("8. Listar Servicios")
        print("9. Modificar Cliente")
        print("10. Eliminar Cliente")
        print("11. Listar Clientes")
        print("12. Ver Pedidos")
        print("13. Ver Ventas Hechas")
        print("14. Registrar otro Empleado")
        print("15. Modificar Empleado")
        print("16. Eliminar Empleado")
        print("17. Listar Empleados")
        print("18. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = Productos(None, None, None, None, None, None)
            producto.agregar_producto()
            print("Producto registrado exitosamente.")

        elif opcion == "2":
            producto = Productos(None, None, None, None, None, None)
            producto.eliminar_producto(cursor, conexion)
            print("Producto eliminado.")

        elif opcion == "3":
            producto = Productos(None, None, None, None, None, None)
            producto.modificar_producto(cursor, conexion)
            print("Producto modificado.")

        elif opcion == "4":
            productos = Productos.listar_productos(cursor)

        elif opcion == "5":
            servicio = Servicios(None, None, None, None)
            servicio.agregar_servicio(cursor, conexion)
            print("Servicio registrado exitosamente.")

        elif opcion == "6":
            servicio = Servicios(None, None, None, None)
            servicio.eliminar_servicio(cursor, conexion)
            print("Servicio eliminado.")

        elif opcion == "7":
            servicio = Servicios(None, None, None, None)
            servicio.modificar_servicio(cursor, conexion)
            print("Servicio modificado.")

        elif opcion == "8":
            servicios = Servicios.listarServicios(cursor)
            for servicio in servicios:
                print(f"Código: {servicio[0]}, Nombre: {servicio[1]}, Precio: {servicio[3]}")

        elif opcion == "9":
            cliente = Cliente(None, None, None, None, None, None, None)
            cliente.modificarCliente(cursor, conexion)
            print("Cliente modificado.")

        elif opcion == "10":
            cliente = Cliente(None, None, None, None, None, None, None)
            cliente.eliminar_cliente(cursor, conexion)
            print("Cliente eliminado.")

        elif opcion == "11":
            clientes = Cliente.listarClientes(cursor)

        elif opcion == "12":
            pedidos = Pedido.listar_pedidos(cursor)

        elif opcion == "13":
            ventas = Venta.listar_ventas(cursor)
        elif opcion == "14":
            empleado = Empleado(None, None, None, None, None, None, None, None, None)
            empleado.registrar_empleado(cursor, conexion)
            print("Empleado registrado exitosamente.")

        elif opcion == "15":
            empleado = Empleado(None, None, None, None, None, None, None, None, None)
            empleado.modificar_empleado(cursor, conexion)
            print("Empleado modificado.")

        elif opcion == "16":
            empleado = Empleado(None, None, None, None, None, None, None, None, None)
            empleado.eliminar_empleado(cursor, conexion)
            print("Empleado eliminado.")

        elif opcion == "17":
            empleados = Empleado.listarEmpleados(cursor)

        elif opcion == "18":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intente de nuevo.")


# Menú principal
def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Login")
        print("2. Registrar (solo clientes)")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            login()
        
        elif opcion == "2":
            registrar_cliente()
        
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")


