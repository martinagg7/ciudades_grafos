from bst import Arbol
from claseGrafo import Grafo, Nodo
from ruta_mas_corta import ruta_mas_corta
from mst import calcular_mst

grafo = Grafo()

# Insertar nodos

nodo_a = Nodo("A")
nodo_b = Nodo("B")
nodo_c = Nodo("C")
nodo_d = Nodo("D")


grafo.insertar_nodo(nodo_a)
grafo.insertar_nodo(nodo_b)
grafo.insertar_nodo(nodo_c)
grafo.insertar_nodo(nodo_d)

# Insertar aristas

grafo.insertar_arista(nodo_a, nodo_b, 1)
grafo.insertar_arista(nodo_a, nodo_c, 4)
grafo.insertar_arista(nodo_b, nodo_c, 2)
grafo.insertar_arista(nodo_b, nodo_d, 5)
grafo.insertar_arista(nodo_c, nodo_d, 1)

print("Matriz de adyacencia")
grafo.mostrar_grafo()

# Aplicar el algoritmo de Dijkstra

distancia, ruta = ruta_mas_corta(nodo_a, nodo_d, grafo)

print(
    "La distancia minima es", distancia, "por la ruta", [nodo.nombre for nodo in ruta]
)

print("Arbol de busqueda binaria")
arbol = Arbol()
arbol.insertar(1, ["A", "B", "C", "D"])
arbol.insertar(2, ["B", "C"])
arbol.insertar(4, ["A", "C"])
arbol.insertar(5, ["B", "D"])
arbol.in_order()

mst = calcular_mst(grafo)

print(f"Distancia total: {mst['distancia_total']}, Aristas: {mst['aristas_mst']}")
