# programa para hacer el ejercicio del cajero automatico
print("***  Cajero automarico de ciudad gotica ***")

salir = True
opcion = 0
saldo = 10000
modificacion = 0

while salir:
    print(f"""Operaciones que puedes realizar:
        1. Consultar saldo
        2. Retirar 
        3. Depositar 
        4. Salir 
        Escoja una opción: """)
    opcion = int(input())
    if opcion == 1:
        print(f"Su saldo es de {saldo}")
    elif opcion == 2:
        modificacion = int(input("Ingrese saldo a retirar: "))
        if saldo >= modificacion:
            saldo -= modificacion
        else:
            print("No cuentas con el saldo suficiente")
    elif opcion == 3:
        modificacion = int(input("Ingrese saldo a depositar: "))
        saldo += modificacion
    elif opcion == 4:
        print("Gracias por visitarnos hasta luego")
        salir = False
    else:
        print("Error, Seleccione una de las opciones indicadas")
