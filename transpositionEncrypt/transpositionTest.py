# Program do testowania innych programów:
# 

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42)  # Zedefiniowanie losowej wartości zalążka jako wartości statycznej

    for i in range(20):  # Przeprowadzenie 20 testów
        # Wygenerowanie losowej wartości do zaszyfrowania

        # Wiadomość będzie miała losową długość:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Konwersja ciągu tekstowego wiadomości na listę której elementy zostaną wymieszane:
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)  # Konwersja listy z powrotem na postać ciągu tekstowego

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Sprawdzenie wszystkich możliwych kluczy dla każdej wiadomości:
        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            # Jeżeli rozszyfrowana wiadomość jest inna niż pierwotna należy
            # wyświetlić komunikat błędu i zakończyć działanie programu:
            if message != decrypted:
                print('Niedopasowanie klucza %s i wiadomości %s.' % (key, message))
                print('Rozszyfrowana wiadomość: ' + decrypted)
                sys.exit()
    
    print('Test zastosowania szyfru przestawnego zosatał zaliczony.')


# Jeżeli program transpositionTest.py został uruchomiony ( a nie
# zaimportowany jako moduł), należy wywołać funkcje main():
if __name__ == '__main__':
    main()