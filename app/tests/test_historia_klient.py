import unittest

from ..Konto import Konto

class TestHistoriaKlientPrywatny(unittest.TestCase): 

    imie = "Ala"
    nazwisko = "Kot"
    pesel = "22222222222"

    def testHistoria1(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(500)
        konto.zaksieguj_przelew_wychodzacy(200)
        konto.zaksieguj_przelew_wychodzacy_ekspresowy(150)
        self.assertEqual(konto.historia, [500, -200, -150, -1], "Błąd")
