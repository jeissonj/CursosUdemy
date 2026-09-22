# Seccion para las funciones


def op_llaves(l):
    llaves = []
    for j in l[0]:
        llaves.append(list(j.keys())[0])
    return llaves


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


def actualizar_pedido(pedido):
    x = input("¿Qué snack quires? (id):  ")
    pedido[x] += 1
