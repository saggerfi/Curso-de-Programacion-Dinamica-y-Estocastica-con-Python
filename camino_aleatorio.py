
from borracho import BorrachoImpredecible
from campo import Campo
from coordenadas import Coordenada
from bokeh.plotting import figure, show


# def caminata(campo, tipo_de_borracho, pasos):
#     inicio = campo.obtener_coordenada(tipo_de_borracho)

#     for _ in range(pasos):
#         campo.mover_borracho(tipo_de_borracho)

#     return inicio.distancia(campo.obtener_coordenada(tipo_de_borracho))


def simular_caminata(campo, tipo_de_borracho, distancias_de_caminata):
    # borracho = tipo_de_borracho(nombre = 'Gerardo')
    # origen = Coordenada(0, 0)
    # distancias = []

    # for _ in range(numero_de_intentos):
    #     campo = Campo()
    #     campo.anadir_borracho(borracho, origen)
    #     simulacion_caminata = caminata(campo, borracho, pasos)
    #     distancias.append(round(simulacion_caminata, 1))
        
    # return distancias
    x_arreglo = []
    y_arreglo = []
    x_arreglo.append(campo.obtener_coordenada(tipo_de_borracho).x)
    y_arreglo.append(campo.obtener_coordenada(tipo_de_borracho).y)
    
    for _ in range(distancias_de_caminata):
        campo.mover_borracho(tipo_de_borracho) #se actualiza las coordenadas del borracho
        x_arreglo.append(campo.obtener_coordenada(tipo_de_borracho).x)
        y_arreglo.append(campo.obtener_coordenada(tipo_de_borracho).y)

    graficar(x_arreglo, y_arreglo)

def graficar(x ,y):
    grafica = figure(title = 'Recorrido aleatorio', x_axis_label = 'X', y_axis_label = 'Y')
    grafica.line(x ,y)

    show(grafica) 
    

def main(distancias_de_caminata, inicio, tipo_de_borracho):
    campo = Campo()
    campo.anadir_borracho(tipo_de_borracho, inicio)
    simular_caminata(campo, tipo_de_borracho, distancias_de_caminata)
    # distancia_media_por_caminata = []

    # for pasos in distancias_de_caminata:
    #     distancias = simular_caminata(campo, pasos, numero_de_intentos, tipo_de_borracho)
    #     distancia_media = round(sum(distancias) / len(distancias), 4)
    #     distancia_maxima = max(distancias)
    #     distancia_minima = min(distancias)
    #     distancia_media_por_caminata.append(distancia_media)
    #     print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
    #     print(f'Media = {distancia_media}')
    #     print(f'Max = {distancia_maxima}')
    #     print(f'Min = {distancia_minima}')
    # graficar(distancias_de_caminata, distancia_media_por_caminata)


if __name__ == '__main__':
    distancias_de_caminata = 100
    # numero_de_intentos = 100
    inicio = Coordenada(0, 0)

    main(distancias_de_caminata, inicio, BorrachoImpredecible)