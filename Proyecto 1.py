import math

# Función para calcular la temperatura en función del tiempo
def calcular_temperatura(T0, Ts, k, t):
    """
    Calcula la temperatura de un cuerpo en función del tiempo.
    
    Parámetros:
        T0: Temperatura inicial del cuerpo (en ºC)
        Ts: Temperatura del ambiente (en ºC)
        k: Constante de enfriamiento
        t: Tiempo transcurrido (en horas)
    
    Retorna:
        La temperatura del cuerpo en el tiempo t.
    """
    return Ts + (T0 - Ts) * math.exp(-k * t)

# Función para encontrar el tiempo necesario para alcanzar una temperatura específica
def tiempo_para_temperatura(T0, Ts, k, T_deseada):
    """
    Calcula el tiempo necesario para que la temperatura del cuerpo alcance un valor deseado.
    
    Parámetros:
        T0: Temperatura inicial del cuerpo (en ºC)
        Ts: Temperatura del ambiente (en ºC)
        k: Constante de enfriamiento
        T_deseada: Temperatura deseada (en ºC)
    
    Retorna:
        El tiempo necesario para alcanzar la temperatura deseada.
    """
    if T_deseada >= Ts:
        return 0  # Si la temperatura deseada es igual o mayor a la del ambiente, no hay espera
    return -math.log((T_deseada - Ts) / (T0 - Ts)) / k

# Parámetros iniciales
T0 = 5   # Temperatura inicial de la lata de refresco (en ºC)
Ts = 40  # Temperatura ambiente (en ºC)
k = 0.45  # Constante de enfriamiento

# Calcular la temperatura a los tiempos especificados
tiempos = [1, 5, 12, 14]  # Tiempos en horas
temperaturas = {t: calcular_temperatura(T0, Ts, k, t) for t in tiempos}

print("Temperaturas a diferentes tiempos:")
for t, temp in temperaturas.items():
    print(f"A las {t} horas: {temp:.2f} ºC")

# Calcular el tiempo necesario para que la lata esté a 0.5ºC menos que la temperatura ambiente
T_deseada = Ts - 0.5
tiempo_necesario = tiempo_para_temperatura(T0, Ts, k, T_deseada)

print(f"\nTiempo necesario para que la lata alcance {T_deseada} ºC: {tiempo_necesario:.2f} horas")
