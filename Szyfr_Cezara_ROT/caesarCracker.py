# Łamanie szyfru Cezara


message = 'qeFIP?eGSeECNNS'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Iteracja przez wszystkie możliwe klucze:
for key in range(len(SYMBOLS)):
    # Bardzo ważne jest przypisanie pustego ciągu do zmiennej 
    # translated aby usunąć wartość zmiennej przypisaną w poprzedniej iteracji:
    translated = ''

    # Pozostała część programu jest niemalże identyczna jak w programie wykorzystującym szyfr Cezara:

    # Iteracja przez wszystkie symbole w zmiennej message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Obsługa zawinięcia:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

        # Dołączenie odszyfrowanego symbolu:
        translated = translated + SYMBOLS[translatedIndex]

    else:
        # Dołączenie symbolu bez jego deszyfracji:
        translated = translated + symbol

    # Wyświetlenie wszystkich możliwych danych wyjściowych:
    print('Klucz #%s: %s' % (key,translated))