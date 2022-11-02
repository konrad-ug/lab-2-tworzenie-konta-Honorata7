import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestKsiegowaniePrzelewowKlientPrywatny(unittest.TestCase): 

    nazwaFirmy = "XYZ"
    nip = "1234567890"

    def test_przelew_przychodzacy(self):
        konto = KontoFirmowe(self.nazwaFirmy, self.nip)
        konto.saldo = 500 
        konto.zaksieguj_przelew_przychodzacy(400)
        self.assertEqual(konto.saldo, 500+400, "Błąd!")

    def test_przelew_wychodzacy_wystarczajace_srodki(self):
        konto = KontoFirmowe(self.nazwaFirmy, self.nip)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 500-100, "Błąd!")

    def test_przelew_wychodzacy_niewystarczajace_srodki(self):
        konto = KontoFirmowe(self.nazwaFirmy, self.nip)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(600)
        self.assertEqual(konto.saldo, 500, "Błąd! Zbyt mało środków na koncie, aby wykonać przelew.")

    def test_seria_przelewow(self):
        konto = KontoFirmowe(self.nazwaFirmy, self.nip)
        konto.saldo = 500
        konto.zaksieguj_przelew_przychodzacy(200)
        konto.zaksieguj_przelew_przychodzacy(200)
        konto.zaksieguj_przelew_wychodzacy(600)
        self.assertEqual(konto.saldo, 300, "Błąd! Zbyt mało środków na koncie, aby wykonać przelew.")

    def test_przelew_ekspresowy_wystarczajace_srodki(self):
        konto = KontoFirmowe(self.nazwaFirmy, self.nip)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy_ekspresowy(400)
        self.assertEqual(konto.saldo, 500-(400+1), "Błąd!")

    def test_przelew_ekspresowy_ponizej_0(self):
        konto = KontoFirmowe(self.nazwaFirmy, self.nip)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy_ekspresowy(500)
        self.assertEqual(konto.saldo, 500-500-1, "Błąd!")

    def test_przelew_ekspresowy_niewystarczajace_srodki(self):
        konto = KontoFirmowe(self.nazwaFirmy, self.nip)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy_ekspresowy(800)
        self.assertEqual(konto.saldo, 500, "Błąd! Zbyt mało środków na koncie, aby wykonać przelew.")
