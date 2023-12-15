from kps_peli import KPSPeli
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPSPeli):
    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)
        self.pelaajan_siirto = 'k'

    def palauta_pelaajan_1_siirto(self):
        self.pelaajan_siirto = input("Ensimmäisen pelaajan siirto: ")
        return self.pelaajan_siirto
    
    def palauta_pelaajan_2_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(self.pelaajan_siirto)
        return siirto
