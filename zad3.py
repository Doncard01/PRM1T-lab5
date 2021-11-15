def Funkcja3(nazwa):

    file = open(nazwa, 'r')
    wszystkie_znaki = []
    slownik = {}

    for line in file:
        tablica = list(line)
        for i in tablica:
            wszystkie_znaki.append(i)

    print(wszystkie_znaki)

    for i in wszystkie_znaki:
        znak = i
        licznik = wszystkie_znaki.count(i)
        slownik[i] = licznik

    print(slownik)

    klucze = list(slownik.keys())

    print(klucze)

    najmniejszy = min(klucze)
    najwiekszy = max(klucze)

    print("Najmniejszy: ", repr(str(najmniejszy)), " wystapien: ", slownik[najmniejszy], ", najwiekszy: ", najwiekszy, " wystapien: ", slownik[najwiekszy])

    file.close()
if __name__ == "__main__":
    Funckja3("notatnik.txt")