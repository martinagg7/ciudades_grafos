class NodoCamino:#camino entre dos ciudades
    def __init__(self,distancia,ciudad_destino):
        self.distancia=distancia
        self.ciudad_destino=ciudad_destino
        self.sig=None

class Camino:#lista de todos los caminos que salen de una ciudad
    def __init__(self):
        self.inicio=None
        self.tamanio=0

    def insertar_camino(self,distancia,ciudad_destino):#método para insertar todos los caminos que hay desde una ciudad
        nuevo=NodoCamino(distancia,ciudad_destino)
        nuevo.sig=self.inicio
        self.inicio=nuevo
        self.tamanio+=1

class Ciudad:#ciudad en nuestra red de transporte
    def __init__(self,nombre):
        self.nombre=nombre
        self.sig=None
        self.visitado=None
        self.caminos= Camino()

"Clase grafo que representa nuestra red de transporte entre ciudades"
class Grafociudades:#grafo de nuestras ciudades unidas
    def __init__(self,dirigido=True):
        self.inicio=None
        self.dirigido=dirigido
        self.tamanio=0   

    def insertar_ciudad(self,nombre):#función para crear una nueva ciudad en nuestro grafo
        nueva_ciudad=Ciudad(nombre)
        if self.inicio is None:
            self.inicio=nueva_ciudad
        else:
            actual=self.inicio
            while actual.sig is not None:
                actual=actual.sig
            actual.sig=nueva_ciudad
        self.tamanio+=1

    def insertar_camino(self,origen,destino,distancia):
        ciudad_origen=None
        ciudad_destino=None
        act=self.inicio
        while act is not None:
            if act.nombre==origen:
                ciudad_origen=act
            elif act.nombre==destino:
                ciudad_destino=act
            act=act.sig
        
        if ciudad_origen is not None and ciudad_destino is not None:
            ciudad_origen.caminos.insertar(distancia,ciudad_destino)
            if not self.dirigido:# si no es dirigido puede haber camino de a->b pero no de b->a
                ciudad_destino.caminos.insertar(distancia,ciudad_origen)