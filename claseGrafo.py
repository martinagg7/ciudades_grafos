from bst import Arbol


class Nodo:  # Nodo
    def __init__(self, nombre):
        self.nombre = nombre
        self.caminos = []  # Objetos tipo arista
        self.nodo_previo = None

    def insertar_id(self, id):
        self.id = id


class Arista:  # Arista
    def __init__(self, nodo1, nodo2, distancia):
        self.nodo1 = nodo1
        self.nodo2 = nodo2
        self.distancia = distancia

    def __repr__(self):
        return f"{self.nodo1.nombre} - {self.nodo2.nombre}: {self.distancia}"


class Grafo:
    def __init__(self):
        self.numero_de_nodos = 0
        self.nodos = []
        self.bst = Arbol()

    def insertar_nodo(self, nodo):
        nodo.insertar_id(self.numero_de_nodos)
        self.numero_de_nodos += 1
        self.nodos.append(nodo)

    def insertar_arista(self, nodo1, nodo2, distancia):
        arista = Arista(nodo1, nodo2, distancia)
        nodo1.caminos.append(Arista(nodo1, nodo2, distancia))
        nodo2.caminos.append(Arista(nodo2, nodo1, distancia))
        self.bst.insertar(distancia, [arista])

    def mostrar_grafo(self):
        matriz_de_adyacencia = []
        for _ in range(self.numero_de_nodos):
            matriz_de_adyacencia.append([0] * self.numero_de_nodos)

        for nodo in self.nodos:
            for arista in nodo.caminos:
                matriz_de_adyacencia[arista.nodo1.id][
                    arista.nodo2.id
                ] = arista.distancia
                matriz_de_adyacencia[arista.nodo2.id][
                    arista.nodo1.id
                ] = arista.distancia

        for fila in matriz_de_adyacencia:
            print(fila)

    def mostrar_distancias_ordenadas(self):
        distancias_ordenadas = self.bst.obtener_distancias_ordenadas()
        for distancia, aristas in distancias_ordenadas:
            print(f"Distancia km: {distancia}, Ciudades: {aristas}")
