# ============================================================================
# CLASE Y DATOS DE CRIATURAS MITOLOGICAS
# ============================================================================

class Criatura:
    def __init__(self, nombre, derrotado_por=None, descripcion="", capturada=None):
        self.name = nombre
        self.killer = derrotado_por
        self.description = descripcion
        self.captured = capturada

    def __str__(self):
        derrotador = self.killer if self.killer else "Nadie (-)"
        capturador = self.captured if self.captured else "Nadie (-)"
        return f"{self.name:<25} | Derrotado por: {derrotador:<18} | Capturado por: {capturador:<12} | Desc: {self.description}"


Criaturas = [
    Criatura("Ceto",                 None,            "Monstruo marino primordial, madre de monstruos."),
    Criatura("Tifón",                "Zeus",          "Gigante monstruoso con cien cabezas de serpiente."),
    Criatura("Equidna",              "Argos Panoptes","Ninfa monstruosa, mitad mujer mitad serpiente."),
    Criatura("Dino",                 None,            "Una de las Greas, ancianas con un solo ojo y diente."),
    Criatura("Pefredo",              None,            "Una de las Greas, hermana de Dino y Enio."),
    Criatura("Enio",                 None,            "Una de las Greas, la 'destructora de ciudades'."),
    Criatura("Escila",               None,            "Monstruo marino con torso de mujer y colas de serpiente/perros."),
    Criatura("Caribdis",             None,            "Monstruo marino que crea devoradores remolinos."),
    Criatura("Euríale",              None,            "Gorgona inmortal con garras de bronce y cabellos de serpiente."),
    Criatura("Esteno",               None,            "La mas feroz de las tres hermanas Gorgonas."),
    Criatura("Medusa",               "Perseo",        "Gorgona mortal que convertia en piedra a quien la miraba."),
    Criatura("Ladón",                "Heracles",      "Dragon de cien cabezas que custodiaba las manzanas doradas."),
    Criatura("Águila del Cáucaso",   None,            "Ave gigante que devoraba el higado de Prometeo."),
    Criatura("Quimera",              "Belerofonte",   "Monstruo hibrido de leon, cabra y serpiente que escupia fuego."),
    Criatura("Hidra de Lerna",       "Heracles",      "Serpiente policefala acuatica cuyo aliento era venenoso."),
    Criatura("León de Nemea",        "Heracles",      "Leon de piel impenetrable derrotado en el primer trabajo."),
    Criatura("Esfinge",              "Edipo",         "Monstruo con rostro femenino, cuerpo de leon y alas de ave."),
    Criatura("Dragón de la Cólquida", None,           "Dragon insomne que custodiaba el Vellocino de Oro."),
    Criatura("Cerbero",              None,            "Perro de tres cabezas guardian del Inframundo."),
    Criatura("Cerda de Cromión",     "Teseo",         "Jabali gigante y salvaje que asolaba Cromion."),
    Criatura("Ortro",                "Heracles",      "Perro de dos cabezas hermano de Cerbero."),
    Criatura("Toro de Creta",        "Teseo",         "Toro salvaje de la mitologia cretense."),
    Criatura("Jabalí de Calidón",    "Atalanta",      "Enorme jabali enviado por Artemisa a asolar Calidon."),
    Criatura("Carcinos",             None,            "Cangrejo gigante enviado por Hera para ayudar a la Hidra."),
    Criatura("Gerión",               "Heracles",      "Gigante de tres cuerpos unidos por la cintura."),
    Criatura("Cloto",                None,            "Una de las tres Moiras, la que hila el hilo de la vida."),
    Criatura("Láquesis",             None,            "Una de las tres Moiras, la que mide la longitud de la vida."),
    Criatura("Átropos",              None,            "Una de las tres Moiras, la que corta el hilo de la vida."),
    Criatura("Minotauro de Creta",   "Teseo",         "Monstruo mitad hombre mitad toro atrapado en el Laberinto."),
    Criatura("Harpías",              None,            "Aves con rostro de mujer y garras afiladas."),
    Criatura("Argos Panoptes",       "Hermes",        "Gigante con cien ojos que nunca dormian al mismo tiempo."),
    Criatura("Aves del Estínfalo",   None,            "Aves con picos y plumas de bronce mortiferas."),
    Criatura("Talos",                "Medea",         "Gigante automata de bronce que custodiaba Creta."),
    Criatura("Sirenas",              None,            "Seres maritimos con voz seductora que atraian a marineros."),
    Criatura("Pitón",                "Apolo",         "Gran serpiente que habitaba en el centro de la Tierra."),
    Criatura("Cierva de Cerinea",    None,            "Cierva con cuernos de oro y pezunas de bronce."),
    Criatura("Basilisco",            None,            "Rey de las serpientes cuyo aliento mata las plantas."),
    Criatura("Jabalí de Erimanto",   None,            "Jabali gigante que asolaba las laderas del monte Erimanto."),
]
