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
print(trojkat_rownoboczny.obwod())

trojkat2 = Trojkat(5, 4, 3, 5)
print(trojkat2.pole())


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
print(trapez_rownoramienny.obwod(), trapez_rownoramienny.pole())
