import random 
import collections
from baraja import crear_baraja, dar_mano 


def simulacion(tamano, intentos):
    barajas = crear_baraja()
    manos = []
    
    for _ in range(intentos):
        mano = dar_mano(barajas, tamano)
        manos.append(mano)
    
    color = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[0])
        
        contador =  dict(collections.Counter(valores))
        for val in contador.values():
            if val == val:
                color += 1
                

if __name__ == '__main__':
    tamano = 0

    while tamano == 0 or tamano > 52:
        tamano = int(input('¿De qué tamaño es la mano?: '))
        print('Número no válido ingrese un número en el intervalo [1 - 52]')

    intentos = int(input('¿Cuántas simulaciones quiere correr para obtener la probabilidad?: '))
    simulacion(tamano, intentos)