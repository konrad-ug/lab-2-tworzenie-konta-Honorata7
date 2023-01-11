import unittest
from ..KontoFirmowe import KontoFirmowe
from parameterized import parameterized

class TestKredytFirmowy(unittest.TestCase):
    nazwa = "Foxtry"
    nip = "1234567890"

    def setUp(self):
        self.konto_firmowe = KontoFirmowe(self.nazwa, self.nip)

    @parameterized.expand([
        ([1775, -1775, 3000, -1000], 2000, 500, True, 2500),
        ([1775, -1775, 3000, -1000], 2000, 1100, False, 2000),
        ([1000, -1000, 3000, -1000], 2000, 500, False, 2000),
        ([100, 300, -200], 2000, 1100, False, 2000)
    ])

    def testKredytFirmowy(self, historia, saldo, kwota_kredytu, oczekiwany_wynik, oczekiwane_saldo):
        self.konto_firmowe.saldo = saldo
        self.konto_firmowe.historia = historia
        czy_przyznany = self.konto_firmowe.zaciagnij_kredyt(kwota_kredytu)
        self.assertEqual(czy_przyznany, oczekiwany_wynik, "Kredyt nie został przyznany poprawnie!")
        self.assertEqual(self.konto_firmowe.saldo, oczekiwane_saldo, "Kredyt nie został przyznany poprawnie!")
