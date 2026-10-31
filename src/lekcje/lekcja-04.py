#cwiczenie 1
#a)
n = 5
s = 1
for i in range(1, n+1):
    s*=i

print(s)

#b)
a = 1
c = 0
while (a<3):
    for b in range (1,3):
        c += a+b+1
        c+=8
    a += 1
    print(c)

#cwiczenie 2
#a)

def dziel(x,y):
    if y == 0:
        return("Nie można dzielić przez 0.")
    else:
        z = x/y
        return(z)

print(dziel(5.0, 2))
print(dziel(3, 0))

#b)

def konwerter(temp, jednostka='C'):
    if jednostka == 'C':
        return (temp * 9/5) + 32
    elif jednostka == 'F':
        return (temp - 32) * 5/9
    else:
        return "Nieprawidłowa jednostka"

print(konwerter(25, 'C'))
print(konwerter(77, 'F'))

#cwiczenie 3
#a)

def liczba_cyfr(n):
    n = abs(n) 
    licznik = 0
    if n == 0:
        return 1
    while n > 0:
        n = n//10
        licznik += 1
    return licznik

def main():
    liczba = int(input("Podaj liczbę całkowitą: "))
    print("Liczba cyfr:", liczba_cyfr(liczba))

main()


#b)

def czy_pierwsza(n):
    if n <= 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def main():
    liczba = int(input("Podaj liczbę całkowitą: "))
    if czy_pierwsza(liczba):
        print("Liczba jest pierwsza.")
    else:
        print("Liczba nie jest pierwsza.")

main()

#cwiczenie 4

def funkcja_kwadratowa(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Nieskończona ilość rozwiązań."
            else:
                return "Brak rozwiązań."
        else:
            return -c / b
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b - delta**0.5) / (2*a)
            x2 = (-b + delta**0.5) / (2*a)
            return f"Rozwiązania funkcji kwadratowej to: x1 = {x1}, x2 = {x2}."
        if delta == 0:
            x = -b / (2*a)
            return f"Rozwiązanie funkcji kwadratowej to: x = {x}."
        else:
            czesc_rzeczywista = -b / (2 * a)
            czesc_urojona = (-delta)**0.5 / (2 * a)
            return (f"Rozwiązania zespolone: x1 = {czesc_rzeczywista} + {czesc_urojona}i, "
                    f"x2 = {czesc_rzeczywista} - {czesc_urojona}i")
        
def main():
    a = float(input("Podaj wartość a: "))
    b = float(input("Podaj wartość b: "))
    c = float(input("Podaj wartość c: "))
    print(funkcja_kwadratowa(a,b,c))

main()

#cwiczenie 5

def signum(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    else:
        return 0

def main():
    liczba = float(input("Podaj liczbe: "))
    wynik = signum(liczba)
    print(f"Znak liczby {liczba} to {wynik}.")

main()

#cwiczenie 6

def liczn(n):
    e1 = (1 + 1/n)**n
    e2 = 0
    silnia = 1
    for k in range(n+1):
        e2 += 1/silnia
        silnia *= (k+1)
    return f"Wynik e1: {e1}, e2: {e2}."

def main():
    n = int(input("Podaj liczbe n: "))
    print(liczn(n))

main()
