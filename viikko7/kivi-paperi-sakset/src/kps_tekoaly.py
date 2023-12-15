from tekoaly import Tekoaly
from kps_peli import KPSPeli

class KPSPeliTekoaly(KPSPeli):
    def __init__(self):
        super().__init__()
        self.tekoaly = Tekoaly()

    def palauta_pelaajan_2_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
