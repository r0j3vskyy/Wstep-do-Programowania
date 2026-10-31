from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

dna = (DATA_DIR / "DNA.txt").read_text(encoding="utf-8").upper().replace("N", "")
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
(DATA_DIR / "RNA.txt").write_text(rna, encoding="utf-8")
