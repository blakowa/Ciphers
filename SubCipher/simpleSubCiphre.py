# Prosty szyfr podstawieniowy:
# https://www.nostarch.com/crackingcodes/ (na licencji BSD)

import pyperclip, sys, random


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'szyfrowanie'  # Przypisanie wartości 'szyfrowanie' lub 'deszyfrowanie'

    if not keyIsValid(myKey):
        sys.exit('Wystąpił błąd w kluczu lub zbiorze znaków.')
    if myMode == 'szyfrowanie':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'deszyfrowanie':
        translated = decryptMessage(myKey, myMessage)
    print('Użyty klucz %s' % (myKey))
    print('%s tekstu:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('Wiadomość została skopiowana do schowka.')


def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList


def encryptMessage(key, message):
    return translatedMessage(key, message, 'szyfrowanie')


def decryptMessage(key, message):
    return translatedMessage(key, message, 'deszyfrowanie')


def translatedMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'deszyfrowanie':
        # Do szyfrowania można użyć tego samego kodu, wystarczy zamienić miescami
        # ciągi tekstowe klucza i stałej LETTERS
        charsA, charsB =charsB, charsA

    # Iteracja przez wszystkie znaki w zmiennej message
    for symbol in message:
        if symbol.upper() in charsA:
        # Szyfrowanie i deszyfrowanie znaku
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Znak nie znajduję się w stałej LETTERS, wystarczy go dodać bez zmian
            translated += symbol

    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()