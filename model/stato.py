from dataclasses import dataclass


@dataclass
class Stato:
    _nome: str
    _abbreviazione: str
    _codice: int

    def __hash__(self):
        return hash(self._codice)

    def __str__(self):
        return f"{self._nome} ({self._abbreviazione})"
    @property
    def nome(self):
        return self._nome

    @property
    def abbreviazione(self):
        return self._abbreviazione

    @property
    def codice(self):
        return self._codice
