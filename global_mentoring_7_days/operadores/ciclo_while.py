# Menu interactivo ciclo while

print("*** Sistema de Administración de ciuentas ***")
salir = False

while not salir:
    print(f"""Menu 
          1. Crear cuenta 
          2. Eliminar cuenta 
          3. Salir""")
    opcion = int(input("Escoje una opcion: "))
    if opcion == 1:
        print("Creando tu cuenta \n")
    elif opcion == 2:
        print("Eliminando  cuenta \n")
    elif opcion == 3:
        print(print("Saliendo del siistema . Hasta ponto ...\n"))
        salir = True
    else:
        print("Opcion invalida, selecciona otra opción...")
