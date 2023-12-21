class NodoBST:
    def __init__(self, distancia=None):
        self.izquierda = None
        self.derecha = None
        self.distancia = distancia
        self.aristas = []  

    def insertar(self, distancia, arista):
        if not self.distancia:
            self.distancia = distancia
            self.aristas.append(arista)
            return

        if self.distancia == distancia:
            self.aristas.append(arista)
            return

        if distancia < self.distancia:
            if self.izquierda:
                self.izquierda.insertar(distancia, arista)
                return
            self.izquierda = NodoBST(distancia)
            self.izquierda.aristas.append(arista)
            return

        if self.derecha:
            self.derecha.insertar(distancia, arista)
            return
        self.derecha = NodoBST(distancia)
        self.derecha.aristas.append(arista)

    def inorder(self, vals):
        if self.izquierda is not None:
            self.izquierda.inorder(vals)
        if self.distancia is not None:
            vals.append((self.distancia, self.aristas))
        if self.derecha is not None:
            self.derecha.inorder(vals)

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, distancia, arista):
        if not self.raiz:
            self.raiz = NodoBST(distancia)
            self.raiz.aristas.append(arista)
        else:
            self.raiz.insertar(distancia, arista)

    def obtener_distancias_ordenadas(self):
        vals = []
        if self.raiz is not None:
            self.raiz.inorder(vals)
        return vals

