from collections import deque
from heapq import heappop, heappush
from math import inf, isinf

from graph import Graph


def build_exercise_5(printer_router="Switch 1"):
    vertices = [
        ("Red Hat", "notebook"),
        ("Debian", "notebook"),
        ("Ubuntu", "pc"),
        ("Mint", "pc"),
        ("Impresora", "impresora"),
        ("Guarani", "servidor"),
        ("Router 2", "router"),
        ("Router 1", "router"),
        ("Router 3", "router"),
        ("Manjaro", "pc"),
        ("Fedora", "pc"),
        ("Arch", "notebook"),
        ("Parrot", "pc"),
        ("Switch 1", "switch"),
        ("Switch 2", "switch"),
        ("MongoDB", "servidor"),
    ]
    edges = [
        ("Red Hat", "Router 2", 25),
        ("Router 2", "Guarani", 9),
        ("Router 2", "Router 3", 50),
        ("Router 2", "Router 1", 37),
        ("Router 1", "Router 3", 43),
        ("Router 1", "Switch 1", 29),
        ("Debian", "Switch 1", 17),
        ("Ubuntu", "Switch 1", 18),
        ("Switch 1", "Mint", 80),
        ("Router 3", "Switch 2", 61),
        ("Manjaro", "Switch 2", 40),
        ("Parrot", "Switch 2", 12),
        ("Fedora", "Switch 2", 3),
        ("Arch", "Switch 2", 56),
        ("Switch 2", "MongoDB", 5),
    ]

    if printer_router == "Switch 1":
        edges.insert(8, ("Switch 1", "Impresora", 22))
    elif printer_router == "Router 2":
        edges.append(("Router 2", "Impresora", 22))
    else:
        raise ValueError("printer_router must be 'Switch 1' or 'Router 2'")

    return _build_graph(vertices, edges)


def build_exercise_14():
    vertices = [
        ("Cocina", "ambiente"),
        ("Comedor", "ambiente"),
        ("Cochera", "ambiente"),
        ("Quincho", "ambiente"),
        ("Baño 1", "ambiente"),
        ("Baño 2", "ambiente"),
        ("Habitación 1", "ambiente"),
        ("Habitación 2", "ambiente"),
        ("Sala de estar", "ambiente"),
        ("Terraza", "ambiente"),
        ("Patio", "ambiente"),
    ]
    edges = [
        ("Cocina", "Comedor", 5),
        ("Comedor", "Baño 1", 4),
        ("Baño 1", "Habitación 1", 6),
        ("Habitación 1", "Baño 2", 3),
        ("Baño 2", "Habitación 2", 4),
        ("Habitación 2", "Sala de estar", 5),
        ("Sala de estar", "Terraza", 6),
        ("Terraza", "Patio", 4),
        ("Patio", "Quincho", 7),
        ("Quincho", "Cochera", 6),
        ("Cochera", "Cocina", 8),
        ("Cocina", "Habitación 1", 10),
        ("Cocina", "Sala de estar", 11),
        ("Cocina", "Quincho", 9),
        ("Sala de estar", "Comedor", 3),
        ("Sala de estar", "Cochera", 5),
        ("Habitación 1", "Patio", 8),
        ("Baño 1", "Baño 2", 2),
        ("Habitación 2", "Terraza", 3),
    ]
    return _build_graph(vertices, edges)


def _build_graph(vertices, edges):
    graph = Graph(is_dir=False)
    for name, vertex_type in vertices:
        graph.add_vertex(name, vertex_type)
    for origin, destination, weight in edges:
        graph.add_edge(weight, origin, destination)
    return graph


def _get_vertex(graph, name):
    position = graph.search(name, "value")
    if position is None:
        raise ValueError(f"Unknown vertex: {name}")
    return graph[position]


def depth_first_search(graph, origin):
    _get_vertex(graph, origin)
    visited = set()
    result = []
    pending = [origin]

    while pending:
        current = pending.pop()
        if current in visited:
            continue
        visited.add(current)
        result.append(current)
        neighbors = [edge.destination for edge in _get_vertex(graph, current).edges]
        pending.extend(reversed(neighbors))

    return result


def breadth_first_search(graph, origin):
    _get_vertex(graph, origin)
    visited = {origin}
    result = []
    pending = deque([origin])

    while pending:
        current = pending.popleft()
        result.append(current)
        for edge in _get_vertex(graph, current).edges:
            if edge.destination not in visited:
                visited.add(edge.destination)
                pending.append(edge.destination)

    return result


def shortest_path(graph, origin, destination):
    _get_vertex(graph, origin)
    _get_vertex(graph, destination)

    distances = {vertex.value: inf for vertex in graph}
    previous_vertices = {vertex.value: None for vertex in graph}
    distances[origin] = 0
    pending = [(0, origin)]

    while pending:
        distance, current = heappop(pending)
        if distance != distances[current]:
            continue
        if current == destination:
            break
        for edge in _get_vertex(graph, current).edges:
            if edge.weight < 0:
                raise ValueError("Dijkstra requires non-negative edge weights")
            candidate_distance = distance + edge.weight
            if candidate_distance < distances[edge.destination]:
                distances[edge.destination] = candidate_distance
                previous_vertices[edge.destination] = current
                heappush(pending, (candidate_distance, edge.destination))

    if isinf(distances[destination]):
        raise ValueError(f"No path from {origin} to {destination}")

    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous_vertices[current]
    path.reverse()
    return path, distances[destination]


def minimum_spanning_tree(graph):
    if not graph:
        return [], 0

    representatives = {vertex.value: vertex.value for vertex in graph}

    def find(vertex):
        while representatives[vertex] != vertex:
            representatives[vertex] = representatives[representatives[vertex]]
            vertex = representatives[vertex]
        return vertex

    pending = []
    seen_edges = set()
    for vertex in graph:
        for edge in vertex.edges:
            endpoints = tuple(sorted((vertex.value, edge.destination)))
            if endpoints not in seen_edges:
                seen_edges.add(endpoints)
                heappush(pending, (edge.weight, endpoints[0], endpoints[1]))

    edges = []
    total = 0
    while pending and len(edges) < len(graph) - 1:
        weight, origin, destination = heappop(pending)
        origin_root = find(origin)
        destination_root = find(destination)
        if origin_root != destination_root:
            representatives[origin_root] = destination_root
            edges.append((origin, destination, weight))
            total += weight

    if len(edges) != len(graph) - 1:
        raise ValueError("A minimum spanning tree requires a connected graph")

    return edges, total


def _format_path(path, distance, unit=""):
    suffix = f" {unit}" if unit else ""
    return f"{' -> '.join(path)} ({distance}{suffix})"


def _print_wrapped(prefix, value, width=88):
    parts = value.split(" -> ")
    if len(parts) == 1:
        print(f"{prefix}{value}")
        return

    line = f"{prefix}{parts[0]}"
    for part in parts[1:]:
        if len(line) + len(part) + 4 <= width:
            line += f" -> {part}"
        else:
            print(line)
            line = f"{' ' * len(prefix)}-> {part}"
    print(line)


def _print_traversals(graph, origins):
    for origin in origins:
        print(f"  Desde {origin}:")
        _print_wrapped(
            "    Profundidad: ",
            " -> ".join(depth_first_search(graph, origin)),
        )
        _print_wrapped(
            "    Amplitud:    ",
            " -> ".join(breadth_first_search(graph, origin)),
        )


def _print_minimum_spanning_tree(graph, unit=""):
    edges, total = minimum_spanning_tree(graph)
    suffix = f" {unit}" if unit else ""
    print("  Aristas:")
    for origin, destination, weight in edges:
        print(f"    {origin} -- {destination}: {weight}{suffix}")
    print(f"  Total: {total}{suffix}")


def _nearest_route(graph, candidates, destination):
    routes = []
    for origin in candidates:
        path, distance = shortest_path(graph, origin, destination)
        routes.append((distance, origin, path))
    if not routes:
        raise ValueError(f"No candidates can reach {destination}")
    return min(routes)


def _print_exercise_5():
    graph = build_exercise_5()
    notebooks = ["Red Hat", "Debian", "Arch"]
    print("=" * 88)
    print("EJERCICIO 5 - RED ORIGINAL")
    print("=" * 88)

    print("\n[a] Tipos de equipos")
    name_width = max(len(vertex.value) for vertex in graph)
    print(f"  {'Equipo':<{name_width}} | Tipo")
    print(f"  {'-' * name_width}-+----------")
    for vertex in graph:
        print(f"  {vertex.value:<{name_width}} | {vertex.other_values}")

    print("\n[b] Recorridos desde las notebooks (profundidad y amplitud)")
    _print_traversals(graph, notebooks)

    print("\n[c] Caminos más cortos hasta la impresora")
    for origin in ["Manjaro", "Red Hat", "Fedora"]:
        path, distance = shortest_path(graph, origin, "Impresora")
        print(f"  Desde {origin}:")
        _print_wrapped("    Ruta: ", _format_path(path, distance))

    print("\n[d] Árbol de expansión mínima")
    _print_minimum_spanning_tree(graph)

    pc_candidates = [
        vertex.value for vertex in graph if vertex.other_values == "pc"
    ]
    nearest_pc = _nearest_route(graph, pc_candidates, "Guarani")
    print("\n[e] PC (no notebook) más cercana al servidor Guarani")
    print(f"  Equipo: {nearest_pc[1]}")
    _print_wrapped(
        "  Ruta: ",
        _format_path(nearest_pc[2], nearest_pc[0]),
    )

    switch_1 = _get_vertex(graph, "Switch 1")
    computer_candidates = [
        edge.destination
        for edge in switch_1.edges
        if _get_vertex(graph, edge.destination).other_values in {"pc", "notebook"}
    ]
    nearest_computer = _nearest_route(graph, computer_candidates, "MongoDB")
    pc_only_candidates = [
        name
        for name in computer_candidates
        if _get_vertex(graph, name).other_values == "pc"
    ]
    nearest_pc_on_switch = _nearest_route(graph, pc_only_candidates, "MongoDB")

    print("\n[f] Computadora de Switch 1 más cercana a MongoDB")
    print(
        f"  Equipo: {nearest_computer[1]} "
        f"({_get_vertex(graph, nearest_computer[1]).other_values})"
    )
    _print_wrapped(
        "  Ruta: ",
        _format_path(nearest_computer[2], nearest_computer[0]),
    )
    print("  Si se consideran solo equipos tipo PC:")
    _print_wrapped(
        f"    Equipo: {nearest_pc_on_switch[1]} | Ruta: ",
        _format_path(nearest_pc_on_switch[2], nearest_pc_on_switch[0]),
    )

    moved_printer_graph = build_exercise_5(printer_router="Router 2")
    print("\n[g] Recorridos al conectar la impresora al Router 2")
    _print_traversals(moved_printer_graph, notebooks)
    print("\n[h] Tipo de grafo: no dirigido")
    print("=" * 88)


def _print_exercise_14():
    graph = build_exercise_14()
    print("\n" + "=" * 88)
    print("EJERCICIO 14 - CONEXIONES DE UNA CASA")
    print("=" * 88)

    print("\n[a] Ambientes representados por los vértices")
    for vertex in graph:
        print(f"  - {vertex.value}")

    print("\n[b] Aristas y distancias (metros)")
    for vertex in graph:
        for edge in vertex.edges:
            if vertex.value < edge.destination:
                print(f"    {vertex.value} -- {edge.destination}: {edge.weight} m")

    print("\n  Cantidad de conexiones por ambiente (mínimo requerido: 3)")
    name_width = max(len(vertex.value) for vertex in graph)
    for vertex in graph:
        print(f"    {vertex.value:<{name_width}} | {len(vertex.edges)} conexiones")

    print("\n[c] Árbol de expansión mínima")
    _print_minimum_spanning_tree(graph, "m")

    path, distance = shortest_path(graph, "Habitación 1", "Sala de estar")
    print("\n[d] Camino más corto para el cable de red")
    print("  Se toma Habitación 1 como ubicación del router y Sala de estar")
    print("  como ubicación del Smart TV.")
    _print_wrapped(
        "  Ruta más corta: ",
        _format_path(path, distance, "m"),
    )
    print(f"  Cable necesario: {distance} m")
    print("=" * 88)


def main():
    _print_exercise_5()
    _print_exercise_14()


if __name__ == "__main__":
    main()
