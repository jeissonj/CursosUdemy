# Manejo de cadenas

mi_cadena = "\tUbaldo \nAcosta"
# print(mi_cadena)

mensaje = "Hola Mundo"
# subcadena hola -> cadena[indice_inicio:indice_final + 1]
subcadena_hola = mensaje[0:4]
subcadena_mundo = mensaje[5:]  # tambíen se podría con [5:10]

# print(subcadena_hola, "\n", subcadena_mundo)

var_hola = "Hola"
var_mundo = "Mundo"

# Imprimir los valores
# print(var_hola, var_mundo)

# Concacatenacion de cadenas (unir dos o mas cadenas, +)
var_hola_mundo = var_hola + " " + var_mundo
# print(var_hola_mundo)
# Interpolacion de cadenas, usando la letra f
var_hola_mundo = f"Mi cadena {var_hola} {var_mundo}"
# print(var_hola_mundo)
# Interpolacion con multilineas f''' '''
print(f"""Mi cadena:
    {var_hola}
        {var_mundo}""")
