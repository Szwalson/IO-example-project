class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a

    def obwod(self):
        return self.a + self.b + self.c

    def pole(self):
        return self.a * self.h_a / 2


trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
#print(trojkat_rownoboczny.obwod())

trojkat2 = Trojkat(5, 4, 3, 5)
#print(trojkat2.pole())


class Trapez:
    def __init__(self, a, b, c, d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h

    def obwod(self):
        return self.a + self.b + self.c + self.d

    def pole(self):
        return (self.a + self.b) * self.h / 2


trapez_rownoramienny = Trapez(10, 8, 6, 6, 5)
#print(trapez_rownoramienny.obwod(), trapez_rownoramienny.pole())


class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"

    def __int__(self):
        return 10

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny)/len(self.oceny)

student_wojtek = Student("Wojciech", "Szwałek", 120135)
#print(student_wojtek)
#print(int(student_wojtek))

student_wojtek.dodaj_ocene(5)
student_wojtek.dodaj_ocene(4)
#print(student_wojtek.oceny)
#print(student_wojtek.zwroc_srednia())


class Wynik_biegu:
    def __init__(self, lokalizacja, dystans, przewyzszenie, uczestnik, czas_minuty, data, godzina_startu, limit_czasu_minuty):
        self.lokalizacja = lokalizacja
        self.dystans = dystans
        self.przewyzszenie = przewyzszenie
        self.uczestnik = uczestnik
        self.czas_minuty = czas_minuty
        self.data = data
        self.godzina_startu = godzina_startu
        self.limit_czasu_minuty = limit_czasu_minuty

    def __str__(self):
        return f"Uczestnik: {self.uczestnik} \n" \
               f"Dystans: {self.dystans} km \n" \
               f"Czas: {self.czas_minuty} min"

    def sr_tempo(self):
        sr_tempo = round(self.czas_minuty/self.dystans, 2)
        return f"Średnie tempo: \n" \
               f"{sr_tempo} min/km"

    def miedzyczasy(self):
        kilometr = round(self.czas_minuty/self.dystans)
        czas1 = kilometr*5
        czas2 = kilometr*10
        czas3 = kilometr*15
        return f"Międzyczasy: \n" \
               f"5km - {czas1} min\n" \
               f"10km - {czas2} min\n" \
               f"15km - {czas3} min"

wynik1 = Wynik_biegu("Poznań", 21.097, 500, "Wojciech Szwałek", 144, "16.04.2023r.", "10:00", 180)

print(wynik1)
print(wynik1.sr_tempo())
print(wynik1.miedzyczasy())
