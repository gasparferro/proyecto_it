from datetime import datetime

def registro_entrada_salida(nombre_encargado, modo):
    fecha_actual = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    registro = f"{modo} {fecha_actual} Encargad@ {nombre_encargado}"

    if modo == "OUT":
        registro += " $"

    registro += "\n##################################################\n"

    with open("C:/Users/gaspa/OneDrive/Escritorio/python/ed-it/reto1/registro.txt", "a") as archivo:
        archivo.write(registro)


def guardar_registro_ventas(nombre_cliente, fecha, combo_s, combo_d, combo_t, flurby, total):
    registro_venta = f"{nombre_cliente}, {fecha}, {combo_s}, {combo_d}, {combo_t}, {flurby}, {total}\n"

    with open("C:/Users/gaspa/OneDrive/Escritorio/python/ed-it/reto1/ventas.txt", "a") as archivo:
        archivo.write(registro_venta)



def ingresar_pedido():
    print("--- Ingreso nuevo pedido ---")
    nombre_cliente = input("Ingrese nombre del cliente: ")
    cantidad_combo_s = int(input("Ingrese cantidad Combo S: "))
    cantidad_combo_d = int(input("Ingrese cantidad Combo D: "))
    cantidad_combo_t = int(input("Ingrese cantidad Combo T: "))
    cantidad_flurby = int(input("Ingrese cantidad Flurby: "))

    # Cálculo del total
    precio_combo_s = 10.99
    precio_combo_d = 12.99
    precio_combo_t = 14.99
    precio_flurby = 5.99

    total = (cantidad_combo_s * precio_combo_s) + (cantidad_combo_d * precio_combo_d) + \
            (cantidad_combo_t * precio_combo_t) + (cantidad_flurby * precio_flurby)

    print("Total $", total)

    # Proceso de pago
    abono = float(input("Abona con $ "))
    vuelto = abono - total
    print("Vuelto $", vuelto)

    # Confirmación del pedido
    confirmacion = input("¿Confirma pedido? (Y/N): ")
    if confirmacion.upper() == "Y":
        # Crear una cadena con los datos a guardar
        fecha_actual = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        guardar_registro_ventas(nombre_cliente, fecha_actual, cantidad_combo_s, cantidad_combo_d, cantidad_combo_t, cantidad_flurby, total)

        print("Pedido confirmado. ¡Gracias!")
    else:
        print("Pedido cancelado.")


def menu_principal(nombre_encargado):
    print("Hamburguesas IT")
    print("Encargado ->", nombre_encargado)
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :)")

    while True:
        print("\n--- Menú ---")
        print("1 - Ingreso nuevo pedido")
        print("2 - Cambio de turno")
        print("3 - Apagar sistema")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            ingresar_pedido()

        elif opcion == "2":
            registro_entrada_salida(nombre_encargado, "OUT")
            nombre_encargado = input("Ingrese su nombre encargado: ")
            registro_entrada_salida(nombre_encargado, "IN")
        
        elif opcion == "3":
            registro_entrada_salida(nombre_encargado, "OUT")
            break
        
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

    print("¡Hasta luego!")


print("Bienvenido a Hamburguesas IT")
nombre_encargado = input("Ingrese su nombre encargado: ")
registro_entrada_salida(nombre_encargado, "IN")
menu_principal(nombre_encargado)

