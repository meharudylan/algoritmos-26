from list_ import List


class Superheroe:
    """Representa un superheroe con sus datos basicos"""

    def __init__(self, nombre, anio, casa, bio):
        self.name  = nombre
        self.year  = anio
        self.house = casa
        self.bio   = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"


def by_name(item):  return item.name
def by_year(item):  return item.year
def by_house(item): return item.house


class ListaSuperheroes(List):
    """List especializada para Superheroe, con criterios ya cargados"""
    def __init__(self):
        super().__init__()
        self.add_criterion('name',  by_name)
        self.add_criterion('year',  by_year)
        self.add_criterion('house', by_house)
