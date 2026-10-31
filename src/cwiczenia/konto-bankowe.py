class Account:
    def __init__(self, wlasciciel, saldo=0):
        self.wlasciciel = wlasciciel
        self.saldo = saldo
    
    def wplata(self, wartosc):
        if wartosc > 0:
            self.saldo += wartosc
            print(f"Wplacono {wartosc}. Nowe saldo: {self.saldo}")
        else:
            print("Kwota musi byc wieksza niz 0.")
    
    def wyplata(self, wartosc):
        if self.saldo >= wartosc > 0:
            self.saldo -= wartosc
            print(f"Wyplacono {wartosc}. Nowe saldo: {self.saldo}")

    def przelew(self, konto_docelowe, wartosc):
        if self.saldo >= wartosc > 0:
            self.saldo -= wartosc
            konto_docelowe.wplata(wartosc)
            print(f"Przelano {wartosc} do {konto_docelowe.wlasciciel}")
        else:
            print("Niewystarczajace srodki na przelew.")

    def __str__(self):
        return f"Konto wlasciciela: {self.wlasciciel}, Saldo: {self.saldo} zl"
    
konto1 = Account("Marcin Lewandowski", 1000)
print(konto1)
konto1.wplata(250)
print(konto1)
konto2 = Account("Oliwia Zielińska", 500)
konto1.przelew(konto2, 300)
print(konto1)
print(konto2)