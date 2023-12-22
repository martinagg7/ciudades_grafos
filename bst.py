class NodoArbol:
    def __init__(self, distancia, ciudades):
        self.distancia = distancia
        self.ciudades = ciudades  # lista de ciudades
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, distancia, ciudades):
        if (
            self.raiz is None
        ):  # si el arbol esta vacio insertamos si no llamos a la función recursiva
            self.raiz = NodoArbol(distancia, ciudades)
        else:
            self.insertar_recur(distancia, ciudades, self.raiz)

    def insertar_recur(self, distancia, ciudades, nodo):
        if distancia < nodo.distancia:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(distancia, ciudades)
            else:
                self.insertar_recur(
                    distancia, ciudades, nodo.izquierda
                )  # recorremos bst hasta encontrar su posición de forma recursiva
        elif distancia > nodo.distancia:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(distancia, ciudades)
            else:
                self.insertar_recur(distancia, ciudades, nodo.derecha)
        else:
            nodo.ciudades += ciudades  # si la distancia coincide lo añadimos a la lista de ciudades asociades con esta distancia

    def in_order(self, nodo=-1):
        if nodo == -1:
            nodo = self.raiz
        if nodo is None:
            return
        print(f"Distancia: {nodo.distancia}, Ciudades: {nodo.ciudades}")
        self.in_order(nodo.izquierda)
        self.in_order(nodo.derecha)
