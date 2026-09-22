import modulo_2maquina as m2

print("*** Maquina de Snks ***")

lista1 = [{"id": 0}, {"nombre": "Papas"}, {"precio": 300}]
lista2 = [{"id": 1}, {"nombre": "Refresco"}, {"precio": 50}]
lista3 = [{"id": 2}, {"nombre": "Sandwich"}, {"precio": 120}]
lt = [lista1, lista2, lista3]
llaves = []
llaves = m2.op_llaves(lt)
pedido = dict.fromkeys(llaves, 0)
opcion = 0
bucle = True
while bucle:
    opcion = m2.mostrar_menu(lt, llaves)
    if opcion == "3":
        bucle = False
    elif opcion = "1":
        m2.actualizar_pedido(pedido)


