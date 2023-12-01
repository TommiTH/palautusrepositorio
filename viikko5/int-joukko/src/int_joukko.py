KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämän luokan refaktorointi on pahinta kidutusta mitä ihminen voi kokea
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti: int = KAPASITEETTI, kasvatuskoko: int = OLETUSKASVATUS):
        self._kapasiteetti = kapasiteetti
        self._kasvatuskoko = kasvatuskoko
        self._lukujono = self._luo_lista(self._kapasiteetti)
        self._alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self._alkioiden_lkm):
            if n == self._lukujono[i]:
                return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return
        self._lukujono[self._alkioiden_lkm] = n
        self._alkioiden_lkm += 1

        if self._alkioiden_lkm % len(self._lukujono) == 0:
            taulukko_old = self._lukujono
            self._lukujono = self._luo_lista(
                self._alkioiden_lkm + self._kasvatuskoko)
            self.kopioi_lista(taulukko_old, self._lukujono)

    def poista(self, n):
        kohta = -1
        for i in range(0, self._alkioiden_lkm):
            if n == self._lukujono[i]:
                kohta = i
                self._lukujono[kohta] = 0
                break

        if kohta >= 0:
            self._alkioiden_lkm = self._alkioiden_lkm - 1
            for i in range(kohta, self._alkioiden_lkm):
                self._lukujono[i] = self._lukujono[i + 1]

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self._alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self._alkioiden_lkm)
        for i in range(0, len(taulu)):
            taulu[i] = self._lukujono[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])
        return z

    def __str__(self):
        palautus_str = ""
        for i in range(0, self._alkioiden_lkm):
            palautus_str += str(self._lukujono[i])
            if (i < self._alkioiden_lkm - 1): 
                palautus_str += ", "
        return "{" + palautus_str + "}"
