# Moduł wykrywania języka angielskiego:
# https://www.nostarch.com/crackingcodes/ (na licencji BSD)

# Aby użyć tego programu, należy skorzystać z następujących poleceń:
#  import detectEnglish
#  detectEnglish.isEnglish(dowolnyCiągTekstowy) # Wartością zwrotną jest True lub False
# (W katalogu programu musi znajdować się plik o nazwie dictionary.txt zawierający
# słowa angielskie, po jednym w każdym wierszu; plik ten znajdziesz pod adresem
# https://invpy.com/dictionary.txt)
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('F:\\Szyfry\\detectEnglish\\dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()


def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == []:
        return 0.0  # Lista jest pusta, więc wartością zwrotną jest 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message, wordPercentage=20, letterPercentage=85):
    # Domyślnie 20% słów musi istnieć w pliku słownika.
    # a 85% wszystkich znaków musi być literami i spacjami
    # (nie znakami przestankowymi)
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch