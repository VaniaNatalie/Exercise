def makeForms(verb):
    suffix2 = ('o', 's', 'x', 'z', 'ch', 'sh')
    if verb.endswith('y'):
        if True:
            verb = verb[:-1]
            a = verb + 'ies'
            return a
    elif verb.endswith(suffix2):
        if True:
            b = verb + 'es'
            return b
    else:
        verb += 's'
        return verb

def main():
    verb = input("Input word: ")
    print(makeForms(verb))

main()