import unittest
from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejest(unittest.TestCase):

    imie = "Ala"
    nazwisko = "Kot"
    pesel = "22222222222"
    dane = {
         "imie": "Karolina",
         "saldo": 100
    }

    @classmethod
    def setUpClass(cls):
        konto = Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.dodaj_konto(konto)

    def test_dodawanie_konta(self):
        konto = Konto(self.imie, self.nazwisko, "02222222222")
        dodane_konto = RejestrKont.dodaj_konto(konto)
        self.assertEqual(dodane_konto, konto)
        self.assertEqual(RejestrKont.ile_kont(), 3, "Nieprawidłowa ilość kont")
        
    
    def test_2_wyszukiwanie_konta_ktore_istnieje(self):
        konto = Konto(self.imie, self.nazwisko, "01222222222")
        dodane_konto = RejestrKont.dodaj_konto(konto)
        self.assertEqual(dodane_konto, konto)
        wynik = RejestrKont.wyszukaj_konto_z_peselem("01222222222")
        self.assertEqual(wynik, konto)


    def test_wyszukiwanie_nieistniejacego_konta(self):
        wynik = RejestrKont.wyszukaj_konto_z_peselem("01234567890")
        self.assertEqual(wynik, None)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []