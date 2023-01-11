import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "12345678900")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")


    def test_krotki_pesel(self):
        krotki_pesel = Konto("Anna", "Nowak", "012345")
        self.assertEqual(krotki_pesel.pesel, "Niepoprawny pesel!", "Pesel jest za krótki")

    def test_dlugi_pesel(self):
        dlugi_pesel = Konto("Jan", "Kowalski", "01234567891234")
        self.assertEqual(dlugi_pesel.pesel, "Niepoprawny pesel!", "Pesel jest za dlugi")

    def test_urodzony_1800_0(self):
        urodzony_1800_0 = Konto("Jan", "Kowalski", "01934567890")
        self.assertEqual(urodzony_1800_0.rok_urodzenia(), 1801, "Niepoprawny pesel")

    def test_urodzony_1900_0(self):
        urodzony_1900_0 = Konto("Jan", "Kowalski", "01134567890")
        self.assertEqual(urodzony_1900_0.rok_urodzenia(), 1901, "Niepoprawny pesel")

    def test_urodzony_2100_0(self):
        urodzony_2100_0 = Konto("Jan", "Kowalski", "01534567890")
        self.assertEqual(urodzony_2100_0.rok_urodzenia(), 2101, "Niepoprawny pesel")

    def test_urodzony_1800_inne_niz_0(self):
        urodzony_1800_inne_niz_0 = Konto("Jan", "Kowalski", "11934567890")
        self.assertEqual(urodzony_1800_inne_niz_0.rok_urodzenia(), 1811, "Niepoprawny pesel")

    def test_urodzony_2100_inne_niz_0(self):
        urodzony_2100_inne_niz_0 = Konto("Jan", "Kowalski", "19534567890")
        self.assertEqual(urodzony_2100_inne_niz_0.rok_urodzenia(), 2109, "Niepoprawny pesel")


    def test_dobry_kod_rabatowy(self):
        konto_dobry_kod = Konto("Anna", "Nowak", "12345678900", "PROM_123")
        self.assertEqual(konto_dobry_kod.kod, "PROM_123", "")

    def test_zly_kod_rabatowy(self):
        konto_zly_kod = Konto("Ala", "Kot", "12345678900", "ABCD_123")
        self.assertEqual(konto_zly_kod.saldo, 0, "")

    def test_kod_mlodsi_niz_1960(self):
        konto_mlodsi_niz_1960 = Konto("Jan", "Kowalski", "01230111111", "PROM_123")
        self.assertEqual(konto_mlodsi_niz_1960.rok_urodzenia(), 2001, "Niepoprawny rok urodzenia")
        self.assertEqual(konto_mlodsi_niz_1960.urodzony_po_1960(), True, "Uzytkownik jest młodszy niz 1960")
        self.assertEqual(konto_mlodsi_niz_1960.saldo, 50, "Błąd, promocja powinna się naliczyć.")

    def test_kod_starsi_niz_1960(self):
        konto_starsi_niz_1960 = Konto("Jan", "Kowalski", "53030111111", "PROM_123")
        self.assertEqual(konto_starsi_niz_1960.rok_urodzenia(), 1903, "Niepoprawny rok urodzenia")
        self.assertEqual(konto_starsi_niz_1960.urodzony_po_1960(), False, "Uzytkownik jest starszy niz 1960")
        self.assertEqual(konto_starsi_niz_1960.saldo, 0, "Błąd, promocja nie powinna się naliczyć.")
