# Łamanie szyfru przestawieniowego
# https://www.nostarch.com/crackingcodes/ (na licencji BSD)

import pyperclip, detectEnglish, transpositionDecrypt

def main():
    # Ten tekst możesz skopiować i wkleić z pliku kodu źródłowego któty znajdziesz na stronie
    # https://www.nostarch.com/crackingcodes/:
    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""
    
    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Deszyfrowanie zakończyło się niepowodzeniem.')
    else:
        print('Deszyfrowana wiadomość została skopiowana do schowka:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)


def hackTransposition(message):
    print('Łamanie szyfru...')

    # Program Pythona można zatrzymać w dowolnym momencie przez naciśnięcie klawiszy
    # Ctrl+C(Windows) lub Ctrl+D(macOS i Linux):
    print('Naciśnij klawisze Ctrl+C(Windows) lub Ctrl+D(macOS i Linux), aby w dowolnym momencie zakończyć działanie programu.')

    # Podejście typu brute force, które w tym programie oznacza iterację przez wszystkie możliwe klucze
    for key in range(1, len(message)):
        print('Sprawdzanie klucza %s...' % key)

        decryptedText = transpositionDecrypt.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            # Użytkownik powinien potwierdzić czy tekst został deszyfrowany prawidłowo
            print()
            print('Potencjalnie udane złamanie szyfru:')
            print('Klucz %s: %s' % (key, decryptedText[:100]))
            print()
            print('Wpisz \'D\', aby zakończyć. Dowolny inny klawisz kontynuuje łamanie szyfru:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == '__main__':
    main()