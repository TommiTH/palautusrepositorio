from tuomari import Tuomari


class KPSPeli:
    def __init__(self):
        self.tuomari = Tuomari()

    def pelaa(self):
        while True:
            ekan_siirto = self.palauta_pelaajan_1_siirto()
            tokan_siirto = self.palauta_pelaajan_2_siirto()

            if (not self._ovatko_siirrot_ok(ekan_siirto, tokan_siirto)):
                break

            self.kirjaa_pisteet(ekan_siirto, tokan_siirto)
            self.printtaa_pisteet()

        self.lopeta()

    def palauta_pelaajan_1_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def palauta_pelaajan_2_siirto(self):
        return input("Toisen pelaajan siirto: ")

    def lopeta(self):
        print("Kiitos!")
        self.printtaa_pisteet()

    def printtaa_pisteet(self):
        print(self.tuomari)

    def kirjaa_pisteet(self, ekan_siirto, tokan_siirto):
        self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)

    def _ovatko_siirrot_ok(self, siirto1, siirto2):
        return self._onko_ok_siirto(siirto1) and self._onko_ok_siirto(siirto2)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
