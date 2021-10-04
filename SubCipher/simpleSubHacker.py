# Łamanie prostego szyfru podstawiniowego
# https://www.nostarch.com/crackingcodes/ (na licencji BSD)

import os, re, copy, pyperclip, simpleSubCiphre, wordPatterns, makeWordPatterns





LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

    # Potencjalnie udane złamanie szyfru
    print('Łamanie szyfru...')
    letterMapping = hackSimpleSub(message)

    # Wyświetlanie wyniku użytkownikowi
    print('Mapowanie:')
    print(letterMapping)
    print()
    print('Pierwotny szyfrogram:')
    print(message)
    print()
    print('Deszyfrowana wiadomość została skopiowana do schowka:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)


def getBlankCipherletterMapping():
    # Ta funkcja zwraca słownik, który obecnie jest pustym mapowaniem
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def addLettersToMapping(letterMapping, cipherword, candidate):
    # Parametr letterMapping pobiera słownik, który przechowuje mapowanie
    # liter szyfru. To mapowanie zostanie skopiowane przez funkcję.
    # Parametr cipherword to ciąg tekstowy w postaci słowa szyfru.
    # Parametr candidate to potencjalne słowo w języku angielskim, które
    # może być deszyfrowaną wersją wartości parametru cipherword

    # Ta funkcja dodaję litery kandydata jako potencjalne
    # litery deszyfrowania do mapowania liter na
    # litery szyfru


    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])



def intersectMappings(mapA, mapB):
    # Aby połączyć dwa mapowania należy utworzyć puste mapowanie, a następnie
    # dodawać potencjalne litery deszyfrowania tylko wtedy, gdy instnieją w OBU mapowaniach
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:

        # Pusta lista oznacza że każda litera jest możliwa; w takim
        # przypadku należy w całości skopiować drugie mapowanie
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            # Jeżeli litera z mapA[letter] instnieje w mapB[letter]
            # to należu ją dodać do intersectedMapping[letter]
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
    # Litery szyfru, którym w mapowaniu odpowiada tylko jedna litera, są
    # "desszyfrowane" i mogą zostać usunięte z listy liter.
    # Przykładowo jeśli 'A' jest mapowanie na potencjalne litery ['M','N'], a B
    # jest mapowana na ['N'], wówczas wiadomo, że litera 'B' musi być mapowana na 'N',
    # więc można usunąć 'N' z listy mapowanych liter dla 'A'. W takim przypadku litera 'A'
    # jest mapowana na ['M']. Zwróć uwagę że litera 'A' jest mapowana na jedną
    # literę, więc można usunąć 'M' z listy liter przypisanych pozostałym literom.
    # (Dlatego użyta została pętla niesutanie zmniejszająca mapowanie)

    loopAgain = True
    while loopAgain:
        # Zakładamy że jest to ostania iteracja pętli
        loopAgain = False

        # solvedLetters to lista wielkich liter, które mają
        # tylko jedno możliwe mapowanie w letterMapping
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # Jeżeli litera jest deszyfrowana nie moze być potecncjalną literą
        # deszyfrowania dla innej litery szyfru, dlatego należy usunąć
        # ją z listy mapowania dla innych liter
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        # Kolejna litera została deszyfrowana, więc trzeba przeprowadzić natępną
                        # iteracje pętli
                        loopAgain = True
    return letterMapping

def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        # Pobranie nowego mapowania liter szyfru dla każdego słowa szyfru
        candidateMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue  # To słowo nie znajduję się w słowniku, więc rozpoczynamy nową iterację pętli

        # Dodanie mapowania liter wszystkich kandydatów
        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)

        # Połączenie nowego mapowania z już istniejącym mapowaniem połączonym
        intersectedMap = intersectMappings(intersectedMap, candidateMap)

    # Usunięcie deszyfrowanych liter z wszystkich list mapowania dla pozostałych liter
    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
    # Zwrot ciągu tekstowego, który został deszyfrowany za pomocą mapowania liter
    # Pozostałe nieodszyfrowane litery zostały zastąpione znakami podkreślenia

    # Trzeb zacząć od utworzenia prostego klucza na podstawie mapowania letterMapping
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # Jeżeli została tylko jedna litera należy dodać ją do klucza
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # Szyfrogram można deszyfrować za pomocą wygenerowanego klucza
    return simpleSubCiphre.decryptMessage(key, ciphertext)


if __name__ == '__main__':
    main()