def pangram_checker(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabets:
        if i not in sentence:
            return False
    return True

def main():
    sentence = str(input("Input sentence here: "))
    sentence = sentence.lower()
    print(pangram_checker(sentence))

main()