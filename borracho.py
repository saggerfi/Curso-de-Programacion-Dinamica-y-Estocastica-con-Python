import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])


class BorrachoImpredecible(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0, 0), (5, 0), (0, 0), (0, 5), (0, 0), (-5, 0), (0, 0), (0, -5)])