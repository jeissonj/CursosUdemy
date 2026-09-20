# Modulo de maquina de esnaks
# la idea es coloacr aca todas las funciones así de una vez ensayar lo de los modulos
def llenar_lista(key, dlista):
    for i in key:
        dlista[i] = 0
    return dlista


def calculo_valor(dlista, precios):
    mul = 0
    for i in dlista.keys():
        mul += dlista[i] * precios[i]
    return mul


def consulta(lp, dlista, precios):
    ordenar = True
    while ordenar:
        pedir = input(
            "Si desea ordenar un producto ingrese el numero 1, si no, ingrese el 2: "
        )
        if pedir == "1":
            dlis = mostrar_productos(lp, dlista)
        elif pedir == "2":
            # Cómo es un diccionario necesitamos saber si la suma de los values es cero
            valor = calculo_valor(dlista, precios)
            if valor != 0:
                print("La lista de los productos con sus precios es \n")
                for i in list(lp.keys()):
                    if dlista[i] != 0:
                        print(f"{dlista[i]} {lp[i]} ... {precios[i]}")
                print(f"El costo total de la transacción es {valor}")
            print("Para una proxima ")
            ordenar = False
        else:
            print("Opccion erronea ")


def mostrar_productos(lp, dlista):
    print(f"los productos disponibles son {list(lp.keys())} ")
    print(f"Y Los codigos para pedirlos son {list(lp.values())} ")
    x = input("Ingrese el codigo del producto que desea pedir ")
    if x in lp.keys():
        dlista[x] += 1
    else:
        print("El codigo ingresado es errroneo")
    return dlista


# def modifir_productp
