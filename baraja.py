import random
import collections


PALOS = ['Espada', 'Corazón', 'Rombo', 'Trébol']
VALORES = ['As', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    
    return barajas


def dar_mano(barajas, tamano):
    mano = random.sample(barajas, tamano)

    return mano


def main(tamano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = dar_mano(barajas, tamano)
        manos.append(mano)
    
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        contador =  dict(collections.Counter(valores))
        for val in contador.values():
            if val == 2:
                pares += 1
                break

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par es {probabilidad_par}')    


if __name__ == '__main__':
    tamano = int(input('¿De cuátas barajas será la mano?: '))
    intentos = int(input('¿Cuántos intentos para obtener la probabilidad desea?: '))
    
    main(tamano, intentos)
