from collections import deque
# ══════════════════════════════════════════════════════════════
#  EJERCICIO 10 — Cola de notificaciones de redes sociales
#  Cada notificacion: (hora, aplicacion, mensaje)
# ══════════════════════════════════════════════════════════════

def eliminar_facebook(cola):
    # a. Elimina todas las notificaciones de Facebook de la cola
    aux = deque()
    eliminadas = 0
    while len(cola) > 0:
        notif = cola.popleft()
        hora, app, mensaje = notif
        if app == "Facebook":
            eliminadas += 1
        else:
            aux.append(notif)
    for notif in aux:
        cola.append(notif)
    return eliminadas


def mostrar_twitter_python(cola):
    # b. Muestra notificaciones de Twitter con la palabra Python
    #    sin perder datos de la cola
    aux = deque()
    encontradas = []
    while len(cola) > 0:
        notif = cola.popleft()
        hora, app, mensaje = notif
        if app == "Twitter" and "Python" in mensaje:
            encontradas.append(notif)
        aux.append(notif)
    for notif in aux:
        cola.append(notif)
    return encontradas


def notificaciones_en_rango(cola, hora_inicio, hora_fin):
    # c. Guarda en una pila las notificaciones entre hora_inicio y hora_fin
    #    sin perder datos de la cola
    aux  = deque()
    pila = []
    while len(cola) > 0:
        notif = cola.popleft()
        hora, app, mensaje = notif
        if hora >= hora_inicio and hora <= hora_fin:
            pila.append(notif)
        aux.append(notif)
    # restauramos la cola
    for notif in aux:
        cola.append(notif)
    return pila


def ejercicio_10():
    cola_notif = deque([
        ("10:15", "Facebook",  "Maria te etiqueto en una foto"),
        ("10:42", "Twitter",   "Nuevo seguidor: @pythonista"),
        ("11:00", "Instagram", "Pedro le dio like a tu publicacion"),
        ("11:20", "Facebook",  "Juan comento tu publicacion"),
        ("11:43", "Twitter",   "Aprende Python con este hilo increible"),
        ("12:05", "WhatsApp",  "Mensaje de grupo: Reunion manana"),
        ("12:30", "Facebook",  "Tienes 3 nuevas solicitudes de amistad"),
        ("13:10", "Twitter",   "Python 3.13 ya esta disponible"),
        ("14:00", "Instagram", "Tu historia fue vista por 50 personas"),
        ("14:55", "Twitter",   "Curso gratis de Python este fin de semana"),
        ("15:20", "Facebook",  "Recuerdo de hace 3 anos"),
        ("15:57", "Twitter",   "Hilo sobre Python y estructuras de datos"),
        ("16:10", "WhatsApp",  "Llamada perdida de Ana"),
        ("16:45", "Facebook",  "Evento cercano: Meetup de tecnologia"),
    ])

    # b. Twitter + Python (antes del a para no perder datos de Facebook)
    print("b) Notificaciones de Twitter con la palabra Python:")
    resultados = mostrar_twitter_python(cola_notif)
    if len(resultados) > 0:
        for hora, app, mensaje in resultados:
            print(hora, "-", mensaje)
    else:
        print("No se encontraron notificaciones.")

    # c. Pila entre 11:43 y 15:57
    print("\nc) Notificaciones entre 11:43 y 15:57 (guardadas en pila):")
    pila = notificaciones_en_rango(cola_notif, "11:43", "15:57")
    for hora, app, mensaje in pila:
        print(hora, "-", app, "-", mensaje)
    print("Total de notificaciones en la pila:", len(pila))

    # a. Eliminar Facebook
    print("\na) Eliminando notificaciones de Facebook...")
    cant = eliminar_facebook(cola_notif)
    print("Se eliminaron", cant, "notificaciones de Facebook.")
    print("\nCola resultante:")
    for hora, app, mensaje in cola_notif:
        print(hora, "-", app, "-", mensaje)



# ══════════════════════════════════════════════════════════════
#  EJERCICIO 22 — Cola MCU (Marvel Cinematic Universe)
#  Cada personaje: (nombre_personaje, superheroe, genero)
# ══════════════════════════════════════════════════════════════

def ejercicio_22():
    cola_mcu = deque([
        ("Tony Stark",       "Iron Man",        "M"),
        ("Steve Rogers",     "Capitan America", "M"),
        ("Natasha Romanoff", "Black Widow",     "F"),
        ("Thor Odinson",     "Thor",            "M"),
        ("Bruce Banner",     "Hulk",            "M"),
        ("Carol Danvers",    "Capitana Marvel", "F"),
        ("Wanda Maximoff",   "Scarlet Witch",   "F"),
        ("Scott Lang",       "Ant-Man",         "M"),
        ("Sam Wilson",       "Falcon",          "M"),
        ("Shuri",            "Black Panther",   "F"),
        ("Peter Parker",     "Spider-Man",      "M"),
        ("Stephen Strange",  "Doctor Strange",  "M"),
    ])

    # a. Nombre del personaje de la superheroe "Capitana Marvel"
    print("a) Personaje cuyo superheroe es Capitana Marvel:")
    for nombre, superheroe, genero in cola_mcu:
        if superheroe == "Capitana Marvel":
            print(nombre)
            break

    # b. Nombres de los superheroes femeninos
    print("\nb) Superheroes femeninos:")
    for nombre, superheroe, genero in cola_mcu:
        if genero == "F":
            print(superheroe)

    # c. Nombres de los personajes masculinos
    print("\nc) Personajes masculinos:")
    for nombre, superheroe, genero in cola_mcu:
        if genero == "M":
            print(nombre)

    # d. Superheroe del personaje "Scott Lang"
    print("\nd) Superheroe de Scott Lang:")
    for nombre, superheroe, genero in cola_mcu:
        if nombre == "Scott Lang":
            print(superheroe)
            break

    # e. Todos los datos de personajes/superheroes que empiezan con S
    print("\ne) Personajes o superheroes cuyo nombre empieza con S:")
    for nombre, superheroe, genero in cola_mcu:
        if nombre[0] == "S" or superheroe[0] == "S":
            print(nombre, "|", superheroe, "|", genero)

    # f. Determinar si "Carol Danvers" esta en la cola
    print("\nf) Carol Danvers esta en la cola?")
    encontrado = False
    for nombre, superheroe, genero in cola_mcu:
        if nombre == "Carol Danvers":
            encontrado = True
            print("Si esta. Su superheroe es:", superheroe)
            break
    if not encontrado:
        print("No se encontro a Carol Danvers en la cola.")


