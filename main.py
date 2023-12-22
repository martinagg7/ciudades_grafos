from bst import *
from claseGrafo import *
from ruta_mas_corta import *
from mst import *

#Ejemplo de uso

grafo = Grafo()

#Insertar nodos

nodo_a = Nodo('A')
nodo_b = Nodo('B')
nodo_c = Nodo('C')
nodo_d = Nodo('D')


grafo.insertar_nodo(nodo_a)
grafo.insertar_nodo(nodo_b)
grafo.insertar_nodo(nodo_c)
grafo.insertar_nodo(nodo_d)

#Insertar aristas

grafo.insertar_arista(nodo_a, nodo_b, 1)
grafo.insertar_arista(nodo_a, nodo_c, 4)
grafo.insertar_arista(nodo_b, nodo_c, 2)
grafo.insertar_arista(nodo_b, nodo_d, 5)
grafo.insertar_arista(nodo_c, nodo_d, 1)

    
#Aplicar el algoritmo de Dijkstra

distancia, ruta = ruta_mas_corta(nodo_a, nodo_d, grafo)

print("La distancia minima es", distancia, "por la ruta", [nodo.nombre for nodo in ruta])
# #Imprimir las distancias mínimas

# grafo.imprimir_distancias_minimas()

# #Obtener el camino mínimo desde A a D

# camino_minimo = grafo.obtener_camino_minimo(nodo_d)
# print("Camino mínimo desde A a D:", [nodo.nombre for nodo in camino_minimo])

print("Arbol de busqueda binaria")
arbol = Arbol()
arbol.insertar(1, ['A', 'B', 'C', 'D'])
arbol.insertar(2, ['B', 'C'])
arbol.insertar(4, ['A', 'C'])
arbol.insertar(5, ['B', 'D'])
print(arbol.in_order())

# mst = Prim.calcular_mst(grafo)

# print(f"Distancia total: {mst['distancia_total']}, Nodos: {mst['visitados']}")