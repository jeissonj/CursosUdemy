print("*** Argumentos Variables ***")


# *args -> arguments -> tupla
# **kwargs -> keyword arguments -> diccionario
# Llamamos a la funcion
def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f"Superheroe: {nombre} - {args}. Mas info: {kwargs}")
    # for superpoder in args:
    #     print(f'Superpoder: {superpoder}')


superheroe_superpoderes("Spiderman", "Instinto Aracnido", edad=17, empresa="Marvel")
superheroe_superpoderes("Ironman", "Armadura", "Playboy", edad=45)
# Es opcional enviar argumentos variables
superheroe_superpoderes("Mi Vecino", personalidad="Buena onda!")
