import random
import collections
from estadistica import desvest, media
from bokeh.plotting import figure, output_file, show


def tirar(tiros):
    suma = []

    for _ in range(tiros):
        tiro1 = random.choice([1, 2, 3, 4, 5, 6])
        tiro2 = random.choice([1, 2, 3, 4, 5, 6])
        tiro = tiro1 + tiro2
        suma.append(tiro)
    
    return suma


def graficar(x,y):
    plot = figure(title = "Distribución Normal")
    plot.vbar(x, top = y, width = 0.5, color = "#CAB2D6")
    output_file("vertical_bar.html")
    show(plot)   


def estimacion(tiros):
    tirada = tirar(tiros)
    media_est = media(tirada)
    sigma = desvest(tirada)
    counter = dict(collections.Counter(tirada))
    graficar(list(counter.keys()), list(counter.values()))

    return (media_est, sigma) 

def main(tiros):
    media, sigma = estimacion(tiros)
    print(f'Est = {round(media, 5)} sigma = {round(sigma, 5)}')


if __name__ == '__main__':
    tiros = 0
    
    while tiros == 0: 
        tiros = int(input('¿Cuántas veces quieres tirar los dados?: '))
        if tiros == 0:
            print(f'{tiros} no es un valor permitido porfavor ingrese un número mayor a 0')
        else:
            main(tiros)