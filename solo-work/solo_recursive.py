# Stworzenie funkcji, która rekurencyjnie będzie sumować elementy listy:
# Zakładam, że wszystkie elementy listy są typu liczbowego.
#
# funkcja list_sum(lista):
#   is lista empty?
#       yes -> 0
#       no -> lista[0] + funkcja[reszta listy]

def list_sum(lista):
    if len(lista) == 0:
        return 0
    else:
        el1 = lista.pop(0)
        return el1 + list_sum(lista)


lista1 = [3, 2, 3, 4]
print(list_sum(lista1))


# Stworzenie funkcji, która oblicza rekurencyjnie silnię z podanej liczby:
# Zakładam, że do funkcji zostanie podana całkowita liczba nieujemna.
#
# funkcja silnia(liczba):
#   is liczba > 0 ?
#       no -> błąd
#       yes -> is liczba > 1?
#           no -> 1
#           yes -> liczba * silnia(liczba-1)

def silnia(liczba):
    if liczba > 1:
        return (liczba * silnia(liczba - 1))
    elif liczba < 0:
        return "Błędna wartość wejściowa"
    else:
        return 1


print(silnia(5))


# Stworzenie funkcji, która zwraca podany element ciągu Fibonacciego:
# Zakładam, że nie zostanie podana do funkcji liczba ujemna.
#
# funkcja fib(liczba):
#   is liczba > 2 ?
#       yes -> fib(liczba-1) + fib(liczba-2)
#       no -> is liczba = 0?
#           yes -> return 0
#           no -> return 1

def fib(liczba):
    if liczba > 2:
        return fib(liczba - 1) + fib(liczba - 2)
    elif liczba == 0:
        return 0
    else:
        return 1


print(fib(7))


# Stworzenie funkcji, która znajdzie największy element z listy:
# Zakładam, że wszystkie elementy listy są typu liczbowego.
#
# funkcja find_max(lista):
#   is lista empty?
#       yes -> return "błąd"
#       no -> does lenght of lista equal 1?
#           yes -> return lista[0]
#           no -> is lista[0] > lista[1]?
#               yes -> lista.pop(1) and find_max(lista)
#               no -> lista.pop(0) and find_max(lista)

def find_max(lista):
    if len(lista) == 0:
        return "Lista jest pusta."
    elif len(lista) == 1:
        return lista[0]
    else:
        if lista[0] > lista[1]:
            lista.pop(1)
            return find_max(lista)
        else:
            lista.pop(0)
            return find_max(lista)


lista2 = [120, 4, 6, 1]
print(find_max(lista2))
