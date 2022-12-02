class Konto:
    def __init__(self, imie, nazwisko, pesel, kod = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = self.poprawny_pesel(pesel)
        self.kod = kod
        self.saldo = self.promocja_poprawiona()
        self.oplata_za_przelew_ekspresowy = 1


    def poprawny_pesel(self, pesel):
        if len(pesel) == 11:
            return pesel
        else:
            return "Niepoprawny pesel!"

    def rok_urodzenia(self):
        pesel = self.pesel
        if pesel != "Niepoprawny pesel!":
            if int(pesel[0])==0:
                if int(pesel[2])== 8 or int(pesel[2]) == 9:
                    return 1800+int(pesel[1])
                if int(pesel[2])==0 or int(pesel[2]) == 1:
                    return 1900+int(pesel[1])
                if int(pesel[2])== 2 or int(pesel[2]) == 3:
                    return 2000+int(pesel[1])
                if int(pesel[2])== 4 or int(pesel[2]) == 5:
                    return 2100+int(pesel[1])
            elif 0<int(pesel[0]):
                if int(pesel[2])== 8 or int(pesel[2]) == 9:
                    return 1800+int(pesel[0:2])
                if int(pesel[2])== 0 or int(pesel[2]) == 1:
                    return 1900+int(pesel[1])
                if int(pesel[2])== 2 or int(pesel[2]) == 3:
                    return 2000+int(pesel[1])
                if int(pesel[2])== 4 or int(pesel[2]) == 5:
                    return 2100+int(pesel[1])

    def urodzony_po_1960(self):
        if self.rok_urodzenia != "Niepoprawny pesel!":
            return self.rok_urodzenia() > 1960

    def promocja_poprawiona(self):
        if self.kod != None and self.urodzony_po_1960():
            if len(self.kod) == 8 and self.kod[0:5] == "PROM_":
                return 50
        return 0

    def zaksieguj_przelew_przychodzacy(self, kwota_przelewu):
        self.saldo += kwota_przelewu

    def zaksieguj_przelew_wychodzacy(self, kwota_przelewu):
        if kwota_przelewu <= self.saldo:
            self.saldo -= kwota_przelewu

    def zaksieguj_przelew_wychodzacy_ekspresowy(self, kwota_przelewu):
        if kwota_przelewu <= self.saldo:
            self.saldo -= kwota_przelewu + self.oplata_za_przelew_ekspresowy

