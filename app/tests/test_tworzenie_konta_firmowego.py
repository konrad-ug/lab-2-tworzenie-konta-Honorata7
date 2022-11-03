import unittest

from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta_firmowego(self):
        nowe_konto = KontoFirmowe("XYZ", "1234567890")
        self.assertEqual(nowe_konto.nazwaFirmy, "XYZ", "Nazwa Firmy nie została zapisana!")
        self.assertEqual(nowe_konto.nip, "1234567890", "Nip firmy nie został zapisany!")
        self.assertEqual(nowe_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_krotki_nip(self):
        konto_krotki_nip = KontoFirmowe("XYZ", "123456789")
        self.assertEqual(konto_krotki_nip.nip, "Niepoprawny nip!", "Nip jest za krótki!")

    def test_dlugi_nip(self):
        konto_dlugi_nip = KontoFirmowe("XYZ", "1234567812345678")
        self.assertEqual(konto_dlugi_nip.nip, "Niepoprawny nip!", "Nip jest za długi!")