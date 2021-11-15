
def Funkcja1(wejscie):

    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..'}

    tablica = list(wejscie)
    dlug = len(tablica)
    konwert = []
    blad = "blad"

    print(tablica, dlug)

    for i in range(dlug):
        jest = False
        for key, value in morse_code.items():
            if tablica[i] == key:
                konwert.append(value)
                jest = True
        if jest == False:
            konwert.append(blad)

    print(konwert)





if __name__ == "__main__":
    str = "ABcDE f"
    Funkcja1(str)