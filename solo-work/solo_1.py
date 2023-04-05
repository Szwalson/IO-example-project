import math
import numpy

# Zadanie 1.1
# oczekiwany rezultat: Hello Wojtek
# wykorzystaj w princie zmienne hello i student

hello = "Hello"
student = "Wojtek"
print("{message} {name}".format(message=hello, name=student))

# Zadanie 1.2

student = input("Wpisz swoje imie: ")
print("Hello {name}".format(name=student))

# Zadanie 1.3
# policz liczbe studentow w tablicy studenci
# oczekiwany rezultat: Liczba studentow wynosi: 4

studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow = len(studenci)
print("Liczba studentow wynosi: {number}".format(number=liczba_studentow))

# Zadanie 1.4
# za pomoca petli i print przywitaj sie z kazdym studentem
# z tabeli studenci osobno
# oczekiwany rezultat:
# Hello Ania
# Hello Kasia
# Hello Piotr
# Hello Tomek

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for i in studenci:
    print("Hello {name}".format(name=i))

# Zadanie 1.5
# oczekiwany rezultat:
# Wynik wynosi: 81

liczba = 3
potega = 4
wynik = math.pow(liczba, potega)
print("Wynik wynosi: " + str(wynik))

# Zadanie 1.6
# policz ilosc nawiasow ( w danym ciagu znakow
# oczekiwany rezultat:
# Liczba nawiasow otwierajacych wynosi: 4

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# Zadanie 1.7
# posortuj alfabetycznie (od imienia) studentow
# oczekiwany rezultat:
# Anna Szczesny
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
print("Alfabetyczna lista studentow wynosi: ")
for student in numpy.sort(studenci):
    print(student)

# Zadanie 1.8
# posortuj alfabetycznie (od nazwiska) studentow
# oczekiwany rezultat:
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
# Anna Szczesny

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]


def sortowanie(lista_wejsciowa):
    lista_wejsciowa.sort(key=lambda x: x.split()[-1])
    return lista_wejsciowa


print("Alfabetyczna lista studentow wynosi: ")
for student in sortowanie(studenci):
    print(student)

# Zadanie 1.9
# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci_lastnames = []
for student in studenci:
    studenci_lastnames.append(student.split()[-1])
studenciN = [x for x in studenci_lastnames if x.startswith("N")]
liczba_n = len(studenciN)
print("Liczba studentow na N wynosi: " + str(liczba_n))

# Zadanie 1.10
# zmienne ponizej preprezentuja ulozenie punktow na wykresie,
# do zadania dolaczono takze rysunek pomocniczy
# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True
# oczekiwany rezultat:
# Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]


def weryfikacja_liniowosci(wykres):
    a1 = (wykres[1][1] - wykres[0][1]) / (wykres[1][0] - wykres[0][0])
    a2 = (wykres[2][1] - wykres[0][1]) / (wykres[2][0] - wykres[0][0])
    if a1 == a2:
        wynik = True
    else:
        wynik = False
    return wynik


wykres_1_funkcja_liniowa = weryfikacja_liniowosci(wykres_1)
wykres_2_funkcja_liniowa = weryfikacja_liniowosci(wykres_2)
wykres_3_funkcja_liniowa = weryfikacja_liniowosci(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")
