from claseGrafo import *

def elegir_nodo(origen):
    distancia_minima = float('inf')
    nodo_minimo = None
    
    for camino in origen.caminos:
        if camino.nodo2.distancia < distancia_minima and not camino.nodo2.visitado:
            distancia_minima = camino.nodo2.distancia
            nodo_minimo = camino.nodo2
    return nodo_minimo
    
def ruta_mas_corta(origen,destino,grafo):
    for nodo in grafo.nodos:
        nodo.distancia = float('inf')
        nodo.visitado = False
    
    origen.distancia = 0
    nodo_actual = origen
    
    while True:
        
        if nodo_actual == destino:
            break
        
        nodo_actual.visitado = True
        
        for camino in nodo_actual.caminos:
            if camino.nodo2.visitado == False:
                nueva_distancia = camino.distancia + nodo_actual.distancia
                
                if nueva_distancia < camino.nodo2.distancia:
                    camino.nodo2.distancia = nueva_distancia
                    camino.nodo2.nodo_previo = nodo_actual
                        
        nodo_actual = elegir_nodo(nodo_actual)
        
    ruta = []
    
    while destino is not None:
        ruta.insert(0, destino) #metemos los nodos por los que pasamos por el principio
        destino = destino.nodo_previo
        
    return (nodo_actual.distancia,ruta)
                        
            