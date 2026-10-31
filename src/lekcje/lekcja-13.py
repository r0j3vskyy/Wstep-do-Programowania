# Cwiczenie 1
class Postac:
    def __init__(self, imie, ptaktyki, zycie):
        self.imie = imie
        self.zycie = float(zycie)
        self.ptaktyki = int(ptaktyki)
    
    def gitzycie(self):
        if self.zycie>100:
            self.zycie = 100
        if self.zycie<0:
            self.zycie = 0

class Lucznik(Postac):
    def __init__(self, imie, zrecznosc, ptaktyki, zycie):
        super().__init__(imie, ptaktyki, zycie)
        self.zrecznosc = int(zrecznosc)
    
    def sila_ataku(self):
        atak = self.zrecznosc*self.ptaktyki*self.zycie
        return atak
    
class Wojownik(Postac):
    def __init__(self, imie, zycie, sila, ptaktyki):
        super().__init__(imie, ptaktyki, zycie)
        self.sila = int(sila)
    
    def sila_ataku(self):
        if self.zycie < 20:
            self.zycie *= 1.5
        atak = self.sila*self.ptaktyki*self.zycie
        return atak

Legolas = Lucznik(imie="Legolas", zrecznosc=15, ptaktyki=10, zycie=83)
Smaug = Wojownik(imie="Smaug", sila=25, ptaktyki=10, zycie=96)

# Cwiczenie 2
#a)
import random

def generator():
    from pathlib import Path

    data_dir = Path(__file__).resolve().parents[2] / "data"
    liczby = [random.randint(-100, 100) for _ in range(101)]
    parzyste = [liczba for liczba in liczby if liczba %2 == 0]
    nieparzyste = [liczba for liczba in liczby if liczba %2 != 0]
    (data_dir / "even.txt").write_text(str(parzyste), encoding="utf-8")
    (data_dir / "odd.txt").write_text(str(nieparzyste), encoding="utf-8")
    return f'Gotowe'
#b)
def liczenie():
    from pathlib import Path

    data_dir = Path(__file__).resolve().parents[2] / "data"
    parzyste = (data_dir / "even.txt").read_text(encoding="utf-8")
    nieparzyste = (data_dir / "odd.txt").read_text(encoding="utf-8")
    lp = [int(x) for x in parzyste.strip("[]").split(', ')]
    np = [int(x) for x in nieparzyste.strip("[]").split(', ')]
    sumalp, sumanp = 0, 0
    for liczba in lp:
        sumalp += liczba
    srednialp = sumalp/len(lp)
    srednialp = round(srednialp, 3)
    for liczba in np:
        sumanp += liczba
    srednianp = sumanp/len(np)
    srednianp = round(srednianp, 3)
    return f"Suma liczb parzystych: {sumalp}, ich srednia: {srednialp}. Suma liczb nieparzystych: {sumanp}, ich srednia: {srednianp}."

print(generator())
print(liczenie())

#Cwiczenie 3

from pathlib import Path

data_dir = Path(__file__).resolve().parents[2] / "data"
dna = (data_dir / "DNA.txt").read_text(encoding="utf-8").upper().replace("N", "")
a, c, g, t = 0, 0, 0, 0
for letter in dna:
    if letter == "A":
        a += 1
    if letter == "C":
        c += 1
    if letter == "G":
        g += 1
    if letter == "T":
        t += 1
print(f"Adenina: {a}, Cytozyna: {c}, Guanina: {g}, Tymina: {t}")
print("GAGA wystepuje: ",dna.count("GAGA"))
print("7 Guanin pod rzad: (index)",dna.find("GGGGGGG"))
print("6 cytozyn pod rząd od końca", dna[::-1].find("CCCCCC"))
print("CTGAAA: ", dna.count("CTGAAA"))
print("CTGAA: ", dna.count("CTGAA"))

rna = dna.replace("T", "U")
(data_dir / "RNA.txt").write_text(rna, encoding="utf-8")
