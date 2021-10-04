# Szyfrowanie i deszyfrowanie pilku tekstowego za pomocą szyfru przestawieniowego:
# https://nostarch.com/crackingcodes/ (na licencji BSD)

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFileName = 'F:\\Szyfry\\transpositionEncrypt\\frankenstein.encrypted.txt'
    # ZACHOWAJ OSTROŻNOŚĆ! Jeżeli plik wymieniony w zmiennej outputFilename
    # już istnieje ten program nadpiszę jego zawartość
    outputFilename = 'F:\\Szyfry\\transpositionEncrypt\\frankenstein.decrypted.txt'
    myKey = 10
    myMode = 'deszyfrowanie'  # Przypisanie wartości 'szyfrowanie' lub 'deszyfrowanie'

    # Jeżeli plik danych wejściowych nie istniej program zakończy działanie
    if not os.path.exists(inputFileName):
        print('Plik %s nie istnieje. Koniec pracy programu...' % (inputFileName))
        sys.exit()

    # Jeżeli plik danych wyjściowych już istnieje należy umożliwić urzytkownikowi zakończenie działania programu
    if os.path.exists(outputFilename):
        print('To spowoduje nadpisanie pliku %s. (K)ontynuować czy (Z)akończyć pracę?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('k'):
            sys.exit()
    
    # Odczyt tekstu z pliku danych wejściowych
    fileObj = open(inputFileName)
    content = fileObj.read()
    fileObj.close()

    print('%s...' % (myMode.title()))

    # Pomiar czsu operacji szyfrowania i deszyfrowania
    startTime = time.time()
    if myMode == 'szyfrowanie':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'deszyfrowanie':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%s trwało %s sekund.' % (myMode.title(), totalTime))

    # Zapisanie przetworzonego tekstu w pliku danych wyjściowych
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Zakończono %s pliku %s (%s znaki).' % (myMode, inputFileName, len(content)))
    print('%s wygenerowało plik %s' % (myMode.title(), outputFilename))

# Jeżeli program transpositionFileCypher.py zostal uruchomiony (a nie 
# importowany jako moduł) należy wywołać funkcje main()
if __name__ == '__main__':
    main()