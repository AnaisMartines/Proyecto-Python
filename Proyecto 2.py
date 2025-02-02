def letra_dni(numero_dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    residuo = numero_dni % 23
    return letras[residuo]

# Probar con un número de DNI de ejemplo
numero_dni = 12345678
letra = letra_dni(numero_dni)
print(letra)  # Resultado: Z
