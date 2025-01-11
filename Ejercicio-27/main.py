import re
texto = "Contacto: ana@correo.com, pedromail.com" # Solo imprime el primero de los correos, ya que es el bueno.
correos = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
print(correos)