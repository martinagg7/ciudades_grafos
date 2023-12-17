class Nodo:#Nodo
    def __init__(self,nombre):
        self.nombre=nombre
        self.caminos = [] #Objetos tipo arista
        # self.visitado=None
    def insertar_id(self,id):
        self.id = id
      
class Arista:#Arista
    def __init__(self, nodo1, nodo2, distancia):
        self.nodo1 = nodo1
        self.nodo2 = nodo2
        self.distancia = distancia

class Grafo:
    def __init__(self):
        self.numero_de_nodos = 0
        self.nodos = []
    
    def insertar_nodo(self,nodo):
        nodo.insertar_id(self.numero_de_nodos)
        self.numero_de_nodos += 1
        self.nodos.append(nodo)
    
    def insertar_arista(self, nodo1, nodo2, distancia):
        nodo1.caminos.append(Arista(nodo1, nodo2, distancia))
        nodo2.caminos.append(Arista(nodo2, nodo1, distancia))
        
    def mostrar_grafo(self):
        matriz_de_adyacencia = []
        for _ in range(self.numero_de_nodos):
            matriz_de_adyacencia.append([0] * self.numero_de_nodos)
        
        for nodo in self.nodos:
            for arista in nodo.caminos:
                matriz_de_adyacencia[arista.nodo1.id][arista.nodo2.id] = arista.distancia
                matriz_de_adyacencia[arista.nodo2.id][arista.nodo1.id] = arista.distancia
                
        for fila in matriz_de_adyacencia:
            print(fila)
        

espania = Grafo()

ciudades = [Nodo('Madrid'), Nodo('Barcelona'), Nodo('Cadiz'), Nodo('Lugo')]
for ciudad in ciudades:
    espania.insertar_nodo(ciudad)
espania.insertar_arista(ciudades[0],ciudades[1],626)
espania.insertar_arista(ciudades[1],ciudades[2],1108)
espania.insertar_arista(ciudades[0],ciudades[3],500)
espania.insertar_arista(ciudades[1],ciudades[3],994)

    
espania.mostrar_grafo()













"""class NodoCamino:#camino entre dos ciudades
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
                ciudad_destino.caminos.insertar(distancia,ciudad_origen)"""