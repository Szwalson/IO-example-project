# zadanie 1.1

hello = "Hello"
student = "Wojtek"

# oczekiwany rezultat: Hello Wojtek
# wykorzystaj w princie zmienne hello i student

print("{message} {name}".format(message=hello, name=student))


# zadanie 1.2

student = input("Wpisz swoje imię: ")

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
