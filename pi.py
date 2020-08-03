import random
import math
from estadisticas import desvest, media


def aventar_agujas(numero_de_agujas):
    dentro_del_circulo = 0

    for _ in range(numero_de_agujas):
        x = random.random() * random.choice[(-1, 1)]
        y = random.random() * random.choice[(-1, 1)]
        distancia_desde_el_centro = math.sqrt(x ** 2 + y ** 2)

        if distancia_desde_el_centro <= 1:
            adentro_del_circulo += 1

    return (4 * adentro_del_circulo) / numero_de_agujas


def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []

    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desvest(estimados)
    print(f'Estimación = {round(media_estimados, 5)}, sigma = {(round{sigma, 5)}')
    