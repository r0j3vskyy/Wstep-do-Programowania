#cwiczenie 2

print("Marcin, Oliwia, Patryk, Piotr, Monika")
print("Marcin,\n Oliwia,\n Patryk,\n Piotr,\n Monika")
print("Deadpool "*100)
a=5
b=7
print(a+b)
print(a**b)
print("")

#cwiczenie 3

print((9+4*5**(0.5))**0.5)
print((100-4*17**(0.5))**(1/3))
print((9**(-1/4)+(3*(3**(1/2)))**(4/3))*(9**(-1/4)-(3*(3**(1/2)))**(4/3)))
print((8**(-1/6)-(2*(2**(1/2)))**(-5/6))*(8*(-1/6)+(1/((2*(2*(0.5))**(5/6))))))
print(((5+2*(6**0.5))**0.5)-(1/(((5+2*(6**0.5))**0.5))))
print("")

#cwiczenie 4

pi=3.14151926
e=2.718281828
print(25*pi)
print(pi**2)
print(18*e+pi)
print(e*(pi+2))
print(pi**2)
print((12*e)**0.5)
print(e-pi)
print(pi/(e**2))
print(2**0.5)
print(pi**0.5)
print("")

#cwiczenie 5

def deg2rad(deg):
    return deg*(pi/180)
print(deg2rad(105))
print(deg2rad(35))
print(deg2rad(45))
print(deg2rad(185))
print(deg2rad(-95))
print(deg2rad(712))
print("")


#cwiczenie 6

#binarne na dziesietne
def DecToBin(b):
    return int(b, 2)
print(DecToBin("10"))
print(DecToBin("1111"))
print(DecToBin("101011"))
print(DecToBin("1101"))
print(DecToBin("10000"))
print(DecToBin("11000"))
print(" ")

#dziesietne na binarne
def nToDec(n):
    return bin(n).replace("0b", "")
print(nToDec(64))
print(nToDec(28))
print(nToDec(12))
print(nToDec(1235))
print(nToDec(29649))
print(nToDec(8912556))
print(" ")

#osemkowe na dziesietne
def octToInt(b):
    return int(b, 8)
print(octToInt("71"))
print(octToInt("2375"))
print(octToInt("16230"))
print(octToInt("777"))
print(octToInt("11111"))
print(octToInt("74367"))
print(" ")

#dziesietne na osemkowe
def DecToOct(b):
    return oct(b).replace("0o", "")
print(DecToOct(64))
print(DecToOct(512))
print(DecToOct(273))
print(DecToOct(918))
print(DecToOct(90860))
print(DecToOct(5968939))
print(" ")

#szesnastkowy na dziesietne
def hexToInt(b):
    return int(b, 16)
print(hexToInt("12F"))
print(hexToInt("7682"))
print(hexToInt("A3561"))
print(hexToInt("99"))
print(hexToInt("AB12C"))
print(hexToInt("341D"))
print(" ")

#dziesietne na szesnastkowy
def IntToHex(b):
    return hex(b).replace("0x", "")
print(IntToHex(60))
print(IntToHex(123))
print(IntToHex(256))
print(IntToHex(147178))
print(IntToHex(870))
print(IntToHex(7450091))
print(" ")

#binarne na szesnastkowe
def BinToHex(b):
    hexd = int(b, 2)
    return hex(hexd).replace("0x", "")
print(BinToHex("10000"))
print(BinToHex("101"))
print(BinToHex("100011"))
print(BinToHex("1101"))
print(BinToHex("101100"))
print(BinToHex("11"))
print(" ")

#szesnastkowe na binarne
def HexToBin(b):
    dycha = int(b, 16)
    return bin(dycha).replace("0b", "")
print(HexToBin("F"))
print(HexToBin("2C"))
print(HexToBin("AF1"))
print(HexToBin("147"))
print(HexToBin("8"))
print(HexToBin("3B11"))
print(HexToBin("16"))
print(" ")



#cwiczenie 7

# a)
a = 670
a1 = a*0.6
a2 = a1*1.4
print(f"Aktualna cena towaru: {a2}zł")

# b)
b = (185+217)*2
print(f"Ilosc znaczkow: {b}")

# c)
jab1 = 15
jab2 = 14
jab3 = 11
koszt = 8*jab1+4*jab2
print(f"Zapłacił: {koszt}zł.")
ilejab3 = koszt/jab3
ilejab3 = int(ilejab3)
print(f"Najtansze skrzynki: {ilejab3}")