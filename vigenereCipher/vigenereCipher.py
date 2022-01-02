# Szyfr Vigenere'a (polialfabetyczny szyfr podstawieniowy):
# https://www.nostarch.com/crakingcodes/ (na licencji BSD)

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    # Ten tekst możesz skopiować i wkleić z pliku źrudołowego, który znajduje się na stronie https://www.nostarch.com/crackingcodes/
    myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    myKey = 'ASIMOV'
    myMode = 'szyfrowanie' # Przypisanie wartości 'szyfrowanie' lub 'deszyfrowanie'

    if myMode == 'szyfrowanie':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'deszyfrowanie':
        translated = decryptMessage(myKey, myMessage)

    print('%s tekstu:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('Wiadomość została skopiowana fo schowka.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'szyfrowanie')


def decryptMessage(key, message):
    return translateMessage(key, message, 'deszyfrowanie')


def translateMessage(key, message, mode):
    translated = [] # Przechowuje ciąg tekstowy szyfrowanej lub deszyforwanej wiadomości.

    keyIndex = 0
    key = key.upper()

    for symbol in message: # Iteracja przez wszystkie znaki wiadomości
        num = LETTERS.find(symbol.upper())
        if num != -1: # Wartość -1 oznacza że znak symbol.upper() nie został znaleziony w zmiennej LETTERS
            if mode == 'szyfrowanie':
                num += LETTERS.find(key[keyIndex])  # W przypadku szyfrowania mamy dodawaie
            elif mode == 'deszyfrowanie':
                num -= LETTERS.find(key[keyIndex])  # W przypadku deszyfrowania mamy odejmowanie

            num %= len(LETTERS)  # Obsługa zawinięcia

            # Dodawanie zaszyfrowanego lub odszyfrowanego znaku na końcu zmiennej translated:
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            
            keyIndex += 1  # Przejście do następnej litery klucza
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Dołączenie zanku bez jego wcześniejszego szyfrowania i deszyfrowania:
            translated.append(symbol)
    
    return ''.join(translated)


# Jeżeli program vigenereCipher.py został uruchomiony(a nie zaimportowany 
# jako moduł), należy wywołać funkcje main()
if __name__ == '__main__':
    main()