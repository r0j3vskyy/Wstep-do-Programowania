#Cwiczenie 1
class Account:
    def __init__(self, wlasciciel, saldo=0):
        self.wlasciciel = wlasciciel 
        self.saldo = saldo

    def wplata(self, amount):
        if amount > 0:
            self.saldo += amount
            print(f"Wpłacono {amount}. Nowe saldo: {self.saldo}")
        else:
            print("Kwota musi być większa od zera.")

    def wyplata(self, amount):
        if 0 < amount <= self.saldo:
            self.saldo -= amount
            print(f"Wypłacono {amount}. Nowe saldo: {self.saldo}")
        else:
            print("Niewystarczające środki lub błędna kwota.")

    def przelew(self, konto_docelowe, amount):
        if 0 < amount <= self.saldo:
            self.wyplata(amount)
            konto_docelowe.wplata(amount)
            print(f"Przelano {amount} do {konto_docelowe.wlasciciel}")
        else:
            print("Niewystarczające środki na przelew.")

    def __str__(self):
        return f"Konto właściciela: {self.wlasciciel}, Saldo: {self.saldo} zł"


class PrivatAccount(Account):
    def salary_payment(self, amount):
        self.wplata(amount)
        print(f"Wynagrodzenie {amount} wpłacone na konto prywatne {self.wlasciciel}.")


class FirmAccount(Account):
    def pay_taxes(self, amount):
        if 0 < amount <= self.saldo:
            self.wyplata(amount)
            print(f"Zapłacono {amount} podatku (ZUS/US) z konta {self.wlasciciel}.")
        else:
            print("Niewystarczające środki na zapłatę podatku.")


konto1 = Account("Marcin Lewandowski", 1000)
konto2 = PrivatAccount("Oliwia Zielińska", 500)
konto3 = FirmAccount("Firma XYZ", 10000)

konto1.deposit(200)
konto1.withdraw(300)
konto1.transfer(konto2, 400)
konto2.salary_payment(1500)
konto3.pay_taxes(2000)
konto3.withdraw(500)


#Cwiczenie 2
class Roman:
    roman_to_arabic_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    arabic_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def __init__(self, roman):
        self.roman = roman
        self.arabic = self.roman_to_arabic(roman)

    def roman_to_arabic(self, roman):
        total = 0
        prev_value = 0
        for char in reversed(roman):
            current_value = self.roman_to_arabic_map[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        return total

    def arabic_to_roman(self, arabic):
        result = ""
        for value, symbol in self.arabic_to_roman_map:
            while arabic >= value:
                result += symbol
                arabic -= value
        return result

    def __add__(self, other):
        return Roman(self.arabic_to_roman(self.arabic + other.arabic))

    def __sub__(self, other):
        return Roman(self.arabic_to_roman(self.arabic - other.arabic))

    def __mul__(self, other):
        return Roman(self.arabic_to_roman(self.arabic * other.arabic))

    def __str__(self):
        return self.roman

    def __len__(self):
        return len(self.roman)

    def __getitem__(self, index):
        return self.roman[index]


num1 = Roman("XIV")
num2 = Roman("X")
print(num1 + num2)  
print(num1 - num2)  
print(num1 * num2)  
print(len(num1))    
print(num1[0])      

#Cwiczenie 3
class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.values, other.values)])

    def __mul__(self, scalar):
        return Vector([a * scalar for a in self.values])

    def __str__(self):
        return str(self.values)

wektor1 = Vector([1, 2, 3])
wektor2 = Vector([4, 5, 6])

print(wektor1 + wektor2)
print(wektor1 - wektor2)
print(wektor1 * 2) 

#Cwiczenie 4
class Polynomial(Vector):
    def __init__(self, coefficients):
        super().__init__(coefficients)

    def degree(self):
        return len(self.values) - 1

    def __str__(self):
        result = ''
        for i, value in enumerate(self.values):
            if value != 0:
                if i > 0:
                    if value > 0:
                        result += ' + '
                    else:
                        result += ' - '
                if abs(value) != 1 or i == 0:
                    result += str(abs(value))
                if i > 0:
                    if value > 0:
                        result += 'x'
                    else:
                        result += '-x'
                if i > 1:
                    result += '^' + str(i)
        return result

    def __mul__(self, other):
        result = [0] * (self.degree() + other.degree() + 1)
        for i, value in enumerate(self.values):
            for j, value2 in enumerate(other.values):
                result[i + j] += value * value2
        return Polynomial(result)

    def evaluate(self, x):
        result = 0
        for i, value in enumerate(self.values):
            result += value * (x ** (self.degree() - i))
        return result

wielomian1 = Polynomial([2, 3, 4])
wielomian2 = Polynomial([1, 2, 3])

print(wielomian1)
print(wielomian2)
print(wielomian1 * wielomian2)
print(wielomian1.evaluate(2))