# Generador de ID
from random import randint

print("*** Sistema generador de un Id unico ***")

nombre = input("Cuál es su nombre?: ")
apellido = input("Cuál es su apellido?: ")
anho = input("¿Cuál es su año de nacimiento? ")

aleatorio = randint(0,9999)



id = f"{nombre[0:2].upper()}{apellido[0:2].upper()}{anho[2:]}{aleatorio}" 



print(f"""\n Hola {nombre}, habítante de ciudad gotica!
\t Tu nuevo numero de identificación (ID) generado poe el sistema es:
\t {id}
    Felicidades! """)