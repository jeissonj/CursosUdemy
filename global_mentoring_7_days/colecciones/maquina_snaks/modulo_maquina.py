# Modulo de maquina de esnaks
# la idea es coloacr aca todas las funciones así de una vez ensayar lo de los modulos
def llenar_lista(key,lista):
    for i in key:
        lista[i] = 0
    return lista


def consulta(l, lista):
    pedir = input(
        "Si desea ordenar un producto ingrese el numero 1, si no ingrese el 2: "
    )
    if pedir == "1":
        lis = mostrar_productos(l, lista)
    elif pedir == "2":
        if lista != {}:
        print("La lista de los productos con sus precios es \n")
        # y acá coloco la lista 
                     
        print("Para una proxima ")
    else:
        print("Opccion erronea ")
        return lis


def mostrar_productos(l, lista):
    print(f"los productos disponibles son {list(l.keys())} ")
    print(f"Y Los codigos para pedirlos son {list(l.values())} ")
    lista.append(input("Ingrese el codigo del producto que desea pedir "))
    return lista


# def modifir_productp
