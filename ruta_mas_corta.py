from claseGrafo import *

def elegir_nodo(origen):
    distancia_minima = float('inf')
    nodo_minimo = None
    
    for camino in nodo_actual.caminos:
        if camino.nodo2.distancia < distancia_minima:
            distancia_minima = camino.nodo2.distancia
            nodo_minimo = camino.nodo2
    return nodo_minimo
    
def ruta_mas_corta(origen,destino,grafo):
    for nodo in grafo.nodos:
        nodo.distancia = float('inf')
        nodo.visitado = False
        
    origen.distancia = 0
    
    while True:
        nodo_actual = elegir_nodo(nodo_actual)
        
        if nodo_actual == destino:
            break
        
        nodo_actual.visitado = True
        
        for camino in nodo_actual.caminos:
            if camino.nodo2.visitado == False:
                nueva_distancia = camino.distancia + nodo_actual.distancia
                
                    if nueva_distancia < camino.nodo2.distancia:
                        camino.nodo2.distancia = nueva_distancia
                        
            