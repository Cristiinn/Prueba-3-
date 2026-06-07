print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

stock_inicial = 120
prestamos = 0
total_prestamos = 0

while True:

    print("\n--- MENÚ BIBLIOTECA ---")
    print("1. Libros disponibles")
    print("2. Realizar prestamo")
    print("3. Devolver prestamo")
    print("4. Historial de prestamos")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print(f"Libros disponibles: {stock_inicial}")

        elif opcion == 2:

            while True:
                try:
                    cantidad_prestamo = int(
                        input("Ingrese la cantidad de libros que desea solicitar: "))

                    if cantidad_prestamo <= 0:
                        print("Debe ingresar una cantidad mayor a 0.")

                    elif cantidad_prestamo > stock_inicial:
                        print("No hay stock disponible para la cantidad de libros solicitados :(")

                    else:
                        stock_inicial -= cantidad_prestamo
                        prestamos += cantidad_prestamo
                        total_prestamos += cantidad_prestamo

                        print("Cantidad de libros solicitada ingresada correctamente.")
                        break

                except:
                    print("Ingrese un número entero válido.")

        elif opcion == 3:

            while True:
                try:
                    librosA_devolver = int(
                        input("Ingrese la cantidad de libros a devolver: "))

                    if librosA_devolver <= 0:
                        print("La cantidad de libros a devolver debe ser mayor a 0.")

                    elif stock_inicial + librosA_devolver > 120:
                        print(
                            "La cantidad de libros a devolver no puede superar la capacidad máxima de la biblioteca."
                        )

                    else:
                        stock_inicial += librosA_devolver
                        prestamos -= librosA_devolver

                        print(f"{librosA_devolver} libros devueltos correctamente.")
                        break

                except:
                    print("Ingrese un número entero válido.")

        elif opcion == 4:
            print(f"Préstamos activos: {prestamos}")
            print(f"Total de préstamos realizados: {total_prestamos}")

        elif opcion == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break

        else:
            print("Debe seleccionar una opción válida.")

    except:
        print("Ingrese un número entero válido.")
