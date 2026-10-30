"""
Guía de ejercicios de grafos - Ejercicios 5 y 14
Implementación utilizando la clase Graph provista por la cátedra.
"""
from graph import Graph


def camino_minimo(g: Graph, origen: str, destino: str):
    """Reconstruye el camino más corto y su costo usando el dijkstra de la cátedra."""
    paths = g.dijkstra(origen)
    curr = destino
    costo_total = None
    camino = []

    while paths.size() > 0:
        nodo, costo, anterior = paths.pop()
        if nodo == curr:
            if costo_total is None:
                costo_total = costo
            camino.append(nodo)
            curr = anterior

    camino.reverse()
    return costo_total, camino


# =====================================================================
# EJERCICIO 5 - Red de equipos
# =====================================================================
def cargar_red() -> Graph:
    g = Graph(is_dir=False)

    equipos = {
        "pc": ["Manjaro", "Parrot", "Fedora", "Ubuntu", "Mint"],
        "notebook": ["Red Hat", "Debian", "Arch"],
        "servidor": ["Guaraní", "MongoDB"],
        "router": ["Router 1", "Router 2", "Router 3"],
        "switch": ["Switch 1", "Switch 2"],
        "impresora": ["Impresora"],
    }

    # a) Cada nodo almacena su nombre y su tipo en other_values
    for tipo, nombres in equipos.items():
        for nombre in nombres:
            g.add_vertex(nombre, other_values={"tipo": tipo})

    conexiones = [
        (25, "Red Hat", "Router 2"),
        (9, "Guaraní", "Router 2"),
        (50, "Router 2", "Router 3"),
        (37, "Router 2", "Router 1"),
        (43, "Router 3", "Router 1"),
        (61, "Router 3", "Switch 2"),
        (29, "Router 1", "Switch 1"),
        (17, "Switch 1", "Debian"),
        (18, "Switch 1", "Ubuntu"),
        (22, "Switch 1", "Impresora"),
        (80, "Switch 1", "Mint"),
        (40, "Switch 2", "Manjaro"),
        (12, "Switch 2", "Parrot"),
        (5, "Switch 2", "MongoDB"),
        (56, "Switch 2", "Arch"),
        (3, "Switch 2", "Fedora"),
    ]

    # add_edge recibe (weight, origin, destination)
    for peso, a, b in conexiones:
        g.add_edge(peso, a, b)

    return g


def barridos_desde_notebooks(g: Graph):
    for nb in ("Red Hat", "Debian", "Arch"):
        print(f"\n--- Barridos desde {nb} ---")
        print("Profundidad (DFS):")
        g.deep_show(nb)
        print("Amplitud (BFS):")
        g.amplitude_show(nb)


def ejercicio_5():
    g = cargar_red()

    print("=" * 70)
    print("EJERCICIO 5")
    print("=" * 70)

    # b) Barridos en profundidad y amplitud desde las tres notebooks
    print("\nb) Barridos en profundidad y amplitud desde notebooks:")
    barridos_desde_notebooks(g)

    # c) Camino más corto a la impresora desde Manjaro, Red Hat y Fedora
    print("\nc) Camino más corto hasta la impresora:")
    for pc in ("Manjaro", "Red Hat", "Fedora"):
        costo, camino = camino_minimo(g, pc, "Impresora")
        print(f"   {pc}: costo {costo} -> {' -> '.join(camino)}")

    # d) Árbol de expansión mínima (Kruskal)
    print("\nd) Árbol de expansión mínima (Kruskal):")
    min_tree = g.kruskal("Router 1")
    peso_total = 0
    for edge in min_tree.split(";"):
        orig, dest, weight = edge.split("-")
        print(f"   {orig} - {dest}: {weight}")
        peso_total += int(weight)
    print(f"   Peso total: {peso_total}")

    # e) PC (no notebook) con camino más corto hasta "Guaraní"
    print("\ne) PC (no notebook) con el camino más corto al servidor Guaraní:")
    todas_las_pc = [
        v.value for v in g if v.other_values and v.other_values.get("tipo") == "pc"
    ]
    mejor_pc = None
    mejor_costo = float("inf")
    mejor_camino = []

    for pc in todas_las_pc:
        costo, camino = camino_minimo(g, pc, "Guaraní")
        if costo is not None and costo < mejor_costo:
            mejor_costo = costo
            mejor_pc = pc
            mejor_camino = camino

    print(f"   Mejor PC: {mejor_pc} (costo: {mejor_costo}) -> {' -> '.join(mejor_camino)}")

    # f) Computadora conectada al Switch 1 con camino más corto a MongoDB
    print("\nf) Computadora del Switch 1 con el camino más corto a MongoDB:")
    pos_sw1 = g.search("Switch 1", "value")
    compus_sw1 = []
    if pos_sw1 is not None:
        for edge in g[pos_sw1].edges:
            pos_v = g.search(edge.destination, "value")
            if pos_v is not None:
                tipo = g[pos_v].other_values.get("tipo") if g[pos_v].other_values else None
                if tipo in ("pc", "notebook"):
                    compus_sw1.append(edge.destination)

    mejor_compu = None
    mejor_costo_mongo = float("inf")
    mejor_camino_mongo = []

    for compu in compus_sw1:
        costo, camino = camino_minimo(g, compu, "MongoDB")
        print(f"   {compu}: costo {costo}")
        if costo is not None and costo < mejor_costo_mongo:
            mejor_costo_mongo = costo
            mejor_compu = compu
            mejor_camino_mongo = camino

    print(f"   Mejor opción: {mejor_compu} (costo: {mejor_costo_mongo}) -> {' -> '.join(mejor_camino_mongo)}")

    # g) Cambiar conexión de impresora al Router 2 y repetir punto b
    print("\ng) Cambiando la conexión de la impresora al Router 2 y repitiendo punto b:")
    g.delete_edge("Switch 1", "Impresora")
    g.add_edge(22, "Router 2", "Impresora")
    barridos_desde_notebooks(g)


# =====================================================================
# EJERCICIO 14 - Ambientes de una casa
# =====================================================================
def cargar_casa() -> Graph:
    g = Graph(is_dir=False)

    ambientes = [
        "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
        "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
    ]
    for amb in ambientes:
        g.add_vertex(amb, other_values={"tipo": "ambiente"})

    distancias = [
        (4, "sala de estar", "comedor"),
        (6, "sala de estar", "habitación 1"),
        (7, "sala de estar", "habitación 2"),
        (5, "sala de estar", "baño 1"),
        (10, "sala de estar", "terraza"),
        (3, "comedor", "cocina"),
        (5, "comedor", "patio"),
        (6, "comedor", "baño 1"),
        (9, "comedor", "quincho"),
        (4, "cocina", "patio"),
        (8, "cocina", "cochera"),
        (6, "cochera", "patio"),
        (10, "cochera", "quincho"),
        (3, "quincho", "patio"),
        (3, "baño 1", "habitación 1"),
        (2, "baño 2", "habitación 2"),
        (4, "baño 2", "habitación 1"),
        (6, "baño 2", "terraza"),
        (5, "habitación 2", "terraza"),
    ]

    for peso, a, b in distancias:
        g.add_edge(peso, a, b)

    return g


def ejercicio_14():
    g = cargar_casa()

    print("\n" + "=" * 70)
    print("EJERCICIO 14")
    print("=" * 70)

    # b) Cantidad de aristas por cada ambiente
    print("\nb) Cantidad de aristas por ambiente:")
    for vertex in g:
        print(f"   {vertex.value}: {len(vertex.edges)} aristas")

    # c) Árbol de expansión mínima (cable de red para conectar todos)
    print("\nc) Árbol de expansión mínima (Kruskal):")
    min_tree = g.kruskal("sala de estar")
    cable_total = 0
    for edge in min_tree.split(";"):
        orig, dest, peso = edge.split("-")
        print(f"   {orig} - {dest}: {peso} m")
        cable_total += int(peso)
    print(f"   Total de cable necesario: {cable_total} metros")

    # d) Camino más corto: habitación 1 -> sala de estar
    print("\nd) Camino más corto desde 'habitación 1' hasta 'sala de estar':")
    costo, camino = camino_minimo(g, "habitación 1", "sala de estar")
    print(f"   Ruta: {' -> '.join(camino)}")
    print(f"   Cable necesario: {costo} metros")


if __name__ == "__main__":
    ejercicio_5()
    ejercicio_14()
