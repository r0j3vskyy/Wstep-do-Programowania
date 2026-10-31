# Cwiczenie 1
#a)

panstwa = {"Niemcy", "Hiszpania", "Polska", "Francja", "Norwegia"}
panstwa.add("Polska") #nie dziala bo jest juz element w zbiorze
print("Polska" in panstwa)
panstwa.remove("Niemcy")
print(panstwa)

#b)

zbior1 = {"Wrocław", "Olsztyn", "Warszawa", "Kraków", "Toruń"}
zbior2 = {"Szczecin", "Gdańsk", "Warszawa", "Bydgoszcz", "Olsztyn"}

kr1 = zbior1.union(zbior2) #miasta ktore sa w przynajmniej jednym ze zbiorow (suma zbiorow)
print(kr1)

kr2 = zbior1.intersection(zbior2) #miasta ktore sa jednoczesne we wwszystkich zbiorach (czesc wspolna)
print(kr2)

kr3 = zbior1.difference(zbior2) #miasta sa w pierwszym zbiorze, ale nie ma w drugim (roznica zbiorow)
print(kr3)

kr4 = zbior1.issubset(zbior2) #czy z1 jest podzbiorem z2?
print(kr4)

# Cwiczenie 2
#a)

telefony = {
    "Marcin Lewandowski": 123456789,
    "Oliwia Zielińska": 987654321,
    "Robert Wiśniewski": 555123456,
    "Tomasz Kaczmarek": 213769420
}

print(telefony)
print(telefony["Marcin Lewandowski"])
telefony["Natalia Wójcik"] = 872367094
del telefony["Oliwia Zielińska"]


def print_phone_numbers(telefony):
    for imie, numer in telefony.items():
        print(f"{imie} ma numer {numer}")

print_phone_numbers(telefony)

#b)
# kropka 1
dni_tygodnia = {
    "Monday": "poniedziałek",
    "Tuesday": "wtorek",
    "Wednesday": "środa",
    "Thursday": "czwartek",
    "Friday": "piątek",
    "Saturday": "sobota",
    "Sunday": "niedziela"
}

def zamien_dni(dni):
    return dni.copy()

def odwrotne_zamien_dni(dni):
    return dict(zip(dni.values(), dni.keys()))

# Przykłady użycia
print(zamien_dni({"Monday": "poniedziałek", "Tuesday": "wtorek"}))
print(odwrotne_zamien_dni({"poniedziałek": "Monday", "wtorek": "Tuesday"}))


# kropka 2
miesiace = {
    "Styczeń": 1,
    "Luty": 2,
    "Marzec": 3,
    "Kwiecień": 4,
    "Maj": 5,
    "Czerwiec": 6,
    "Lipiec": 7,
    "Sierpień": 8,
    "Wrzesień": 9,
    "Październik": 10,
    "Listopad": 11,
    "Grudzień": 12
}

lista = ['Maj', 'Luty', 'Styczeń', 'Grudzień', 'Lipiec']
posortowana_lista = sorted(lista, key=lambda x: miesiace[x])

print(posortowana_lista)

# kropka 3
def rzymskieNAarabskie(rzymskie):
    rzymskie_liczby = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    suma = 0
    poprzednia_wartosc = 0
    for litera in rzymskie:
        wartosc = rzymskie_liczby[litera]
        if wartosc > poprzednia_wartosc:
            suma -= poprzednia_wartosc
        else:
            suma += poprzednia_wartosc
        poprzednia_wartosc = wartosc
    suma += poprzednia_wartosc
    return suma

print(rzymskieNAarabskie("XIV"))
print(rzymskieNAarabskie("MCXIX"))

# kropka 4
def arabskieNArzymskie(number):
    rzymskie_wartosci = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    rzymskie = ""
    
    for value, symbol in rzymskie_wartosci:
        while number >= value:
            rzymskie += symbol
            number -= value
    
    return rzymskie

# Przykład użycia
print(arabskieNArzymskie(14))  # XIV
print(arabskieNArzymskie(1994))  # MCMXCIV
