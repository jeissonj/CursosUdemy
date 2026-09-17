print("*** Argumentos Variables ***")


def superheroe_superpoderes(nombre, *args):
    print(f"Superheroe: {nombre} - {args}")
    # for superpoder in args:
    #     print(f'Superpoder: {superpoder}')


# Llamamos a la funcion
superheroe_superpoderes("Spiderman", "Instinto Aracnido", "Telaraña")
superheroe_superpoderes("Ironman", "Armadura", "Playboy", "Millonario")
# Es opcional enviar argumentos variables
superheroe_superpoderes("Mi Vecino")
