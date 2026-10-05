from list_ import List
from pokemon import ListaPokemon, Pokemon


class Entrenador:
    def __init__(self, nombre, torneos, batallas_perdidas, batallas_ganadas):
        self.name     = nombre
        self.tourneys = torneos
        self.losses   = batallas_perdidas
        self.wins     = batallas_ganadas
        self.pokemons = ListaPokemon()

    @property
    def win_rate(self):
        total = self.wins + self.losses
        return (self.wins / total) * 100 if total else 0

    def __str__(self):
        return f"{self.name} | Torneos: {self.tourneys} | Victorias: {self.win_rate:.1f}%"


def by_name(item):     return item.name
def by_tourneys(item): return item.tourneys
def by_wins(item):     return item.wins


class ListaEntrenadores(List):
    """List especializada para Entrenador, con criterios ya cargados"""
    def __init__(self):
        super().__init__()
        self.add_criterion('name',     by_name)
        self.add_criterion('tourneys', by_tourneys)
        self.add_criterion('wins',     by_wins)
