
from sovelluslogiikka import Sovelluslogiikka
from abc import abstractmethod


class LaskuKomento:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._edellinen = None

    @abstractmethod
    def _tee_lasku(self, arvo):
        pass

    def suorita(self):
        try:
            self._edellinen = self._sovelluslogiikka.arvo()
            self._tee_lasku()
        except Exception:
            pass

    def kumoa(self):
        if (self._edellinen == None):
            return
        print(self._edellinen)
        self._sovelluslogiikka.aseta_arvo(self._edellinen)
        self._edellinen = None


class Summa(LaskuKomento):
    pass

    def _tee_lasku(self):
        arvo = int(self._root())
        self._sovelluslogiikka.plus(arvo)


class Erotus(LaskuKomento):
    pass

    def _tee_lasku(self):
        arvo = int(self._root())
        self._sovelluslogiikka.miinus(arvo)


class Nollaus(LaskuKomento):
    pass

    def _tee_lasku(self):
        self._sovelluslogiikka.nollaa()
