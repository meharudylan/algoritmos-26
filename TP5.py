# ============================================================================
# TRABAJO PRACTICO 5: ARBOLES BINARIOS DE BUSQUEDA (AVL)
# Ejercicios 5 (MCU Superheroes y Villanos) y 23 (Criaturas Mitologicas)
# ============================================================================

from tree import BinaryTree
from super_heroes_data import superheroes
from criatura import Criatura, Criaturas
import unicodedata


# ============================================================================
# FUNCIONES AUXILIARES DE BUSQUEDA
# ============================================================================

def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )


# ============================================================================
# EJERCICIO 5 (SUPERHEROES Y VILLANOS MCU)
# ============================================================================

def ejercicio_5():
    print("=" * 80)
    print("EJERCICIO 5: SUPERHEROES Y VILLANOS DE MCU")
    print("=" * 80)

    arbol_marvel = BinaryTree()

    # a) Cargar árbol con campo booleano (is_villain: True/False)
    for c in superheroes:
        arbol_marvel.insert_node(c['name'], other_value=c)

    print("\n--- a. Árbol cargado ---")
    print(f"Cantidad total de elementos: {len(superheroes)}")

    # b) Listar villanos ordenados alfabéticamente
    print("\n--- b. Villanos ordenados alfabéticamente ---")
    arbol_marvel.inorden_villain()

    # c) Mostrar superhéroes que empiezan con 'C'
    print("\n--- c. Superhéroes que empiezan con 'C' ---")
    arbol_marvel.inorden_hero_star_with('C')

    # d) Determinar cuántos superhéroes hay en el árbol
    print("\n--- d. Cantidad de superhéroes ---")
    print(f"Cantidad de héroes: {arbol_marvel.count_heroes()}")

    # e) Modificar 'Dr. Strange' a 'Doctor Strange' usando búsqueda por proximidad
    print("\n--- e. Búsqueda por proximidad y modificación ---")
    arbol_marvel.proxy_search("strange")

    node = arbol_marvel.search("Dr. Strange")
    if node is not None:
        delete_val, delete_other = arbol_marvel.delete_node("Dr. Strange")
        new_name = "Doctor Strange"
        delete_other['name'] = new_name
        arbol_marvel.insert_node(new_name, delete_other)
        print(f"[+] '{delete_val}' modificado correctamente a '{new_name}'")

    # f) Listar superhéroes ordenados de manera descendente
    print("\n--- f. Superhéroes en orden descendente ---")
    arbol_marvel.postorden_hero()

    # g) Generar bosque (Héroes y Villanos separados)
    print("\n--- g. Generar Bosque ---")
    arbol_heroes, arbol_villanos = arbol_marvel.generar_bosque()

    print("\n--- g.I Cantidad de nodos ---")
    print(f"Nodos en Héroes:   {arbol_heroes.count_heroes()}")
    print(f"Nodos en Villanos: {arbol_villanos.count_villains()}")

    print("\n--- g.II Barrido alfabético de Héroes ---")
    arbol_heroes.inorden()

    print("\n--- g.II Barrido alfabético de Villanos ---")
    arbol_villanos.inorden()


# ============================================================================
# EJERCICIO 23 (CRIATURAS MITOLOGICAS)
# ============================================================================

def ejercicio_23():
    print("\n\n" + "=" * 80)
    print("EJERCICIO 23: CRIATURAS DE LA MITOLOGIA GRIEGA")
    print("=" * 80)

    arbol_criaturas = BinaryTree()
    for c in Criaturas:
        arbol_criaturas.insert_node(c.name, other_value=c)

    # a) Listado inorden de criaturas y quién las derrotó
    print("\n--- a. Listado inorden de criaturas y quién las derrotó ---")
    def __inorden_derrotas(root):
        if root is not None:
            __inorden_derrotas(root.left)
            obj = root.other_values
            print(f"  * {obj.name:<25} | Derrotado por: {obj.killer if obj.killer else 'Nadie (-)'}")
            __inorden_derrotas(root.right)
    __inorden_derrotas(arbol_criaturas.root)

    # b) Descripción sobre cada criatura
    print("\n--- b. Descripción sobre cada criatura ---")
    print("  [+] Cargas realizadas con su descripción correspondiente.")

    # c) Información completa de Talos
    print("\n--- c. Información completa de Talos ---")
    talos = arbol_criaturas.search("Talos")
    if talos is not None:
        print(f"  {talos.other_values}")

    # d) Top 3 héroes/dioses que derrotaron más criaturas
    print("\n--- d. Top 3 héroes/dioses con más derrotas ---")
    conteo = {}
    def __contar_derrotas(root):
        if root is not None:
            __contar_derrotas(root.left)
            killer = root.other_values.killer
            if killer and killer != "-":
                conteo[killer] = conteo.get(killer, 0) + 1
            __contar_derrotas(root.right)
    __contar_derrotas(arbol_criaturas.root)
    top3 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]
    for pos, (h, cant) in enumerate(top3, 1):
        print(f"  {pos}. {h}: {cant} criatura(s)")

    # e) Criaturas derrotadas por Heracles
    print("\n--- e. Criaturas derrotadas por Heracles ---")
    def __derrotados_por(root, heroe):
        if root is not None:
            __derrotados_por(root.left, heroe)
            if root.other_values.killer == heroe:
                print(f"  * {root.value}")
            __derrotados_por(root.right, heroe)
    __derrotados_por(arbol_criaturas.root, "Heracles")

    # f) Criaturas no derrotadas
    print("\n--- f. Criaturas no derrotadas ---")
    def __no_derrotadas(root):
        if root is not None:
            __no_derrotadas(root.left)
            if not root.other_values.killer or root.other_values.killer == "-":
                print(f"  * {root.value}")
            __no_derrotadas(root.right)
    __no_derrotadas(arbol_criaturas.root)

    # g) Campo 'captured'
    print("\n--- g. Campo 'captured' ---")
    print("  [+] Campo 'captured' listo en la clase Criatura.")

    # h) Modificar capturas de Heracles
    print("\n--- h. Heracles atrapó a Cerbero, Toro de Creta, Cierva de Cerinea y Jabalí de Erimanto ---")
    capturados = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
    for nombre in capturados:
        node = arbol_criaturas.search(nombre)
        if node:
            node.other_values.captured = "Heracles"
            print(f"  [+] {nombre} -> Capturada por Heracles")

    # i) Búsqueda por coincidencia
    print("\n--- i. Búsqueda por coincidencia ('Dragon') ---")
    def __coincidencia(root, cadena):
        if root is not None:
            __coincidencia(root.left, cadena)
            if remove_accents(cadena).lower() in remove_accents(root.value).lower():
                print(f"  * {root.other_values}")
            __coincidencia(root.right, cadena)
    __coincidencia(arbol_criaturas.root, "Dragon")

    # j) Eliminar Basilisco y Sirenas
    print("\n--- j. Eliminar Basilisco y Sirenas ---")
    for a_eliminar in ["Basilisco", "Sirenas"]:
        val, _ = arbol_criaturas.delete_node(a_eliminar)
        if val:
            print(f"  [+] '{val}' eliminada.")

    # k) Modificar Aves del Estínfalo
    print("\n--- k. Modificar Aves del Estínfalo ---")
    aves = arbol_criaturas.search("Aves del Estínfalo")
    if aves:
        aves.other_values.killer = "Heracles"
        aves.other_values.description += " (Heracles derrotó a varias)."
        print("  [+] Aves del Estínfalo actualizadas.")

    # l) Renombrar Ladón a Dragón Ladón
    print("\n--- l. Renombrar 'Ladón' a 'Dragón Ladón' ---")
    old_val, old_obj = arbol_criaturas.delete_node("Ladón")
    if old_val and old_obj:
        old_obj.name = "Dragón Ladón"
        arbol_criaturas.insert_node("Dragón Ladón", old_obj)
        print("  [+] 'Ladón' renombrado a 'Dragón Ladón'.")

    # m) Listado por nivel del árbol
    print("\n--- m. Listado por nivel del árbol (BFS) ---")
    arbol_criaturas.by_level()

    # n) Criaturas capturadas por Heracles
    print("\n--- n. Criaturas capturadas por Heracles ---")
    def __capturadas_por(root, heroe):
        if root is not None:
            __capturadas_por(root.left, heroe)
            if root.other_values.captured == heroe:
                print(f"  * {root.value}")
            __capturadas_por(root.right, heroe)
    __capturadas_por(arbol_criaturas.root, "Heracles")


# ============================================================================
# MAIN
# ============================================================================

def main():
    ejercicio_5()
    ejercicio_23()

    print("\n" + "=" * 80)
    print("                 FIN DEL TRABAJO PRACTICO 5")
    print("=" * 80)


if __name__ == "__main__":
    main()