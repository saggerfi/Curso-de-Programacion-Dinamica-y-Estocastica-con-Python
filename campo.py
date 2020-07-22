
class Campo: 

    def __init__(self):
        self.coordenadas_de_borracho = {}

    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borracho[borracho] = coordenada

    def mover_borracho(self, tipo_de_borracho):
        delta_x, delta_y = tipo_de_borracho.camina(tipo_de_borracho)
        coordenada_actual = self.coordenadas_de_borracho[tipo_de_borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borracho[tipo_de_borracho] = nueva_coordenada
    
    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borracho[borracho]