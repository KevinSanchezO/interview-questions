'''
Checks if two words are anagram using dictionaries
'''
def anagram_(word1, word2):
    if (len(word1) != len(word2)):
        return False

    dictWord1 = check(word1)
    dictWord2 = check(word2)
    return dictWord1 == dictWord2

def check(word):
    dictWord = {}
    for a in word:
        if (not(a in dictWord)):
            dictWord[a] = 1
        else:
            dictWord[a] += dictWord[a] + 1
    return dictWord

'''
Checks if two words are anagram using only for loops
and counting the words
'''
def anagram(word1, word2):
    for i in word1:
        if countLetters(i, word1) != countLetters(i, word2):
            return False
    return True

def countLetters(letter, word):
    res = 0
    for i in word:
        if i == letter:
            res += 1
    return res

if __name__ == '__main__':
    a = 'clinteastwood'
    b = 'oldwestaction'
    print(anagram_(a, b))