# Ten program potwierdza że liczba kluczy dla szyfru afinicznego
# jest ograniczona do wartości mniejszej niż len(SYMBOLS) ^ 2 - len(SYMBOLS) to ilość elementów w zbiorze znaków dla których obsługiwane jest szyfrowanie.

import affineCipher, cryptomath

message = 'Wszystko powinno się konstruować w sposób możliwie najprostszy, ale nie uproszczony.'
for keyA in range(2, 80):
    key = keyA * len(affineCipher.SYMBOLS) + 1

    if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key, message))