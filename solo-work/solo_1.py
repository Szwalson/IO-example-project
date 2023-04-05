# zadanie 1.1

hello = "Hello"
student = "Wojtek"

# oczekiwany rezultat: Hello Wojtek
# wykorzystaj w princie zmienne hello i student

print("{message} {name}".format(message=hello, name=student))


# zadanie 1.2

student = input("Wpisz swoje imie: ")

print("Hello {name}".format(name=student))


# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

# policz liczbe studentow w tablicy studenci
# oczekiwany rezultat: Liczba studentow wynosi: 4
liczba_studentow = len(studenci)
print("Liczba studentow wynosi: {number}".format(number=liczba_studentow))


# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

# za pomoca petli i print przywitaj sie z kazdym studentem
# z tabeli studenci osobno
# oczekiwany rezultat:
# Hello Ania
# Hello Kasia
# Hello Piotr
# Hello Tomek
for i in studenci:
    print("Hello {name}".format(name=i))


# zadanie 1.5

import math

liczba = 3
potega = 4

wynik = math.pow(liczba, potega)

# oczekiwany rezultat:
# Wynik wynosi: 81
print("Wynik wynosi: "+str(wynik))


# zadanie 1.6

# policz ilosc nawiasow ( w danym ciagu znakow

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

# oczekiwany rezultat:
# Liczba nawiasow otwierajacych wynosi: 4
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))


# zadanie 1.7

import numpy

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

# oczekiwany rezultat:
# Anna Szczesny
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
print("Alfabetyczna lista studentow wynosi: ")
for student in numpy.sort(studenci):
    print(student)


# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

def sortowanie(lista_wejsciowa):
    lista_wejsciowa.sort(key=lambda x: x.split()[-1])
    return lista_wejsciowa

# oczekiwany rezultat:
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
# Anna Szczesny
print("Alfabetyczna lista studentow wynosi: ")
for student in sortowanie(studenci):
    print(student)


# zadanie 1.9

# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci_lastnames = []
for student in studenci:
    studenci_lastnames.append(student.split()[-1])

studenciN = [x for x in studenci_lastnames if x.startswith("N")]

liczba_n = len(studenciN)
print("Liczba studentow na N wynosi: "+str(liczba_n))


# zadanie 1.10

# zmienne poniezej preprezentuja ulozenie punktow na wykresie,
# do zadania dolaczono takze rysunek pomocniczy
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

def weryfikacja_liniowosci(wykres):
    a1 = (wykres[1][1]-wykres[0][1])/(wykres[1][0]-wykres[0][0])
    a2 = (wykres[2][1]-wykres[0][1])/(wykres[2][0]-wykres[0][0])

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

# oczekiwany rezultat:
# Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.