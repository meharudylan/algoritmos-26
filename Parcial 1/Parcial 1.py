# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.

# from list_ import List


# superheroes = [
#     "Hulk", "Ironman", "Spiderman", "CapitanAmerica", "Thanos",
#     "Thor", "Wolverine", "Daredevil", "Punisher", "Loki",
#     "Nova", "Groot", "Pantera Negra", "She Hulk", "Gamora"
# ]


# def busqueda_recursiva(superheroes, CapitanAmerica :str, i=0):
    
#     if i == len(superheroes):  
#         return -1
#     if superheroes[i] == CapitanAmerica:  
#         return i
#     return busqueda_recursiva(superheroes, CapitanAmerica, i + 1)  

# def listar_superheroes(superheroes, i=0):
   
#     if i == len(superheroes): 
#         return
#     print(f"{i}: {superheroes[i]}")
#     listar_superheroes(superheroes, i + 1) 



# print()
# nombre_buscado = "CapitanAmerica"
# posicion = busqueda_recursiva(superheroes, nombre_buscado)

# if posicion != -1:
#     print(f'"{nombre_buscado}" encontrado en la posición {posicion}')
# else:
#     print(f'"{nombre_buscado}" no está en la lista')

# print()
# print("Listado completo:")
# listar_superheroes(superheroes)


#Ejercicio 2
# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
# Listado ordenado de manera ascendente por nombre de los personajes.
# Determinar en que posicion esta The Thing y Rocket Raccoon.
# Listar todos los villanos de la lista.
# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# Listar los superheores que comienzan con  Bl, G, My, y W.
# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# Listado de superheroes ordenados por fecha de aparación.
# Modificar el nombre real de Ant Man a Scott Lang.
# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.



from super_heroes_data import superheroes
from collections import deque
from list_ import List


class Personaje:
    def __init__(self, data):
        self.nom       = data["name"]
        self.alias     = data["alias"]
        self.nom_real  = data["real_name"] or "Desconocido" 
        self.bio       = data["short_bio"]
        self.aparicion = data["first_appearance"]
        self.villano   = data["is_villain"]

    def __str__(self):
        tipo = "Villano" if self.villano else "Héroe"
        return f"{self.nom} ({self.nom_real}) | {tipo} | {self.aparicion}"



lista = List()
for h in superheroes:
    lista.append(Personaje(h))



# 1. Listado ordenado por nombre ascendente
print("1. ORDENADO POR NOMBRE")
lista.sort(key=lambda x: x.nom)
for p in lista:
    print(p.nom)

print()

# 2. Posición de The Thing y Rocket Raccoon

print("2. POSICIÓN")
for nombre in ["The Thing", "Rocket Raccoon"]:
    pos = lista.search(nombre)
    if pos != -1:
        print(f'"{nombre}" está en la posición {pos}')
    else:
        print(f'"{nombre}" no encontrado')

print()

# 3. Listar todos los villanos

print("3. VILLANOS")
for p in lista:
    if p.villano:
        print(p.nom)

print()

# 4. Cola de villanos (anteriores a 1980)

print("4. VILLANOS ANTES DE 1980")
cola = deque(p for p in lista if p.villano)
while cola:
    v = cola.popleft()
    if v.aparicion < 1980:
        print(v)

print()

# 5. Personajes que comienzan con Bl, G, My, W

print("5. Bl / G / My / W")
prefijos = ("Bl", "G", "My", "W")
for p in lista:
    if p.nom.startswith(prefijos):
        print(p)

print()

# 6. Ordenado por nombre real ascendente

print("\n=== 6. ORDENADO POR NOMBRE REAL ===")
lista.sort(key=lambda x: x.nom_real)
lista.show()

print()

# 7. Ordenado por fecha de aparición

print("\n=== 7. ORDENADO POR APARICIÓN ===")
lista.sort(key=lambda x: x.aparicion)
lista.show()

print()

# 8. Modificar nombre real de Ant Man a Scott Lang

print("\n=== 8. MODIFICAR ANT-MAN ===")
for p in lista:
    if p.nom == "Ant Man":
        p.nom_real = "Scott Lang"
        print(f"Actualizado: {p}")
        break

print()

# 9. Biografía con "time-traveling" o "suit"

print("9. PALABRAS CLAVE EN BIO")
for p in lista:
    if "time-traveling" in p.bio.lower() or "suit" in p.bio.lower():
        print(f" {p.nom}: {p.bio}")

print()

# 10. Eliminar Electro y Baron Zemo

print(" 10. ELIMINAR PERSONAJES")
for nombre in ["Electro", "Baron Zemo"]:
    encontrado = False
    for p in lista:
        if p.nom == nombre:
            print(f"Eliminado: {p}")
            lista.remove(p)
            encontrado = True
            break
    if not encontrado:
        print(f'"{nombre}" no estaba en la lista')