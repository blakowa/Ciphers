# Moduł crypthomath:
# https://www.nostarch.com/crackingcodes/ (na licencji BSD)

def gcd(a, b):
    # Zwraca największy wspólny dzielnik liczby a i b obliczony za pomocą algorytmu Euklidesa
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Zwraca odwrotność modularną a % m, gdzie
    # dla liczby x jest spełniony warunek a * x % m = 1

    if gcd(a, m) != 1:
        return None  # Brak odwrotności modularnej, jeśli a & m nie są liczbami względnie pierwszymi

    # Obliczenia wykorzystujące rozszeżony algorytm Euklidesa
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # Zwróć uwagę że // to operator dzielenia całkowitego
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m