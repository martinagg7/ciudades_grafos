from bst import NodoArbol, Arbol
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













