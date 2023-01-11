import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestHistoriaFirma(unittest.TestCase): 

    nazwaFirmy = "XYZ"
    nip = "1234567890"

    def testHistoria1(self):
        konto = KontoFirmowe(self.nazwaFirmy, self.nip)
        konto.zaksieguj_przelew_przychodzacy(1000)
        konto.zaksieguj_przelew_wychodzacy(500)
        konto.zaksieguj_przelew_przychodzacy(500)
        konto.zaksieguj_przelew_wychodzacy_ekspresowy(300)
        konto.zaksieguj_przelew_wychodzacy(300)
        konto.zaksieguj_przelew_przychodzacy(200)
        self.assertEqual(konto.historia, [1000, -500, 500, -300, -5, -300, 200], "Błąd")
