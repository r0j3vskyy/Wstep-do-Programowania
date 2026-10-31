#cwiczenie 1

imie = input("Wprowadz swoje imie: ")
print("Hello world, " +imie, "!")

#cwiczenie 2

var1 = 2
var2 = 3
var1 += 2
var3 = var1
var1 *= 3 
var4 = var1/var2

#cwiczenie 3

#a)
age = int(input("Wprowadz swoj wiek: "))
if age >= 18 and age <= 100:
    print("Autoryzacja uzyskana")
else: print("Odmowa")

#b)
a = int(input("Wprowadz liczbe:"))
if a > 0:
    print("|a|=", +a)
else:
    print("|a|=", -a)

#c)
a = 50
b = 10
if a>b:
    print("Hello World")

#d)
x = int(input("Wprowadz liczbe: "))
if x % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")

#e)
liczba1 = float(input("Wprowadz liczbe nr 1: "))
liczba2 = float(input("Wprowadz liczbe nr 2: "))
if liczba1 > liczba2:
    print("Liczba ", +liczba1, "jest wieksza")
elif liczba2 > liczba1:
    print("Liczba ", +liczba2, "jest wieksza")
else:
    print("Liczby są równe.")

#f)
l1 = int(input("Podaj liczbe: "))
if 1 <= l1 <= 10:
    print("Liczba nalezy do przedzialu nr 1")
elif 17 <= l1 <= 21:
    print("Liczba nalezy do przedzialu nr 2")
else:
    print("Liczba nie nalezy do zadnego przedzialu")

#g)
gl1 = int(input("Podaj liczbe calkowita: "))
if gl1 % 3 == 0 and gl1 % 5 == 0:
    print("Liczba jest podzielna przez 3 i przez 5.")
elif gl1 % 3 == 0 and not gl1 %5 == 0:
    print("Liczba jest podzielna przez 3, ale nie przez 5.")
elif gl1 % 5 == 0 and not gl1 %3 == 0:
    print("Liczba jest podzielna przez 5, ale nie przez 3.")
elif not gl1 % 3 == 0 and not gl1 %5 == 0:
    print("Liczba nie jest podzielna przez 3 ani przez 5.")

#h)
kl1 = float(input("Podaj liczbe nr1: "))
kl2 = float(input("Podaj liczbe nr2: "))
print("Wybierz co chcesz zrobić:")
print("1 - dodawanie")
print("2 - odejmowanie")
print("3 - mnożenie")
print("4 - dzielenie")
oper = int(input())
if oper in (1,2,3,4):
    if oper == 1:
        kl3 = kl1+kl2
        print("Wynik:", +kl3)
    if oper == 2:
        kl3 = kl1-kl2
        print("Wynik:", +kl3)
    if oper == 3:
        kl3 = kl1*kl2
        print("Wynik:", +kl3)
    if oper == 4:
        kl3 = kl1/kl2
        print("Wynik:", +kl3)
else:
    print("Błąd.")

#i)
stopnie = float(input("Ile stopni: "))
print("Jak zamieniamy?")
print("Fahrenheit na Celsjusz - 1")
print("Celsjusz na Fahrenheit - 2")
wyb = int(input())
if wyb in (1,2):
    if wyb == 1:
        c = (stopnie - 32)*5/9
        print("Stopni Fahrenheita: ", +c)
    if wyb == 2:
        c = (stopnie * 9/5)+32
        print("Stopni Celsjusza: ", +c)
else:
    print("Błąd.")


#j)
def czy_trojka_pitagorejska(a, b, c):
    liczby = sorted([a, b, c])
    return liczby[0]**2 + liczby[1]**2 == liczby[2]**2

a = int(input("Wprowadź pierwszą liczbę: "))
b = int(input("Wprowadź drugą liczbę: "))
c = int(input("Wprowadź trzecią liczbę: "))

if czy_trojka_pitagorejska(a, b, c):
    print("Liczby stanowią trójkę pitagorejską.")
else:
    print("To nie jest trójka pitagorejska.")