def generar_lista_cuadrados_cubos():
    lista = []
    for i in range(1, 101):
        if i % 2 == 0:
            lista.append(i ** 2)  # cuadrado de los pares
        else:
            lista.append(i ** 3)  # cubo de los impares
    return lista

# Generar la lista y calcular la suma más cercana a un millón
lista_numeros = generar_lista_cuadrados_cubos()
suma = contador = 0
for numero in lista_numeros:
    if suma + numero < 1000000:
        suma += numero
        contador += 1
    else:
        break

print(suma, contador)  # Resultado: (938080, 52)
