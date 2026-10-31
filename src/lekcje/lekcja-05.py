#Cwiczenie 1
#a)
def gmean(*args):
    iloczyn = 1
    for i in args:
        iloczyn *= i
    n = len(args)
    srednia = iloczyn**(1/n)
    return srednia

print(gmean(2,4,8))

#b)
def wypisz(*args):
    for i in range(1, len(args)+1):
        print(*args[:i])
wypisz(3, 'Ala', 5)

#c)
def wypiszz(*args):
    for i in range(len(args)):
        for _ in range(i+1):
            print((args[i]), end=" ")
        print()

wypiszz(3, 'Ala', 5)

#Cwiczenie 2
#a)
def my_max(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return "Liczby są równe."
    
def main(a,b):
    print(my_max(a,b))

main(1,4)
main(11, 15)
main(7, 42)

#b)
def my_max(a,b,c):
    x = max(a,b,c)
    return x

def main(a,b,c):
    print(my_max(a,b,c))

main(1, 4, 7)
main(11, 15, 4)
main(7, 42, 11)

#c)
def my_max(*args):
    a = max(*args)
    return a

def main(*args):
    print(my_max(*args))

main(3, 11, 5, 9, 4, 7)
main(17, 4, 1, 0, 1347)
main(17, 4, 5, 1999, 2347834)

#Cwiczenie 3
#a)
licznik = 0
def finabocci(n):
    global licznik
    licznik += 1
    if n <= 1:
        return n
    else:
        return finabocci(n-1) + finabocci(n-2)
    
def main(n):
    print(finabocci(n))
    print(f"Ilość powtórzeń dla {n}: {licznik}.")

main(10)
main(29)
main(100)

#b)
def finaboci(n):
    licznik = 0

    if n == 0:
        return n, licznik
    if n == 1:
        return n, licznik
    
    a, b = 0, 1
    for _ in range(2, n+1):
        licznik += 1
        a, b = b, a + b
    return b, licznik
    
def main(n):
    wynik, licznik = finaboci(n)
    print(f"Wynik Finabocciego dla {n} to: {wynik}")
    print(f"Licznik powtórzeń: {licznik}")

main(10)
main(29)
main(100)

#Cwiczenie 4
#a)
def euklid(a,b):
    while b!=0:
        c = a%b
        a = b
        b = c
    return a

def main(a,b):
    print(euklid(a,b))

main(15,25)
main(216, 42)
main(211, 71)

#b)
def euklid(a,b):
    while b!=0:
        c = a%b
        a = b
        b = c
    return a

def skr(a,b):
    dzielnik = euklid(a,b)
    p = a // dzielnik
    q = b // dzielnik
    return p,q


def main(a,b):
    print(skr(a,b))

main(6,9)
main(25, 15)
main(12, 8)

#Cwiczenie 5