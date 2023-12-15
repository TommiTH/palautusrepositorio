from kps_tekoaly import KPSPeliTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_peli import KPSPeli
from enum import Enum

class PeliMoodit(Enum):
    NULL = 0
    PVP = 1
    PVC = 2
    PVC_HARD = 3

class PeliTehdas:
    
    @staticmethod
    def anna_tekstia_vastaava_pelimoodi(text: str):
        if text.endswith("a"):
            return PeliMoodit.PVP
        if text.endswith("b"):
            return PeliMoodit.PVC
        if text.endswith("c"):
            return PeliMoodit.PVC_HARD
        return PeliMoodit.NULL
    
    @staticmethod
    def luo_peli_tekstista(str: str):
        moodi = PeliTehdas.anna_tekstia_vastaava_pelimoodi(str)
        return PeliTehdas.luo_peli_pelimoodista(moodi)
    
    @staticmethod
    def luo_peli_pelimoodista(peliMoodi: PeliMoodit):
        if (peliMoodi is PeliMoodit.NULL):
            return None
        if (peliMoodi is PeliMoodit.PVP):
            return KPSPeli()
        if (peliMoodi is PeliMoodit.PVC):
            return KPSPeliTekoaly()
        if (peliMoodi is PeliMoodit.PVC_HARD):
            return KPSParempiTekoaly()