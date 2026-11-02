from graph import Graph
from heap import HeapMin

EPISODIOS = {
    "Luke Skywalker": {4, 5, 6, 7, 8, 9},
    "Darth Vader": {3, 4, 5, 6},
    "Yoda": {1, 2, 3, 5, 6, 8, 9},
    "Boba Fett": {2, 5, 6},
    "C-3PO": {1, 2, 3, 4, 5, 6, 7, 8, 9},
    "Leia": {3, 4, 5, 6, 7, 8, 9},
    "Rey": {7, 8, 9},
    "Kylo Ren": {7, 8, 9},
    "Chewbacca": {3, 4, 5, 6, 7, 8, 9},
    "Han Solo": {4, 5, 6, 7, 9},
    "R2-D2": {1, 2, 3, 4, 5, 6, 7, 8, 9},
    "BB-8": {7, 8, 9},
}


def armar_grafo():
    """Vértice = personaje (los episodios van en other_values).
    Arista = cantidad de episodios en los que aparecieron juntos."""
    grafo = Graph(is_dir=False)
    for personaje, episodios in EPISODIOS.items():
        grafo.add_vertex(personaje, episodios)

    nombres = list(EPISODIOS)
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            juntos = len(EPISODIOS[nombres[i]] & EPISODIOS[nombres[j]])
            if juntos > 0:
                grafo.add_edge(juntos, nombres[i], nombres[j])
    return grafo


def arbol_expansion_minima(grafo, origen):
    aristas = HeapMin()
    for vertice in grafo:
        for arista in vertice.edges:
            aristas.arrive([vertice.value, arista.destination], arista.weight)

    componente = {v.value: {v.value} for v in grafo} 
    arbol = []
    while aristas.size() > 0:
        peso, (a, b) = aristas.attention()
        if componente[a] is not componente[b]:
            union = componente[a] | componente[b]
            for v in union:
                componente[v] = union
            arbol.append((a, b, peso))

    return [(a, b, p) for a, b, p in arbol if a in componente[origen]]


def camino_mas_corto(grafo, origen, destino):
    pila = grafo.dijkstra(origen)
    camino = []
    costo = None
    actual = destino
    while pila.size() > 0:
        vertice, costo_vertice, previo = pila.pop()
        if vertice == actual:
            if costo is None:
                costo = costo_vertice
            camino.append(vertice)
            actual = previo
    camino.reverse()
    return camino, costo


# Máximo de episodios compartidos 
def maximo_episodios(grafo):
    pares = {}
    for vertice in grafo:
        for arista in vertice.edges:
            par = tuple(sorted([vertice.value, arista.destination]))
            pares[par] = arista.weight  # sin duplicados (no dirigido)
    maximo = max(pares.values())
    return maximo, [par for par, peso in pares.items() if peso == maximo]


# Personajes que aparecen en los nueve episodios
def en_los_nueve(grafo):
    return [v.value for v in grafo if len(v.other_values) == 9]


if __name__ == "__main__":
    grafo = armar_grafo()

    for origen in ["C-3PO", "Yoda", "Leia"]:
        arbol = arbol_expansion_minima(grafo, origen)
        print(f"\nÁrbol de expansión mínimo desde {origen} "
              f"(peso total {sum(p for _, _, p in arbol)}):")
        for a, b, peso in arbol:
            print(f"  {a} -- {b} ({peso})")

    maximo, pares = maximo_episodios(grafo)
    print(f"\nMáximo de episodios compartidos: {maximo}")
    for a, b in pares:
        print(f"  {a} y {b}")

    for origen, destino in [("C-3PO", "R2-D2"), ("Yoda", "Darth Vader")]:
        camino, costo = camino_mas_corto(grafo, origen, destino)
        print(f"\nCamino más corto {origen} -> {destino}: "
              f"{' -> '.join(camino)} (costo {costo})")

    print("\nAparecieron en los nueve episodios:", ", ".join(en_los_nueve(grafo)))
