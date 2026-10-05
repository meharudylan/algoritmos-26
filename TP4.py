# ============================================================================
# TRABAJO PRACTICO 4: LISTAS EN PYTHON
# Ejercicios 6 (Superheroes) y 15 (Entrenadores Pokemon)
# ============================================================================

from superheroe import Superheroe, ListaSuperheroes
from pokemon import Pokemon, ListaPokemon
from entrenador import Entrenador, ListaEntrenadores


# ============================================================================
# DATOS EJERCICIO 6 (SUPERHEROES)
# ============================================================================

superheroes_data = [
    ("Superman",        1938, "DC",     "Kal-El fue enviado desde Krypton. Usa sus poderes solares para defender la Tierra con traje azul y rojo."),
    ("Batman",          1939, "DC",     "Bruce Wayne juró proteger Gotham. Usa armadura con herramientas y gadgets especiales."),
    ("Spider-Man",      1962, "Marvel", "Peter Parker fue mordido por una araña radiactiva. Usa traje rojo y azul."),
    ("Thor",            1962, "Marvel", "Dios nordico del trueno. Empuna el martillo Mjolnir y defiende Asgard y la Tierra."),
    ("Iron Man",        1963, "Marvel", "Tony Stark construyo una armadura tecnologica. Fundador de los Vengadores."),
    ("Mujer Maravilla", 1941, "DC",     "Diana, princesa amazona, porta el lazo de la verdad y brazaletes indestructibles."),
    ("Flash",           1956, "DC",     "Barry Allen puede moverse a velocidades superluminicas conectado a la Fuerza de la Velocidad."),
    ("Wolverine",       1974, "Marvel", "Logan posee esqueleto de adamantium y garras retractiles. Casi inmortal. Icónico X-Men."),
    ("Dr. Strange",     1963, "DC",     "Stephen Strange es el Hechicero Supremo. Usa traje rojo especial y controla las artes misticas."),
    ("Capitana Marvel", 1968, "Marvel", "Carol Danvers obtuvo poderes kree. Vuela y tiene fuerza sobrehumana."),
    ("Star-Lord",       2008, "Marvel", "Peter Quill, lider de los Guardianes de la Galaxia. Usa armadura especial y pistolas de plasma."),
    ("Black Widow",     1964, "Marvel", "Natasha Romanoff, espia de elite de S.H.I.E.L.D. experta en artes marciales."),
    ("Aquaman",         1941, "DC",     "Arthur Curry es rey de Atlantis. Controla el agua y usa tridente dorado como armadura."),
    ("Hulk",            1962, "Marvel", "Bruce Banner se transforma en monstruo verde incontrolable. Fuerza enorme."),
    ("Black Panther",   1966, "Marvel", "T'Challa es rey de Wakanda. Su traje de vibranio lo protege."),
    ("Green Lantern",   1959, "DC",     "Hal Jordan crea construcciones de energia verde con su voluntad e imaginacion."),
]


# ============================================================================
# DATOS EJERCICIO 15 (ENTRENADORES POKEMON)
# ============================================================================

entrenadores_data = [
    {"nombre": "Ash",    "torneos": 5, "perdidas": 10, "ganadas": 35},
    {"nombre": "Misty",  "torneos": 3, "perdidas":  8, "ganadas": 22},
    {"nombre": "Brock",  "torneos": 4, "perdidas": 12, "ganadas": 28},
    {"nombre": "Gary",   "torneos": 6, "perdidas":  5, "ganadas": 40},
    {"nombre": "Blaine", "torneos": 2, "perdidas": 15, "ganadas": 20},
]

pokemons_data = {
    "Ash": [
        ("Pikachu",    55, "Electrico", "Normal"),
        ("Charizard",  60, "Fuego",     "Volador"),
        ("Blastoise",  58, "Agua",      "Normal"),
        ("Venusaur",   57, "Planta",    "Veneno"),
        ("Pikachu",    45, "Electrico", "Normal"),   # repetido
    ],
    "Misty": [
        ("Starmie",   52, "Agua", "Psiquico"),
        ("Golduck",   50, "Agua", "Normal"),
        ("Lapras",    54, "Agua", "Hielo"),
    ],
    "Brock": [
        ("Onix",      48, "Roca",   "Tierra"),
        ("Golem",     55, "Roca",   "Tierra"),
        ("Rhyhorn",   50, "Tierra", "Roca"),
        ("Pineco",    45, "Bicho",  "Acero"),
    ],
    "Gary": [
        ("Tyrantrum", 65, "Roca",   "Dragon"),
        ("Terakion",  68, "Roca",   "Lucha"),
        ("Aerodactyl",62, "Roca",   "Volador"),
        ("Nidoking",  63, "Veneno", "Tierra"),
        ("Arcanine",  61, "Fuego",  "Normal"),
    ],
    "Blaine": [
        ("Charizard", 56, "Fuego", "Volador"),
        ("Magmortar", 58, "Fuego", "Normal"),
        ("Houndoom",  54, "Fuego", "Siniestro"),
        ("Wingull",   40, "Agua",  "Volador"),
    ],
}


# ============================================================================
# EJERCICIO 6
# ============================================================================

def ejercicio_6():
    # --- Cargar superheroes ---
    lista = ListaSuperheroes()
    for nombre, anio, casa, bio in superheroes_data:
        lista.append(Superheroe(nombre, anio, casa, bio))

    # --- Mostrar todos ---
    print("=" * 70)
    print("LISTA COMPLETA DE SUPERHEROES")
    print("=" * 70)
    lista.show()

    # ========== a) ELIMINAR GREEN LANTERN ==========
    print("\n" + "=" * 70)
    print("a) ELIMINAR GREEN LANTERN")
    print("=" * 70)
    eliminado = lista.delete_value("Green Lantern", 'name')
    print(f"Eliminado: {eliminado}")

    # ========== b) AÑO DE WOLVERINE ==========
    print("\n" + "=" * 70)
    print("b) AÑO DE APARICION DE WOLVERINE")
    print("=" * 70)
    idx = lista.search("Wolverine", 'name')
    if idx is not None:
        print(f"Wolverine aparecio en: {lista[idx].year}")

    # ========== c) CAMBIAR CASA DE DR. STRANGE ==========
    print("\n" + "=" * 70)
    print("c) CAMBIAR CASA DE DR. STRANGE (DC -> Marvel)")
    print("=" * 70)
    idx = lista.search("Dr. Strange", 'name')
    if idx is not None:
        casa_anterior = lista[idx].house
        lista[idx].house = "Marvel"
        print(f"Dr. Strange: {casa_anterior} -> {lista[idx].house}")

    # ========== d) BUSCAR 'TRAJE' O 'ARMADURA' EN BIO ==========
    print("\n" + "=" * 70)
    print("d) SUPERHEROES CON 'TRAJE' O 'ARMADURA' EN BIOGRAFIA")
    print("=" * 70)
    lista.filter_contain_on_bio(['traje', 'armadura'])

    # ========== e) ANTERIORES A 1963 ==========
    print("\n" + "=" * 70)
    print("e) SUPERHEROES CON APARICION ANTERIOR A 1963")
    print("=" * 70)
    for hero in lista:
        if hero.year < 1963:
            print(hero)

    # ========== f) CASA DE CAPITANA MARVEL Y MUJER MARAVILLA ==========
    print("\n" + "=" * 70)
    print("f) CASA DE CAPITANA MARVEL Y MUJER MARAVILLA")
    print("=" * 70)
    for nombre_buscado in ["Capitana Marvel", "Mujer Maravilla"]:
        idx = lista.search(nombre_buscado, 'name')
        if idx is not None:
            print(f"{lista[idx].name}: {lista[idx].house}")

    # ========== g) INFO COMPLETA DE FLASH Y STAR-LORD ==========
    print("\n" + "=" * 70)
    print("g) INFORMACION COMPLETA DE FLASH Y STAR-LORD")
    print("=" * 70)
    for nombre_buscado in ["Flash", "Star-Lord"]:
        idx = lista.search(nombre_buscado, 'name')
        if idx is not None:
            h = lista[idx]
            print(f"\n{h.name}:")
            print(f"  Anio: {h.year}")
            print(f"  Casa: {h.house}")
            print(f"  Bio:  {h.bio}")

    # ========== h) POR LETRA INICIAL ==========
    print("\n" + "=" * 70)
    print("h) SUPERHEROES QUE COMIENZAN CON B, M Y S")
    print("=" * 70)
    lista.filter_start_with(('B', 'M', 'S'))

    # ========== i) CONTAR POR CASA ==========
    print("\n" + "=" * 70)
    print("i) CANTIDAD POR CASA")
    print("=" * 70)
    conteo = {}
    for hero in lista:
        conteo[hero.house] = conteo.get(hero.house, 0) + 1
    for casa, cantidad in conteo.items():
        print(f"  {casa}: {cantidad} superheroes")


# ============================================================================
# EJERCICIO 15
# ============================================================================

def ejercicio_15():
    # --- Cargar entrenadores ---
    lista = ListaEntrenadores()
    for d in entrenadores_data:
        e = Entrenador(d['nombre'], d['torneos'], d['perdidas'], d['ganadas'])
        for nombre, nivel, tipo, subtipo in pokemons_data[d['nombre']]:
            e.pokemons.append(Pokemon(nombre, nivel, tipo, subtipo))
        lista.append(e)

    # --- Mostrar todos ---
    print("=" * 70)
    print("LISTA DE ENTRENADORES")
    print("=" * 70)
    for e in lista:
        print(f"\n{e}")
        print(f"  Pokemons ({e.pokemons.size()}):")
        e.pokemons.show()

    # ========== a) CANTIDAD DE POKEMONS ==========
    print("\n" + "=" * 70)
    print("a) CANTIDAD DE POKEMONS")
    print("=" * 70)
    for nombre in ["Ash", "Gary", "Blaine"]:
        idx = lista.search(nombre, 'name')
        if idx is not None:
            print(f"  {lista[idx].name}: {lista[idx].pokemons.size()} pokemons")

    # ========== b) MAS DE 3 TORNEOS ==========
    print("\n" + "=" * 70)
    print("b) ENTRENADORES CON MAS DE 3 TORNEOS")
    print("=" * 70)
    for e in lista:
        if e.tourneys > 3:
            print(f"  {e.name}: {e.tourneys} torneos")

    # ========== c) POKEMON MAYOR NIVEL DEL MEJOR ENTRENADOR ==========
    print("\n" + "=" * 70)
    print("c) POKEMON DE MAYOR NIVEL DEL MEJOR ENTRENADOR")
    print("=" * 70)
    lista.sort_by_criterion('tourneys')
    mejor = lista[-1]
    mejor_pokemon = max(mejor.pokemons, key=lambda p: p.level)
    print(f"  Entrenador: {mejor.name} ({mejor.tourneys} torneos)")
    print(f"  Pokemon: {mejor_pokemon}")

    # ========== d) INFO COMPLETA DE ASH ==========
    print("\n" + "=" * 70)
    print("d) INFORMACION COMPLETA DE ASH")
    print("=" * 70)
    idx = lista.search("Ash", 'name')
    if idx is not None:
        e = lista[idx]
        print(f"  Nombre:               {e.name}")
        print(f"  Torneos ganados:      {e.tourneys}")
        print(f"  Batallas ganadas:     {e.wins}")
        print(f"  Batallas perdidas:    {e.losses}")
        print(f"  Porcentaje victorias: {e.win_rate:.2f}%")
        print(f"  Pokemons:")
        e.pokemons.show()

    # ========== e) >79% VICTORIAS ==========
    print("\n" + "=" * 70)
    print("e) ENTRENADORES CON >79% DE VICTORIAS")
    print("=" * 70)
    encontrado = False
    for e in lista:
        if e.win_rate > 79:
            print(f"  {e.name}: {e.win_rate:.2f}%")
            encontrado = True
    if not encontrado:
        print("  (ninguno)")

    # ========== f) TIPOS ESPECIFICOS ==========
    print("\n" + "=" * 70)
    print("f) ENTRENADORES CON POKEMONS DE TIPO/SUBTIPO ESPECIFICO")
    print("=" * 70)

    def buscar_por_tipo(tipo, subtipo):
        for e in lista:
            encontrados = [p.name for p in e.pokemons
                           if p.type_.lower() == tipo.lower()
                           and p.subtype.lower() == subtipo.lower()]
            if encontrados:
                print(f"  {e.name}: {', '.join(encontrados)}")

    print("\n  Con Fuego/Volador:")
    buscar_por_tipo("Fuego", "Volador")
    print("\n  Con Agua/Volador:")
    buscar_por_tipo("Agua", "Volador")

    # ========== g) PROMEDIO DE NIVEL ==========
    print("\n" + "=" * 70)
    print("g) PROMEDIO DE NIVEL DE POKEMONS")
    print("=" * 70)
    for nombre in ["Ash", "Gary", "Misty"]:
        idx = lista.search(nombre, 'name')
        if idx is not None:
            e = lista[idx]
            niveles = [p.level for p in e.pokemons]
            promedio = sum(niveles) / len(niveles) if niveles else 0
            print(f"  {e.name}: {promedio:.2f}")

    # ========== h) CUANTOS ENTRENADORES TIENEN UN POKEMON ==========
    print("\n" + "=" * 70)
    print("h) CUANTOS ENTRENADORES TIENEN UN POKEMON ESPECIFICO")
    print("=" * 70)
    for pokemon_buscado in ["Pikachu", "Charizard", "Onix", "Lapras"]:
        cantidad = sum(
            1 for e in lista
            if any(p.name.lower() == pokemon_buscado.lower() for p in e.pokemons)
        )
        print(f"  {pokemon_buscado}: {cantidad} entrenador(es)")

    # ========== i) POKEMONS REPETIDOS ==========
    print("\n" + "=" * 70)
    print("i) ENTRENADORES CON POKEMONS REPETIDOS")
    print("=" * 70)
    encontrado = False
    for e in lista:
        nombres = [p.name.lower() for p in e.pokemons]
        repetidos = [n for n in set(nombres) if nombres.count(n) > 1]
        if repetidos:
            print(f"  {e.name}: {', '.join(repetidos)}")
            encontrado = True
    if not encontrado:
        print("  (ninguno)")

    # ========== j) POKEMONS ESPECIFICOS ==========
    print("\n" + "=" * 70)
    print("j) ENTRENADORES CON TYRANTRUM, TERAKION O WINGULL")
    print("=" * 70)
    buscados = ["Tyrantrum", "Terakion", "Wingull"]
    encontrado = False
    for e in lista:
        hallados = [b for b in buscados
                    if any(p.name.lower() == b.lower() for p in e.pokemons)]
        if hallados:
            print(f"  {e.name}: {', '.join(hallados)}")
            encontrado = True
    if not encontrado:
        print("  (ninguno)")

    # ========== k) VERIFICAR ENTRENADOR-POKEMON ==========
    print("\n" + "=" * 70)
    print("k) VERIFICAR SI UN ENTRENADOR TIENE UN POKEMON")
    print("=" * 70)
    verificaciones = [
        ("Ash",    "Charizard"),
        ("Misty",  "Pikachu"),
        ("Gary",   "Tyrantrum"),
        ("Blaine", "Wingull"),
    ]
    for nombre_e, nombre_p in verificaciones:
        idx = lista.search(nombre_e, 'name')
        if idx is not None:
            e = lista[idx]
            tiene = any(p.name.lower() == nombre_p.lower() for p in e.pokemons)
            estado = "SI" if tiene else "NO"
            print(f"  {e.name} {estado} tiene a {nombre_p}")
            if tiene:
                print(f"    Pokemons totales: {e.pokemons.size()} | Victorias: {e.wins}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 80)
    print("                 TRABAJO PRACTICO 4: LISTAS (LIST_)")
    print("=" * 80)
    
    print("\n" + "#" * 80)
    print("#  EJERCICIO 6: LISTA DE SUPERHEROES")
    print("#" * 80)
    ejercicio_6()

    print("\n\n" + "#" * 80)
    print("#  EJERCICIO 15: ENTRENADORES Y POKEMON")
    print("#" * 80)
    ejercicio_15()

    print("\n\n" + "=" * 80)
    print("                 FIN DEL TRABAJO PRACTICO 4")
    print("=" * 80)


if __name__ == "__main__":
    main()
