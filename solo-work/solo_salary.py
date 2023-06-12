from tabulate import tabulate
import pandas as pd


class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.wynagrodzenie_brutto}"

    # Funkcje wyliczające koszty pracownika i pracodawcy oraz wynagrodzenie netto
    # w oparciu o informacje z https://www.biznes.gov.pl/pl/portal/0083
    # Funkcje zawierają możliwość podania informacji o tym, czy pracownik dojeżdża do pracy
    # i czy odprowadza składki do PPK (wartości 'tak'/'nie')

    def oblicz_koszty_pracownicze(self, dojazd, ppk):
        emerytalna = self.wynagrodzenie_brutto * 0.0976
        rentowa = self.wynagrodzenie_brutto * 0.015
        chorobowa = self.wynagrodzenie_brutto * 0.0245
        zdrowotna = (self.wynagrodzenie_brutto - emerytalna - rentowa - chorobowa) * 0.09
        if ppk == "tak":
            ppk = self.wynagrodzenie_brutto * 0.02
        else:
            ppk = 0
        if dojazd == "tak":
            dochod = (self.wynagrodzenie_brutto - emerytalna - rentowa - chorobowa) - 300
        else:
            dochod = (self.wynagrodzenie_brutto - emerytalna - rentowa - chorobowa) - 250
        zaliczka_na_podatek = (dochod * 0.12) - 300
        return round(emerytalna, 2), round(rentowa, 2), round(chorobowa, 2), round(zdrowotna, 2), round(
            zaliczka_na_podatek, 2), round(ppk, 2)

    def oblicz_koszty_pracodawcy(self, ppk):
        emerytalna = self.wynagrodzenie_brutto * 0.0976
        rentowa = self.wynagrodzenie_brutto * 0.065
        wypadkowa = self.wynagrodzenie_brutto * 0.0167
        fundusz_pracy = self.wynagrodzenie_brutto * 0.0245
        fundusz_fgsp = self.wynagrodzenie_brutto * 0.001
        if ppk == "tak":
            ppk = self.wynagrodzenie_brutto * 0.015
        else:
            ppk = 0
        return round(emerytalna, 2), round(rentowa, 2), round(wypadkowa, 2), round(fundusz_pracy, 2), round(
            fundusz_fgsp, 2), round(ppk, 2)

    def oblicz_netto(self, dojazd, ppk):
        emerytalna, rentowa, chorobowa, zdrowotna, zaliczka, ppk = self.oblicz_koszty_pracownicze(dojazd, ppk)
        return self.wynagrodzenie_brutto - emerytalna - rentowa - chorobowa - zdrowotna - zaliczka - ppk


# Pobranie listy pracowników z pliku .csv na dysku (wartości oddzielone średnikami)

pracownicy_csv = pd.read_csv(r'C:\Users\layvi\Desktop\Projekty_IO\pracownicy.csv', sep=';')

# Utworzenie tabeli, w której wyświetlone zostaną wyniki obliczeń w pętli dla każdego pracownika

tabela = [["Nazwisko", "Płaca brutto", "Płaca netto", "Koszty pracownicze (suma)", "Koszty pracodawcy (suma)"]]

# W pętli dla każdego wiersza DataFrame importowanego z pliku .csv użytkownik pytany jest o to, czy dany pracownik
# dojeżdża do pracy i czy odprowadza składki do PPK. W zależności od tego wywoływane są zadeklarowane
# dla klasy Pracownik funkcje, a obliczenia są dodawane i ostatecznie wyświetlane w wyprintowanej tabeli.

for _, row in pracownicy_csv.iterrows():
    pracownik = Pracownik(row["imie"], row["nazwisko"], row["wynagrodzenie_brutto"])
    print("Czy pracownik " + pracownik.imie + " " + pracownik.nazwisko + " dojeżdża do pracy?")
    dojazd_input = input()
    print("Czy pracownik odprowadza składki do PPK?")
    ppk_input = input()
    placa_netto = pracownik.oblicz_netto(dojazd_input, ppk_input)
    koszty_pracownicze = sum(pracownik.oblicz_koszty_pracownicze(dojazd_input, ppk_input))
    koszty_pracodawcy = sum(pracownik.oblicz_koszty_pracodawcy(ppk_input))
    tabela.append(
        [pracownik.nazwisko, pracownik.wynagrodzenie_brutto, placa_netto, koszty_pracownicze, koszty_pracodawcy])

print(tabulate(tabela, headers="firstrow"))
