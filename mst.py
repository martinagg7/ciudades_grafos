from claseGrafo import Grafo


def calcular_mst(
    grafo: Grafo,
):  # sirve para decirle a python "oye que el parametro grafo es de tipo Grafo"
    visitados = []
    aristas_mst = []
    nodo_actual = grafo.nodos[0]
    distancia_total = 0

    while len(visitados) != grafo.numero_de_nodos - 1:
        visitados.append(nodo_actual)
        menor_distancia = float("inf")
        menor = 0
        for nodo_visitado in visitados:
            for camino in nodo_visitado.caminos:
                if menor_distancia > camino.distancia and camino.nodo2 not in visitados:
                    menor_distancia = camino.distancia
                    menor = camino
        aristas_mst.append(menor)
        distancia_total += menor_distancia
        nodo_actual = menor.nodo2
    visitados.append(nodo_actual)
    return {
        "distancia_total": distancia_total,
        "aristas_mst": [
            (arista.nodo1.nombre, arista.nodo2.nombre, arista.distancia)
            for arista in aristas_mst
        ],
    }
