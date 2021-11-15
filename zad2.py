import zad1
def Funckja2(wejscie):

    morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'}

    code_morse = {}
    for key, value in morse_code.items():
        code_morse[value] = key

    #print(code_morse)

    tablica = wejscie.split()
    dlug = len(tablica)
    konwert = []
    blad = "blad"

    print(tablica, dlug)

    for i in range(dlug):
        jest = False
        for key, value in code_morse.items():
            if tablica[i] == key:
                konwert.append(value)
                jest = True
        if jest == False:
            konwert.append(blad)

    print(konwert)



if __name__ == "__main__":
    wejscie = "... --- ....."
    Funckja2(wejscie)