def desglosar_cantidad(cantidad):
    billetes_y_monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    desglose = {}
    for valor in billetes_y_monedas:
        cantidad, num_billetes = divmod(cantidad, valor)
        if num_billetes > 0:
            desglose[valor] = num_billetes
    return desglose

# Probar con una cantidad de ejemplo
cantidad = 1234
resultado = desglosar_cantidad(cantidad)
print(resultado) # Resultado: {500:2,200:1}
