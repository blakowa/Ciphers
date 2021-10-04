"""for spam in ['mrównik afrykański', 'mrówkojad', 'bizon']:
    print('Oto dziś na obiad jeść będziemy ' + spam)


animals = ['mrównik afrykański', 'mrówkojad', 'bizon']
print(animals)
animals[2] = 99999
print(animals)

'Witaj, świecie'[7] = 'X'

spam = 'Witaj, świecie'
spam = spam[:7] + 'X' + spam[8:]
print(spam)

spam = [['pies', 'kot'], [1, 2, 3]]"""

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

wynik = gcd(409119243, 87780243)
print(wynik)

