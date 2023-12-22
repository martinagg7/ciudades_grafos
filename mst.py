from claseGrafo import *

def calcular_mst(grafo:Grafo): #sirve para decirle a python "oye que el parametro grafo es de tipo Grafo"
    visitados = []
    nodo_actual = grafo.nodos[0]
    visitados.append(nodo_actual)
    
    for nodo in visitados:
        for camino in nodo