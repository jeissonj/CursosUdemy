# Seccion para las funciones


def op_llaves(l):
    llaves = []
    for j in l[0]:
        llaves.append(list(j.keys())[0])
    return llaves


def op_valores(lt):
    valores = []
    for j in lt:
        valores.append(j[2]["precio"])
    return valores


def mostrar_menu(l, llaves):
    print("Snacks disponibles")
    for i in l:
        print(
            f"\t   Id: {i[0][llaves[0]]} -> {i[1][llaves[1]]} - Precio: {i[2][llaves[2]]}"
        )
    print(""" Menu:
        1. Comprar Snacks
        2. Mostrat ticket
        3. Salir
    """)
    x = input("Escoge una opcion: ")
    return x


def actualizar_pedido(pedido, l):
    x = int(input("¿Qué snack quires? (id):  "))
    pedido[x] += 1
    print(f"Ok, snaks agregado: {l[x]}")


def mostrar_tiket(pedido, valores, lt, llaves):
    print("*** Tcket de venta ***")
    suma = 0
    suma_tem = 0
    for i in range(len(valores)):
        if 0 != pedido[i]:
            suma_tem = pedido[i] * valores[i]
            suma += suma_tem
            print(f" - {lt[i][1][llaves[1]]} - {suma_tem}\n")
    print(f"Total -> {suma}")
