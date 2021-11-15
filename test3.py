import zad3, sys

if len(sys.argv) == 1:
    print("Podaj nazwe pliku!")
    sys.exit(1)
else:
    nazwa = sys.argv[1]
    zad3.Funkcja3(nazwa)