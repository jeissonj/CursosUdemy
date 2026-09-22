import modulo2_maquina as m2

print("*** Maquina de Snks ***")

lista1 = [{"id": 0}, {"nombre": "Papas"}, {"precio": 300}]
lista2 = [{"id": 1}, {"nombre": "Refresco"}, {"precio": 50}]
lista3 = [{"id": 2}, {"nombre": "Sandwich"}, {"precio": 120}]
lt = [lista1, lista2, lista3]
llaves = []
llaves = m2.op_llaves(lt)
valores = m2.op_valores(lt)
pedido = [0] * len(lt)
opcion = 0
bucle = True
while bucle:
    opcion = m2.mostrar_menu(lt, llaves)
    if opcion == "3":
        print("*** Un gusto servirte, bye bye!!! ***")
        bucle = False
    elif opcion == "1":
        m2.actualizar_pedido(pedido, lt)
    elif opcion == "2":
        m2.mostrar_tiket(pedido, valores, lt, llaves)
