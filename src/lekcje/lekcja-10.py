# Cwiczenie 1
#a)
lista = [1, 2, "a", "b", True, 6, "c", "d", 9, False]

lista[2] = 4
print(lista[8])
print(lista[::2][::-1])
print(lista[-4])

#b)
def czy_posortowana_malejaco(lista):
    return lista == sorted(lista, reverse=True)

lista1 = [1, 4, 7, 2, 12]
lista2 = [14, 11, 7, 4, 3]

print(czy_posortowana_malejaco(lista1))
print(czy_posortowana_malejaco(lista2))

#c)
def suma_wektorow(lista1, lista2):
    return [a + b for a, b in zip(lista1, lista2)]

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(suma_wektorow(lista1, lista2))

#d)
def func(lista, n1, n2):
    for i in range(len(lista)):
        if lista[i] == n1:
            lista[i] = n2
    return None


lista = [1, 2, 3, 4, 5, 6, 7]
n1 = 4
n2 = 8
print(func(lista, n1, n2))
print(lista)

#e)
def func(lista, n1, n2):
    nowalista = []
    for i in range(len(lista)):
        if lista[i] == n1:
            nowalista.append(n2)
        else:
            nowalista.append(lista[i])
    return nowalista

lista = [1, 2, 3, 4, 5, 4, 7, 4, 4]
n1 = 4
n2 = 8
print(func(lista, n1, n2))

#f)
from math import isclose

def func(lista, n1, n2, rel_tol=1e-09, abs_tol=0.5):
    nowalista = []
    for i in lista:
        if isclose(i, n1, rel_tol=rel_tol, abs_tol=abs_tol):
            nowalista.append(n2)
        else:
            nowalista.append(i)
    return nowalista


lista = [1.4, 2.6, 3.1, 4.2, 5.5, 4.7, 7.6, 4.9, 4.5]
n1 = 4.1
n2 = 8.0
print(func(lista, n1, n2))

#g)
def numer_miesiaca(nazwa):
    miesiace = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", 
                "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    if nazwa in miesiace:
        return miesiace.index(nazwa)+1
    else:
        return None

def sortuj(lista):
    lista.sort(key=numer_miesiaca)
    return lista 

miesiace = ["Grudzień", "Marzec", "Sierpień", "Wrzesień", "Styczeń"]
print(sortuj(miesiace))


#Cwiczenie 2
#a)
krotka = (1, "napis", 3, True, 5.17, "tak o", None)
# krotka[2] = 5 
# ^ wyskakuje błąd, krotki są niezmienialne
print(krotka[3])
print(krotka[3:6])
print(krotka[-3])

#b)
# DODAWANIE ELEMENTU
# Opcja nr 1
def dodaj_element(krotka, element):
    return krotka + (element,) # <- przecinek = element jest traktowany jako krotka

# Opcja nr 2
def dodaj_element_lista(krotka, element):
    lista = list(krotka)
    lista.append(element)
    return tuple(lista)
# stworzenie z krotki listy -> dodanie do listy nowego elementu -> zwraca krotke z nowym elementem

# USUWANIE ELEMENTU
# Opcja nr 1
def usun_element_comprehension(krotka, element):
    return tuple(x for x in krotka if x != element)

# Opcja nr 2
def usun_element(krotka, element):
    lista = list(krotka)
    lista.remove(element)  # Usuwamy pierwsze wystąpienie elementu
    return tuple(lista)

#c)
#opcja nr 1
def wyswietl_unikalne_elementy_set_obok_krotka(krotka):
  """Wyświetla unikalne elementy krotki obok siebie, używając set."""
  unikalne_elementy = set(krotka)
  for element in unikalne_elementy:
    print(element, end=" ")
  print()

# Przykład użycia
moja_krotka = (1, 2, 2, 3, 4, 4, 5)
wyswietl_unikalne_elementy_set_obok_krotka(moja_krotka)

#opcja nr2
def wyswietl_unikalne_elementy_petla_obok_krotka(krotka):
  """Wyświetla unikalne elementy krotki obok siebie, używając pętli i sprawdzania."""
  unikalne_elementy = []
  for element in krotka:
    if element not in unikalne_elementy:
      unikalne_elementy.append(element)
  for element in unikalne_elementy:
    print(element, end=" ")
  print() # Dodaję przejście do nowej linii na końcu

# Przykład użycia
moja_krotka = (1, 2, 2, 3, 4, 4, 5)
wyswietl_unikalne_elementy_petla_obok_krotka(moja_krotka)


#Cwicznie 3
#a)
potegi = [i**5 for i in range(15)]
print(potegi)

#b)
silnie = [1]
for i in range(1, 11):
    silnie.append(silnie[-1] * i)
print(silnie)

#c)
e = [1]
for i in range(1, 10):
    e.append(e[-1] + 0.1)
print(e)

#d)
nazwiska = ["kowalski", "nowak", "wiśniewski", "wójcik", "kowalczyk", "lewandowski", "zieliński"]
długie_nazwiska = [nazwisko for nazwisko in nazwiska if len(nazwisko) > 6]
print(długie_nazwiska)

#e)
def parzyste_trzecia_potega(wejsciowe):
    return [i**3 for i in wejsciowe if i % 2 == 0]

#Cwiczenie 4
names = ["tomasz", "nela", "oliwia", "przemek"]

#a)
sumaryczna_dlugosc = sum(len(imie) for imie in names)
print(sumaryczna_dlugosc)

#b)
wielka_poczatek = [imie.capitalize() for imie in names]
print(wielka_poczatek)

#c)
z_litera_l = [imie for imie in names if "l" in imie]
print(z_litera_l)

#d)
żeńskie_imiona = tuple(imie for imie in names if imie.endswith("a"))
print(żeńskie_imiona)

