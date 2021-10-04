# Program wykorzystujący szyfr afiniczny:
# https://wwww.nostarch.com/crackingcodes/ (na licencji BSD)

import sys, pyperclip, cryptomath, random
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def main():
    myMessage = """A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    myKey = 2894
    myMode = 'szyfrowanie'  # Przypisanie wartości 'szyfrowanie' lub 'deszyfrowanie'

    if myMode == 'szyfrowanie':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'deszyfrowanie':
        translated = decryptMessage(myKey, myMessage)
    print('Klucz: %s' % (myKey))
    print('%s tekstu: ' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Pełne %s zakończone skopiowaniem tekstu do schowka.' % (myMode))


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return(keyA, keyB)


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'szyfrowanie':
        sys.exit('Szyfr jest słaby gdy kluczem A jest 1. Wybierz inny klucz.')
    if keyB == 0 and mode == 'szyfrowanie':
        sys.exit('Szyfr jest słaby gdy kluczem B jest 0. Wybierz inny klucz.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Klucz A musi być większy od 0 zaś klucz B musi być z przedziału od 0 do %s' % (len(SYMBOLS) - 1))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Klucz A %s i wielkość zbioru znaków (%s) nie są liczbami względnie pierszymi. Wybierz inny klucz' % (keyA, len(SYMBOLS)))


def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'szyfrowanie')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # Szyfrowanie znaku
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol  # Dołączenie znaku bez jego szyfrowania
    return ciphertext


def decryptMessage(key, message):
    keyA , keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'deszyfrowanie')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # Deszyfrowanie klucza
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol  # Dołączenie znaku bez jego deszyfrowania
    return plaintext


def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


# Jeżeli program affineCipher.py został uruchomiony(a nie
# zaimportowany jako moduł) należy wywołać funkcje main()
if __name__ == '__main__':
    main()