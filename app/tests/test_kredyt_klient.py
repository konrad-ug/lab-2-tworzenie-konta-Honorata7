import unittest
from parameterized import parameterized

from ..Konto import Konto


class TestKredytKlientPrywatny(unittest.TestCase): 

    imie = "Ala"
    nazwisko = "Kot"
    pesel = "22222222222"


    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([-100, 100, 100, 100, 600], 400, True, 400),
        ([100, 100, 300, 250, -100, 300], 200, False, 0),
        ([100, -100, -200, 200, 500, 300], 100, True, 100),
        ([100, 300, 400], 200, False, 0),
        ([100, 100, 200, -100, -50, -60], 150, False, 0)
    ])

    def testKredyt(self, historia, kwota_kredytu, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota_kredytu)
        self.assertEqual(czy_przyznany, oczekiwany_wynik, kwota_kredytu)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo, "Kredyt nie został przyznany poprawnie!")