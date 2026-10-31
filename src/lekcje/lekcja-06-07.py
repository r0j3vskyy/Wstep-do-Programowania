# Ćwiczenie 1
n = int(input("Podaj liczbę wierszy: "))

for wiersz in range(n):
    wspolczynniki = [1]
    for miejsce in range(wiersz):
        poprzedni = wspolczynniki[-1]
        wspolczynniki.append(poprzedni * (wiersz - miejsce) // (miejsce + 1))

    odstep = " " * (n - wiersz - 1)
    print(odstep + " ".join(map(str, wspolczynniki)))

#Cwiczenie 2

def czy_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def blizniak(x=1000):
    bliz = []
    for i in range(2, x-1):
        if czy_pierwsza(i) and czy_pierwsza(i+2):
            bliz.append((i, i+2))
    return bliz

x = int(input("Podaj liczbe:"))
print(blizniak(x))

#Cwiczenie 3

def liczcat(ile):
    Catalan = [1]
    n = 1
    while Catalan[-1] < ile:
        licz = ((4*n-2)*Catalan[n-1])//(n+1)
        if licz >= ile:
            break
        Catalan.append(licz)
        n += 1
    return Catalan

ile = 1000000
print(liczcat(ile))

#Cwiczenie 4

def is_perfect_number(n):
    sumadziel = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    return sumadziel == n

number = int(input("Podaj liczbę naturalną: "))
if is_perfect_number(number):
    print(f"Liczba {number} jest liczbą doskonałą!")
else:
    print(f"Liczba {number} nie jest liczbą doskonałą.")
