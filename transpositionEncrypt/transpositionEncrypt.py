# Szyfr kolumnowy
#

import pyperclip

def main():
    myMessage = 'JEQLDFKJZWALCOYACUPLTRRMLWHOBXQNEAWSLGWAGQQSRSIUIQTRGJHDVCZECRESZJARAVIPFOBWZXXTBFOFHVSIGBWIBBHGKUWHEUUDYONYTZVKNVVTYZPDDMIDKBHTYJAHBNDVJUZDCEMFMLUXEONCZXWAWGXZSFTMJNLJOKKIJXLWAPCQNYCIQOFTEAUHRJODKLGRIZSJBXQPBMQPPFGMVUZHKFWPGNMRYXROMSCEEXLUSCFHNELYPYKCNYTOUQGBFSRDDMVIGXNYPHVPQISTATKVKM'
    myKey = 2

    ciphertext = encryptMessage(myKey, myMessage)

    # Wyświetlanie szyfrogramu na ekranie ze 
    # znakiem potoku (|) na końcu na wypadek
    # gdyby szyfrogram kończył się spacją:
    print(ciphertext + '|')

    # Skopiowanie szyfrogramu do schowka:
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    # Każdy ciąg tekstowy w szyfrogrami przedstawia kolumne siatki:
    ciphertext = [''] * key

    # Iteracja przez poszczególne kolumny szyrogramu:
    for column in range(key):
        currentIndex = column

        # Pętla będzie wykonywana dopóki wartość currentIndex nie będzie większa niż liczba określająca długość wiadomości:
        while currentIndex < len(message):
            # Znak znajdujący się w położeniu currentIndex zmiennej message
            # zostaje umieszczony na końcu bieżącej kolumny listy szyrogramu:
            ciphertext[column] += message[currentIndex]

            # Zwiększenie wartości currentIndex o wartość klucza:
            currentIndex += key

    # Konwersja listy szyfrogramu na watość w postaci pojedyńczego ciągu tekstowego i jej zwrot:
    return ''.join(ciphertext)


# Jeżli program transpositionEncrypt.py(Szyfr kolumnowy.py) został uruchomiony (a nie
# zaimportowany jako moduł), wówczas należy wywołać funkcje main():
if __name__ == '__main__':
    main()