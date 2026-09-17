# Maquina de snacks
import modulo_maquina as mm

# Primero vamos a crear unos productos y llaves iniciales en unas lisas que luego ingresaeremos a un diccionario y despues si desea el usuario podra modificar

productos = ["p1", "p2", "p3"]
llaves = ["ll1", "ll2", "ll3"]

# La forma de unir los productos con las llaves es con la funcion zip
l_productos = dict(zip(llaves, productos))

mm.mostrar_productos(l_productos)
