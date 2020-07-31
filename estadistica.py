import random
import math


def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)
    acumulador = 0
    for x in X: 
        acumulador += (x - mu)**2

    return acumulador / len(X) 


def desvest(X):
    return math.sqrt(varianza(X))


if __name__ == '__main__':
    X = [random.randint(9, 12) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desvest(X)

    print(f'La lista de valores es: {X}')
    print(f'La media de la lista es {mu}')
    print(f'La varianza es {Var}')
    print(f'La desviación estándar es: {sigma}')

