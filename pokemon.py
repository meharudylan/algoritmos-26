from list_ import List


class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.name    = nombre
        self.level   = nivel
        self.type_   = tipo
        self.subtype = subtipo

    def __str__(self):
        return f"{self.name} (Nivel {self.level}) - {self.type_}/{self.subtype}"


def by_name(item):  return item.name
def by_level(item): return item.level


class ListaPokemon(List):
    """List especializada para Pokemon, con criterios ya cargados"""
    def __init__(self):
        super().__init__()
        self.add_criterion('name',  by_name)
        self.add_criterion('level', by_level)
