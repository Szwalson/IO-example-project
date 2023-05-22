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
print(list_sum(lista1))

# Stworzenie funkcji, która oblicza rekurencyjnie silnię z podanej liczby:
# funkcja silnia(liczba):
#   is liczba > 1
#       yes -> liczba*silnia(liczba-1)
#       no -> 1

def silnia(liczba):
    if liczba > 1:
        return (liczba * silnia(liczba-1))
    else:
        return 1

print(silnia(3))
