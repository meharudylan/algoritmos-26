#Ejercicio 20
OPUESTOS = {
    'norte': 'sur',     'sur': 'norte',
    'este': 'oeste',    'oeste': 'este',
    'noreste': 'suroeste', 'suroeste': 'noreste',
    'noroeste': 'sureste', 'sureste': 'noroeste'
}

DIRECCIONES_VALIDAS = set(OPUESTOS.keys())

pila = []

def registrar_movimiento(pasos, direccion):
    if direccion not in DIRECCIONES_VALIDAS:
        print(f"Dirección '{direccion}' no válida.")
        return
    if pasos <= 0:
        print("La cantidad de pasos debe ser positiva.")
        return
    pila.append((pasos, direccion))

def volver_a_origen():
    if not pila:
        print("El robot ya está en el origen.")
        return
    pila_aux = pila.copy()
    while pila_aux:
        pasos, direccion = pila_aux.pop()
        opuesta = OPUESTOS[direccion]
        print(f"{pasos} paso(s) al {opuesta}")

#Ejercicio 22
# Pila de personajes MCU
# Cada elemento es una tupla (nombre, peliculas)
# El último elemento es la CIMA de la pila
pila_mcu = [
    ("Thor", 8),
    ("Hawkeye", 5),
    ("Black Widow", 7),
    ("Groot", 4),
    ("War Machine", 6),
    ("Rocket Raccoon", 9),  # ← cima (posición 1)
]

# a) Posición de un personaje (cima = posición 1)
def buscar_personaje(pila, nombre, pos=1):
    if not pila:
        return f"{nombre} no está en la pila."
    if pila[-1][0] == nombre:
        return f"{nombre} está en la posición {pos}."
    return buscar_personaje(pila[:-1], nombre, pos + 1)

# b) Personajes con más de 5 películas
def mas_de_cinco(pila):
    if not pila:
        return []
    resto = mas_de_cinco(pila[:-1])
    nombre, peliculas = pila[-1]
    if peliculas > 5:
        return resto + [(nombre, peliculas)]
    return resto

# c) Películas de un personaje específico
def buscar_peliculas(pila, nombre):
    if not pila:
        return f"{nombre} no está en la pila."
    if pila[-1][0] == nombre:
        return f"{nombre} participó en {pila[-1][1]} películas."
    return buscar_peliculas(pila[:-1], nombre)

# d) Personajes cuyo nombre empieza con C, D o G
def filtrar_por_letra(pila, letras=('C', 'D', 'G')):
    if not pila:
        return []
    resto = filtrar_por_letra(pila[:-1], letras)
    nombre, peliculas = pila[-1]
    if nombre[0].upper() in letras:
        return resto + [nombre]
    return resto

# --- Llamadas ---
print(buscar_personaje(pila_mcu, "Rocket Raccoon"))
print(buscar_personaje(pila_mcu, "Groot"))

print("\nPersonajes con más de 5 películas:")
for nombre, peliculas in mas_de_cinco(pila_mcu):
    print(f"  {nombre}: {peliculas} películas")

print(buscar_peliculas(pila_mcu, "Black Widow"))

print("\nPersonajes que empiezan con C, D o G:")
for nombre in filtrar_por_letra(pila_mcu):
    print(f"  {nombre}")