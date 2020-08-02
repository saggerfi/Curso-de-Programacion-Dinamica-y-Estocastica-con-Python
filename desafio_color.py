import random 
import collections
from baraja import crear_baraja, dar_mano 


def color(manos):
    color = 0
    for mano in manos:
        mismo_palo = True
        palo = []
        for carta in mano:
            print(f'carta = {carta}')
            palo.append(carta[0])
            if carta[0] == mano[0][0]:
                pass
            else:
                mismo_palo = False
        
        if mismo_palo == True:
            color += 1
        else:
            pass

    
    print(f'Intentos = {intentos}')
    print(f'Probabilidad de sacar una corrida = {color / intentos}')


def simulacion(tamano, intentos):
    barajas = crear_baraja()
    manos = []
    
    for _ in range(intentos):
        mano = dar_mano(barajas, tamano)
        manos.append(mano)
    
    corrida = color(manos)               

if __name__ == '__main__':
    tamano = 0

    while tamano == 0 or tamano > 52:
        tamano = int(input('¿De qué tamaño es la mano?: '))
        if tamano == 0 or tamano > 52:
            print('Número no válido ingrese un número en el intervalo [1 - 52]')

    intentos = int(input('¿Cuántas simulaciones quiere correr para obtener la probabilidad?: '))
    simulacion(tamano, intentos)