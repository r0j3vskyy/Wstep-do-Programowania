#Cwiczenie 1

napis = "Sed luctus rhoncus magna, ac mollis mi malesuada ac. Aliquam vel fringilla dui, vitae rhoncus tellus. Praesent lectus tellus, imperdiet sed varius id, imperdiet nec diam. In sed convallis neque. Nulla condimentum vulputate tempus. Integer ut elementum mauris. Sed egestas tempor magna, eget pharetra dui lobortis ac. Proin fermentum id odio eu aliquam."

#a) 
dlugosc = len(napis)
print(f"Dlugosc napisu to: {dlugosc}")
#b)
znak1 = napis[12]
znak2 = napis[7]
znak3 = napis[-4]
print(znak1, znak2, znak3)
print(znak1+znak2+znak3)
#c)
print(znak1 + znak3*2 + znak2)
print(znak3*4 + (znak2+znak1)*7)
#d)
male = napis.lower()
print(male)
#e)
duzalitera = napis.capitalize()
print(duzalitera)
capslock = napis.upper()
print(capslock)
switch = napis.swapcase()
print(switch)


#Cwiczenie 2

napis = "Marcin Lewandowski"

#a)
oddzielnie = napis.split()
imie = oddzielnie[0]
nazwisko = oddzielnie[1]
print(imie, nazwisko)
#b)
nowe = nazwisko + " " + imie
print(nowe)
#c)
import random

litery = list(napis)
random.shuffle(litery)
znowurazem = ''.join(litery)
print(znowurazem.capitalize())
#d)
oddzielnie = napis.split()
imie = oddzielnie[0][0]
nazwisko = oddzielnie[1][0]
inicjaly = imie+nazwisko
print(inicjaly)
#e)
oddzielnie = napis.split()
imie = oddzielnie[0]
nazwisko = oddzielnie[1]
noweimie = nazwisko[0]+imie[1:]
nowenazwisko = imie[0]+nazwisko[1:]
print(noweimie + ' ' + nowenazwisko)


#Cwiczenie 3
#a)
def parzysta(napis):
    lista = list(napis)
    wynik = ''.join(lista[i] for i in range(1, len(lista), 2))
    return wynik

napis = input("Wprowadz swoj napis: ")
wynik = parzysta(napis)
print(wynik)

#b)
def ostatnie(napis, n=1):
    return napis[-n:]

napis = input("Podaj napis: ")
n = int(input("Podaj ilosc ostatnich znakow:"))
wynik = ostatnie(napis, n)
print(wynik)

#c)
def odwroc_napis(napis):
    return ''.join(reversed(napis))

napis = input("Wprowadź swój napis: ")
wynik = odwroc_napis(napis)
print("Odwrocony napis:", wynik)

#d)
def jest_palindromem(tekst):
    # Usuń spacje i znaki
    tekst = ''.join(e for e in tekst if e.isalnum()).lower()
    # Porównaj tekst z odwrotnością
    return tekst == tekst[::-1]

#e)
def policz_litera(tekst, litera):
    return tekst.count(litera)
def policz_wszystkie_litera(tekst):
    return sum(1 for e in tekst if e.isalpha())


print(policz_litera("Sieremere bum cyk cyk", "k"))
print(policz_wszystkie_litera("Sieremere bum cyk cyk"))

#f)
def zlicz_slowa(tekst):
    return len(tekst.split())

#g)
def zlicz_samogloski(tekst):
    samogloski = "aeiouyąęćżźółś"
    return sum(1 for e in tekst.lower() if e in samogloski)

def zlicz_spolgoski(tekst):
    spolgoski = "bcdfghjklmnpqrstvwxyzćżź"
    return sum(1 for e in tekst.lower() if e in spolgoski)

#h)
def policz_litera(tekst):
    return sum(1 for e in tekst if e.isalpha())

#Cwiczenie 4
#a)

def wstaw_dane(imie, data_urodzenia):
    return f'My name is {imie}. My date of birth is {data_urodzenia}.'

print(wstaw_dane('Tomasz', '1990-01-01'))

#b)
def wstaw_dane_lacznie(a, b):
    return f'{a} + {b} = {a + b}'

#Cwiczenie 5
def zamien_litera(wyrazenie):
    zmiany = 0
    nowe_wyrazenie = ''
    for litera in wyrazenie:
        if litera.lower() == 'a':
            nowe_wyrazenie += 'A'
            zmiany += 1
        elif litera.lower() == 'b':
            nowe_wyrazenie += 'B'
            zmiany += 1
        elif (len(wyrazenie) % 2 != 0) and (litera.lower() == wyrazenie[len(wyrazenie) // 2].lower()):
            nowe_wyrazenie += litera.upper()
            zmiany += 1
        else:
            nowe_wyrazenie += litera
    return f"{nowe_wyrazenie}, Liczba zmian: {zmiany}"


print(zamien_litera(f"Siema siema elo dwa jeden trzy siedem bbb"))

#Cwiczenie 6
#a)?????????????????
#b)
def szyfruj_przestaw(tekst):
    zaszyfrowany_tekst = ''
    for i in range(0, len(tekst), 2):
        if i + 1 < len(tekst):
            zaszyfrowany_tekst += tekst[i+1] + tekst[i]
        else:
            zaszyfrowany_tekst += tekst[i]
    return zaszyfrowany_tekst


print(szyfruj_przestaw("Riko i koko"))

#Cwiczenie 7
def suma_liczb(tekst):
    liczby = []
    liczba = ""
    
    for znak in tekst:
        if znak.isdigit():  # Jeśli znak jest cyfrą, dodaj go do liczby
            liczba += znak
        elif liczba:  # Jeśli liczba została zakończona, dodaj ją do listy
            liczby.append(int(liczba))
            liczba = ""
    
    # Dodaj ostatnią liczbę, jeśli tekst kończy się liczbą
    if liczba:
        liczby.append(int(liczba))
    
    return sum(liczby)

# Przykład użycia
tekst = "W roku pańskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalił dekret o 20 procentowej zniżce podatków"
wynik = suma_liczb(tekst)
print(f"Suma liczb w tekście to: {wynik}")
