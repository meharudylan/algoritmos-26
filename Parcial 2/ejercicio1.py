import json
import random
import sys
from pathlib import Path

from list_ import List
from queue_ import Queue
from tree import BinaryTree



# Lista de Pokémon desde el JSON

def guardar_json(lista, ruta="pokemons.json"):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(list(lista), archivo, ensure_ascii=False, indent=2)


def cargar_json(ruta="pokemons.json"):
    lista = List()
    with open(ruta, encoding="utf-8") as archivo:
        lista.extend(json.load(archivo))
    return lista



def armar_arboles(lista):
    arbol_nombre = BinaryTree()
    arbol_numero = BinaryTree()
    arbol_tipo = BinaryTree()

    random.shuffle(lista)  
    for p in lista:
        arbol_nombre.insert_node(p["nombre"], p)
        arbol_numero.insert_node(p["numero"], p)
        
        for tipo in p["tipos"]:
            nodo = arbol_tipo.search(tipo)
            if nodo is None:
                arbol_tipo.insert_node(tipo, [p])
            else:
                nodo.other_values.append(p)
    return arbol_nombre, arbol_numero, arbol_tipo



def inorden(root):
    if root is not None:
        yield from inorden(root.left)
        yield root
        yield from inorden(root.right)


def por_nivel(root):
    pendientes = Queue()
    if root is not None:
        pendientes.arrive((root, 0))
        while pendientes.size() > 0:
            nodo, nivel = pendientes.attention()
            yield nodo, nivel
            if nodo.left is not None:
                pendientes.arrive((nodo.left, nivel + 1))
            if nodo.right is not None:
                pendientes.arrive((nodo.right, nivel + 1))


def mostrar(p):
    print(f"#{p['numero']:04d} {p['nombre']} | tipos: {', '.join(p['tipos'])} | "
          f"débil a: {', '.join(p['debilidades'])} | "
          f"mega: {'sí' if p['mega'] else 'no'} | gigamax: {'sí' if p['gigamax'] else 'no'}")


# 3. Consignas
def buscar_por_numero(arbol_numero, numero):
    nodo = arbol_numero.search(numero)
    if nodo is None:
        print(f"No existe el Pokémon número {numero}")
    else:
        mostrar(nodo.other_values)


def buscar_por_proximidad(arbol_nombre, texto):
    """'bul' -> todos los nombres que comienzan o contienen 'bul'."""
    texto = texto.lower()
    for nodo in inorden(arbol_nombre.root):
        if texto in nodo.value.lower():
            mostrar(nodo.other_values)


def nombres_por_tipo(arbol_tipo, tipo):
    nodo = arbol_tipo.search(tipo)
    nombres = [p["nombre"] for p in nodo.other_values] if nodo else []
    print(f"Tipo {tipo} ({len(nombres)}): {', '.join(nombres)}")


def listado_por_numero(arbol_numero):
    for nodo in inorden(arbol_numero.root):
        print(nodo.value, nodo.other_values["nombre"])


def listado_por_nombre(arbol_nombre):
    for nodo in inorden(arbol_nombre.root):
        print(nodo.value, f"(#{nodo.other_values['numero']})")


def listado_por_nivel_nombre(arbol_nombre):
    for nodo, nivel in por_nivel(arbol_nombre.root):
        print(f"nivel {nivel}: {nodo.value}")


def debiles_frente_a(arbol_nombre, arbol_numero, nombre):
    """Débiles frente a un Pokémon: los que tienen entre sus
    debilidades alguno de los tipos de ese Pokémon."""
    atacante = arbol_nombre.search(nombre)
    if atacante is None:
        print(f"{nombre} no está cargado")
        return
    tipos = atacante.other_values["tipos"]
    debiles = [n.other_values["nombre"] for n in inorden(arbol_numero.root)
               if any(t in n.other_values["debilidades"] for t in tipos)]
    print(f"Débiles frente a {nombre} ({', '.join(tipos)}) - {len(debiles)}: {', '.join(debiles)}")


def cantidad_por_tipo(arbol_tipo):
    for nodo in inorden(arbol_tipo.root):
        print(f"{nodo.value}: {len(nodo.other_values)}")


def contar_mega(arbol_numero):
    return sum(1 for n in inorden(arbol_numero.root) if n.other_values["mega"])


def contar_gigamax(arbol_numero):
    return sum(1 for n in inorden(arbol_numero.root) if n.other_values["gigamax"])


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    ruta = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("pokemons.json")
    lista = cargar_json(ruta)
    print(f"Pokémon cargados: {len(lista)}\n")
    arbol_nombre, arbol_numero, arbol_tipo = armar_arboles(lista)

    print("--- Buscar por número (25) ---")
    buscar_por_numero(arbol_numero, 25)

    print("\n--- Buscar por proximidad ('bul') ---")
    buscar_por_proximidad(arbol_nombre, "bul")

    print("\n--- Nombres por tipo ---")
    for tipo in ["fantasma", "fuego", "acero", "eléctrico"]:
        nombres_por_tipo(arbol_tipo, tipo)

    print("\n--- Listado por número ---")
    listado_por_numero(arbol_numero)

    print("\n--- Listado por nombre ---")
    listado_por_nombre(arbol_nombre)

    print("\n--- Listado por nivel (árbol de nombres) ---")
    listado_por_nivel_nombre(arbol_nombre)

    print("\n--- Débiles frente a ---")
    for nombre in ["Jolteon", "Lycanroc", "Tyrantrum"]:
        debiles_frente_a(arbol_nombre, arbol_numero, nombre)

    print("\n--- Cantidad por tipo ---")
    cantidad_por_tipo(arbol_tipo)

    print("\nPokémon con megaevolución:", contar_mega(arbol_numero))
    print("Pokémon con forma gigamax:", contar_gigamax(arbol_numero))
