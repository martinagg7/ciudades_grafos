class NodoCamino:
    def __init__(self,distancia,ciudad_destino):
        self.distancia=distancia
        self.ciudad_destino=ciudad_destino
        self.sig=None

class Camino:
    def __init__(self):
        self.inicio=None
        self.tamanio=0

class Ciudad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.sig=None
        self.visitado=None
        self.caminos= Camino()

