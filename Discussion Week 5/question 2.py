def translate(sentence):
    new_sentence = ""
    for c in sentence:
        new_sentence+=c
        if c not in 'aeiou ':
            new_sentence+= 'o'+c
    return new_sentence

def main():
    sentence = str(input("type your sentence here "))
    print(translate(sentence))

main()
