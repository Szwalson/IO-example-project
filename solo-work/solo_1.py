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
