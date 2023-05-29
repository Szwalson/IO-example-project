class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.wynagrodzenie_brutto}"

    def oblicz_koszty_pracownicze(self, dojazd):
        emerytalna = self.wynagrodzenie_brutto*0.0976
        rentowa = self.wynagrodzenie_brutto*0.015
        chorobowa = self.wynagrodzenie_brutto*0.0245
        zdrowotna = (self.wynagrodzenie_brutto-emerytalna-rentowa-chorobowa)*0.09
        if dojazd == "tak":
            dochod = (self.wynagrodzenie_brutto-emerytalna-rentowa-chorobowa)-300
        else:
            dochod = (self.wynagrodzenie_brutto - emerytalna - rentowa - chorobowa)-250
        zaliczka_na_podatek = (dochod*0.12)-300
        return round(emerytalna,2), round(rentowa,2), round(chorobowa,2), round(zdrowotna,2), round(zaliczka_na_podatek,2)

    def oblicz_koszty_pracodawcy(self):
        emerytalna = self.wynagrodzenie_brutto*0.0976
        rentowa = self.wynagrodzenie_brutto*0.065
        wypadkowa = self.wynagrodzenie_brutto*0.0167
        fundusz_pracy = self.wynagrodzenie_brutto*0.0245
        fundusz_fgsp = self.wynagrodzenie_brutto*0.001
        return round(emerytalna,2), round(rentowa,2), round(wypadkowa,2), round(fundusz_pracy,2), round(fundusz_fgsp,2)

    def oblicz_netto(self):
        print("Czy pracownik dojeżdża do pracy?")
        emerytalna, rentowa, chorobowa, zdrowotna, zaliczka = self.oblicz_koszty_pracownicze(dojazd=input())
        return self.wynagrodzenie_brutto -emerytalna-rentowa-chorobowa-zdrowotna-zaliczka


pracownik1 = Pracownik("Wojciech", "Szwałek", 3600)
#print(pracownik1.oblicz_koszty_pracownicze("tak"))
print(pracownik1.oblicz_netto())
#for pracownik in pracownicy:
   # print("Pracownik Kowalski: ")
  #  print("- pensja brutto: ")
   # print("- pensja netto: ")
    #print("- koszty pracowdawcy: ")
    #print("- koszt całkowity: ")