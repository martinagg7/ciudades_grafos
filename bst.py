class NodoArbol:
    def __init__(self, distancia, ciudades):
        self.distancia = distancia
        self.ciudades = ciudades #lista de ciudades
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, distancia, ciudades):
        if self.raiz is None:# si el arbol esta vacio insertamos si no llamos a la función recursiva
            self.raiz = NodoArbol(distancia, ciudades)
        else:
            self.insertar_recur(distancia, ciudades, self.raiz)

    def insertar_recur(self, distancia, ciudades, nodo):
        if distancia < nodo.distancia:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(distancia, ciudades)
            else:
                self.insertar_recur(distancia, ciudades, nodo.izquierda) #recorremos bst hasta encontrar su posición de forma recursiva
        elif distancia > nodo.distancia:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(distancia, ciudades)
            else:
                self.insertar_recur(distancia, ciudades, nodo.derecha)
        else:
            nodo.ciudades += ciudades #si la distancia coincide lo añadimos a la lista de ciudades asociades con esta distancia

    def in_order(self, nodo=-1):
        if nodo == -1:
            nodo = self.raiz
        if nodo is None:
            return
        print(f"Distancia: {nodo.distancia}, Ciudades: {nodo.ciudades}")
        self.in_order(nodo.izquierda)
        self.in_order(nodo.derecha)



# class NodoBST:
#     def __init__(self, distancia=None):
#         self.izquierda = None
#         self.derecha = None
#         self.distancia = distancia
#         self.aristas = []  

#     def insertar(self, distancia, arista):
#         if not self.distancia:
#             self.distancia = distancia
#             self.aristas.append(arista)
#             return

#         if self.distancia == distancia:
#             self.aristas.append(arista)
#             return

#         if distancia < self.distancia:
#             if self.izquierda:
#                 self.izquierda.insertar(distancia, arista)
#                 return
#             self.izquierda = NodoBST(distancia)
#             self.izquierda.aristas.append(arista)
#             return

#         if self.derecha:
#             self.derecha.insertar(distancia, arista)
#             return
#         self.derecha = NodoBST(distancia)
#         self.derecha.aristas.append(arista)

#     def inorder(self, vals):
#         if self.izquierda is not None:
#             self.izquierda.inorder(vals)
#         if self.distancia is not None:
#             vals.append((self.distancia, self.aristas))
#         if self.derecha is not None:
#             self.derecha.inorder(vals)

# class BST:
#     def __init__(self):
#         self.raiz = None

#     def insertar(self, distancia, arista):
#         if not self.raiz:
#             self.raiz = NodoBST(distancia)
#             self.raiz.aristas.append(arista)
#         else:
#             self.raiz.insertar(distancia, arista)

#     def obtener_distancias_ordenadas(self):
#         vals = []
#         if self.raiz is not None:
#             self.raiz.inorder(vals)
#         return vals

