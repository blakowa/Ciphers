# Łamanie szyfru afinicznego:
# https://www.nostarch.com/crackingcodes/ (na licencji BSD)

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():
    # Ten tekst możesz skopiować i wkleić z pliku kodu źródłowego, który znajdziesz na stronie:
    # www.nostarch.com/crackingcodes/
    myMessage = """"5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        # Deszyfrowana wiadomość została wyświetlona na ekranie; dla wygody
        # użytkownika jej tekst został również skopiowany do schowka
        print('Deszyfrowana wiadomość została skopiowana do schowka:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Deszyfrowanie zakończyło się niepowodzeniem.')


def hackAffine(message):
    print('Łamanie szyfru...')

    # Program Pythona można w dowolnym momencie zatrzymać poprzez naciśnięcie klawiszy
    # Ctrl+C(Windows) lub Ctrl+D(macOS i Linux)
    print('(Naciśnij klawisze Ctrl+C lub Ctrl+D, aby w dowolnym momencie zakończyć działanie programu.)')

    # Podejście typu brute force, które w tym programie oznacza iterację przez wszystkie możliwe klucze
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Sprawdzono klucz %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            # Użytkownik powinien potwierdzić, czy tekst został deszyfrowany prawidłowo
            print()
            print('Potencjalnie udane złamanie szyfru:')
            print('Klucz: %s' % (key))
            print('Deszyfrowanie wiadomości: ' + decryptedText[:200])
            print()
            print('Wpisz D, aby zakończyć. Dowolny inny klawisz kontynuje łamanie szyfru:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


# Jeżeli program affineHacker.py został uruchomiony (a nie
# zaimportowany jako moduł), należy wywołać funkcję main()
if __name__ == '__main__':
    main()