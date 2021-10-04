#Szyfr Cezara


import pyperclip;

#Ciąg tekstowy do szyfrowania i deszyfrowywania:
message = 'XCBSw88S18A1S 2SB41SE .8zSEwAS50D5A5x81V'

#Klucz użyty do szyfrowania:
key = 22

#Określenie trybu pracy - szyfrowanie(encrypt) i deszyfrowanie(decrypt):
mode = 'decrypt'

#Znaki które można zaszyfrować:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#Zmienna przechowywująca zaszyfrowaną, bądź rozszyfrowaną postać wiadomości:
translated = ''

for symbol in message:
    #Tylko znaki zdefiniowane w ciągu tekstowym SYMBOLS mogą być szyfrowane i deszyfrowywane.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #Przeprowadzanie szyfrowania i deszyfrowywania:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        #Obsługa zawinięcia, jeżeli trzeba:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        #Dołączenie znaku bez wcześniejszego szyfrowania lub deszyfrowania:
        translated = translated + symbol

#Wyświetlenie skonwertowanego ciągu tekstowego:
print(translated)
pyperclip.copy(translated)