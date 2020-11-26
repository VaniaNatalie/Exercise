def makeForming(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if word.endswith('ie'):
        if True:
            word = word[:-2]
            a = word + "ying"
            return a
    if word.endswith('e'):
        if True:
            word = word[:-1]
            b = word + "ing"
            return b
    if word[-1] not in vowels:
        if word[-2] in vowels:
            if word[-3] not in vowels:
                c = word + str(word[-1]) + "ing"
                return c
    return word += 'ing'

def main():
    word = input("Input word: ")
    print(makeForming(word))

main()
