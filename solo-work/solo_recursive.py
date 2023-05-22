# Stworzenie funkcji, która rekurencyjnie będzie sumować elementy listy:
# funkcja list_sum(lista):
#   is lista empty?
#       yes -> 0
#       no -> lista[0] + funkcja[reszta listy]

def list_sum(lista):
    if len(lista) == 0:
        return 0
    else:
        el1 = lista.pop(0)
        return el1+list_sum(lista)

lista1 = [3, 2, 3, 4]
#print(list_sum(lista1))

# Stworzenie funkcji, która oblicza rekurencyjnie silnię z podanej liczby:
# funkcja silnia(liczba):
#   is liczba > 0 ?
#       no -> błąd
#       yes -> is liczba > 1?
#           no -> 1
#           yes -> liczba * silnia(liczba-1)


def silnia(liczba):
    if liczba > 1:
        return (liczba * silnia(liczba-1))
    elif liczba < 0:
        return "Błędna wartość wejściowa"
    else:
        return 1

print(silnia(5))

# Stworzenie funkcji, która zwraca podany element ciągu Fibonacciego
# funkcja fib(liczba)
#   is liczba > 2 ?
#       yes -> fib(liczba-1) + fib(liczba-2)
#       no -> 1

def fib(liczba):
    if liczba > 2:
        return fib(liczba-1) + fib(liczba-2)
    elif liczba == 0:
        return 0
    else:
        return 1

#print(fib(7))