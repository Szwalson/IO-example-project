import math

# kwadrat
a = 10
obwod1 = a * 4
pole1 = a ** 2
print('Obwód kwadratu wynosi ' + str(obwod1) + ', a pole wynosi ' + str(pole1) + '.')

# prostokąt

a = 10
b = 5

obwod2 = 2*a+2*b
pole2 = a*b
print('Obwód prostokąta wynosi ' + str(obwod2) + ', a pole wynosi ' + str(pole2) + '.')

# trapez

a = 10
b = 20
c = d = 5
h = 8

obwod3 = a+b+c+d
pole3 = ((a+b)*h)/2
print('Obwód trapezu wynosi ' + str(obwod3) + ', a pole wynosi ' + str(pole3) + '.')

# koło

r = 5
pi = math.pi
obwod4 = 2*pi*r
pole4 = pi*(r**2)
print('Obwód okręgu wynosi ' + str(obwod4) + ', a pole koła wynosi ' + str(pole4) + '.')

# trójkąt równoramienny

a = 7
b = c = 10
h = 6

obwod5 = a+b+c
pole5 = a*h/2
print('Obwód trójkąta wynosi ' + str(obwod5) + ', a pole wynosi ' + str(pole5) + '.')