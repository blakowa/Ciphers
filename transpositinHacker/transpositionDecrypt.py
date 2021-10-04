# Deszyfrowanie wiadomości chronionej szyfrem przestawieniowym
# 

import math, pyperclip

def main():
    myMessage = 'JQDKZACYCPTRLHBQEWLWGQRIITGHVZCEZAAIFBZXBOHSGWBHKWEUYNTVNVYPDIKHYABDJZCMMUENZWWXSTJLOKJLACNCQFEUROKGISBQBQPGVZKWGMYRMCELSFNLPKNTUGFRDVGNPVQSAKKELFJWLOAULRMWOXNASGAQSSUQRJDCERSJRVPOWXTFFVIBIBGUHUDOYZKVTZDMDBTJHNVUDEFLXOCXAGZFMNJKIXWPQYIOTAHJDLRZJXPMPFMUHFPNRXOSEXUCHEYYCYOQBSDMIXYHPITTVM'
    myKey = 2

    plaintext = decryptMessage(myKey, myMessage)

    # Wyświetlenie na końcu znaku potoku '|' na wypadek
    # gdyby szyfrowana wiadomość kończyła się spacją
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # Ta funkcjia deszyfrowania będzie symulowała "kolumny" i "wiersze"
    # siatki, na której zostanie umieszczony zwykły tekst na podstawie
    # listy ciągów tekstowych; najpierw trzeba obliczyć kilka wartości:

    # Liczba kolumn siatki:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # Liczba wierszy siatki:
    numOfRows = key
    # Liczba zamazanych kratek w ostatniej kolumnie siatki:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Każdy ciąg tekstowy w zwykłym tekście reprezentuje kolumne w siatce:
    plaintext = [''] * numOfColumns

    # Zmienne kolumn i row wskazują kratkę w której 
    # ma zostać umieszczony następny znak szyfrogramu
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        # Jeżeli nie ma więcej kolumn LUB bieżąca kratka jest zamazana
        # należy powrócić do pierwszej kolumny i przejść do następnego wierza:
        if (column == numOfColumns) or (column == numOfColumns -1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)


# Jeżeli program transpositionDecrypt.py został uruchomiony (a nie
# zaimplementowany jako moduł), należy wywołać funkcje main()
if __name__ == '__main__':
    main()