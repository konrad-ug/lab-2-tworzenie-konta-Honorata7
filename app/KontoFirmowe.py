from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwaFirmy, nip):
        self.nazwaFirmy = nazwaFirmy
        self.nip = self.poprawny_nip(nip)
        self.saldo = 0
        self.oplata_za_przelew_ekspresowy = 5
        self.historia = []

    def poprawny_nip(self, nip):
        if len(nip) == 10:
            return nip
        else:
            return "Niepoprawny nip!"

    def zaciagnij_kredyt(self, kwota_kredytu):
        if self.saldo > 2* kwota_kredytu and -1775 in self.historia:
            self.saldo += kwota_kredytu
            return True
        return False

