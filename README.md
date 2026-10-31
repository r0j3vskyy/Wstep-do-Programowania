# Wstęp do programowania — Python

Zbiór ćwiczeń z podstaw programowania w Pythonie: instrukcje warunkowe,
pętle, funkcje, napisy, kolekcje, programowanie obiektowe, rekurencja
oraz praca z plikami.

## Struktura

```text
.
├── data/                 # pliki wejściowe i przykładowe dane
├── src/
│   ├── cwiczenia/        # dodatkowe ćwiczenia, m.in. DNA i konto bankowe
│   └── lekcje/           # materiały z kolejnych lekcji
├── .gitignore
└── README.md
```

## Uruchamianie

Wymagany jest Python 3.10 lub nowszy. Przykładowe polecenia uruchamiane
w katalogu głównym projektu:

```powershell
python src\lekcje\lekcja-01.py
python src\lekcje\lekcja-13.py
python src\cwiczenia\dna.py
```

Niektóre skrypty pobierają dane z wejścia. `dna.py` i `lekcja-13.py`
korzystają z plików znajdujących się w `data/`.

## Sprawdzenie składni

```powershell
python -m compileall src
```

Skrypty są niezależnymi przykładami edukacyjnymi, dlatego część z nich
uruchamia kilka ćwiczeń po kolei i oczekuje danych wpisywanych w konsoli.
