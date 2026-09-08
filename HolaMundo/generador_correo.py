# generar correo usando el ejemplo anterior

print("*** Bienenido al sistema generador de emaol de ciudad gotica ***")

nombre = input("Cuál es tu nombre?: ")
apellido = input("Cuáñ es tu apellido?: ")

nombre.lower()

correo = f"{nombre.lower()}{'.'}{apellido.lower()}{'@ciudadgotica.com'}"

print(f""" Tu nuevo email generado por el sistema es 
      {correo}
      *** Felicidades ***""")
