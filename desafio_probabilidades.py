import random


def tirar(tiro):
    secuencia_tiro = []
    
    for _ in range(tiro):
        tirada1 = random.choice([1, 2, 3, 4, 5, 6])
        tirada2 = random.choice([1, 2, 3, 4, 5, 6])
        suma = tirada1 + tirada2
        secuencia_tiro.append(suma)
    
    return secuencia_tiro


def main(tiro, simulacion):
    tiros = []
    
    for _ in range(simulacion):
        secuenciad1 = tirar(tiro)
        tiros.append(secuenciad1)
    
    tiro_de_12 = 0
    
    for tiro in tiros:
        if 12 in tiro:
            tiro_de_12 += 1

    probabilidad_tiro12 = tiro_de_12 / simulacion
    print(f'Probabilidad de tener por lo menos un 12 en {simulacion} tiros = {probabilidad_tiro12}')



if __name__ == '__main__':
    tiro = int(input('¿Cuántos tiros de dados quieres?: '))
    simulacion = int(input('¿Cuántas veces quieres simular?: '))
    
    main(tiro, simulacion)