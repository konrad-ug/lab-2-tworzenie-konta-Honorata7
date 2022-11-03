from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwaFirmy, nip):
        self.nazwaFirmy = nazwaFirmy
        self.nip = self.poprawny_nip(nip)
        self.saldo = 0
        self.oplata_za_przelew_ekspresowy = 5


    def poprawny_nip(self, nip):
        if len(nip) == 10:
            return nip
        else:
            return "Niepoprawny nip!"
