#cwiczenie 1
#a)
suma = 0
i = 0
for i in range (0, 101, 2):
    suma = suma+i
    if i == 100:
        print(suma)
#b)
parzyste = 0
nieparzyste = 0

for i in range (5):
    liczba = int(input(f"Podaj liczbe {i+1}: "))
    if liczba % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f"Ilość liczb parzystych to: {parzyste}")
print(f"Ilość liczb nieparzystych to: {nieparzyste}")

#c)

sumakw = 0
for i in range (0, 100, 1):
    sumakw = sumakw + i**2
print(sumakw)

#d)

sumapt = 0
for i in range (1, 63, 1):
    sumapt = sumapt + 2**i
print(sumapt)

#e)

suma_nieparz = 0
a = int(input("Podaj wartość a: "))
b = int(input("Podaj wartość b: "))
for i in range(a, b+1):
    if i%2:
        suma_nieparz += i
print("Suma liczb nieparzystych:", suma_nieparz)

#f)

x = int(input("Podaj liczbe x: "))
for i in range (1, x+1):
    while i <= x:
      print(f"{i} ", end=" ")
      i += 1
    print()


#g)

n = int(input("Podaj liczbe naturalna n: "))
suma = 0 
for i in range(n):
    liczba = float(input(f"Podaj liczbę {i+1}: "))
    suma += liczba
print("Suma liczb wynosi: ", suma)


#h)

n = int(input("Podaj liczbe naturalna n: "))
licznik = 0 
for i in range(n):
    liczba = float(input(f"Podaj liczbę {i+1}: "))
    if liczba % 3 == 0 and liczba % 5:
        licznik += 1
print("Liczba liczb podzielnych przez 3 ale nie przez 5 wynosi:", licznik)



# Cwiczenie 2
# a)

licznik = 0
znak = ""
while znak != 'x':
    znak = input("Wprowadz znak: ")
    licznik += 1
print("Liczba wprowadzonych znaków przed x:", licznik)

# b)

while True:
    liczba = int(input("Podaj liczbe: "))
    if 1 <= liczba <= 10:
        break
    else:
        print("Dwukrotność twojej liczby to:", liczba*2)

# c)
liczba1 = int(input("Podaj liczbe 1: "))
liczba2 = int(input("Podaj liczbe 2: "))
liczba3 = int(input("Podaj liczbe 3: "))
while liczba1 < 0 or liczba2 < 0 or liczba3 < 0:
    if liczba1 == 0 or liczba2 == 0 or liczba3 == 0:
        print("Któraś z liczb jest zerem.")
    else:
        print("Podano liczbę ujemną.")
    liczba1 = int(input("Podaj liczbę 1 ponownie: "))
    liczba2 = int(input("Podaj liczbę 2 ponownie: "))
    liczba3 = int(input("Podaj liczbę 3 ponownie: "))

# d)

import random

proby = 0
a = random.randint(1, 101)

while True:
    b = int(input("Podaj losową liczbę: "))
    proby += 1
    if b < a:
        print("Szukana wartość jest większa.")
    if b > a:
        print("Szukana wartość jest mniejsza.")
    if b == a:
        print("Udało się! Liczba prób:", proby)
        break


# e)

m = int(input("Podaj liczbę m: "))
potega = 1
while m > 2:
    potega+= 1
    if 3**potega < m:
        print(f"3 do potegi {potega} wynosi: {3**potega}")
    else:
        break
else:
    print("Liczba m powinna być większa od 2.")


# f)

proby = 1
while proby <= 3:
    miesiac = int(input("Podaj liczbe miesiaca (1-12): "))
    proby += 1
    if 1 <= miesiac <= 12:
        print("Numer miesiąca:", miesiac)
    else:
        print("Podano zły miesiąc.")
        break