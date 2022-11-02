import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestKsiegowaniePrzelewowKlientPrywatny(unittest.TestCase): 

    imie = "Ala"
    nazwisko = "Kot"
    pesel = "22222222222"
    nazwaFirmy = "XYZ"

    def test_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500 
        konto.zaksieguj_przelew_przychodzacy(400)
        self.assertEqual(konto.saldo, 500+400, "Błąd!")

    def test_przelew_wychodzacy_wystarczajace_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 500-100, "Błąd!")

    def test_przelew_wychodzacy_niewystarczajace_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(600)
        self.assertEqual(konto.saldo, 500, "Błąd! Zbyt mało środków na koncie, aby wykonać przelew.")

    def test_seria_przelewow(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_przychodzacy(200)
        konto.zaksieguj_przelew_przychodzacy(200)
        konto.zaksieguj_przelew_wychodzacy(600)
        self.assertEqual(konto.saldo, 300, "Błąd! Zbyt mało środków na koncie, aby wykonać przelew.")

    def test_przelew_ekspresowy_wystarczajace_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy_ekspresowy(400)
        self.assertEqual(konto.saldo, 500-(400+1), "Błąd!")

    def test_przelew_ekspresowy_ponizej_0(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy_ekspresowy(500)
        self.assertEqual(konto.saldo, 500-500-1, "Błąd!")

    def test_przelew_ekspresowy_niewystarczajace_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy_ekspresowy(800)
        self.assertEqual(konto.saldo, 500, "Błąd! Zbyt mało środków na koncie, aby wykonać przelew.")
