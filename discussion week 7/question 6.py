def decoder(sentence_split):
    sentence_decoded = ''
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x',
           'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i',
           'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T',
           'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E',
           'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    for i in sentence_split:
        if i in key.keys():
            sentence_decoded += key[i]
        elif i not in key.keys():
            sentence_decoded += i
    return sentence_decoded

if __name__ == "__main__":
    sentence_split = []
    sentence = str(input("Input the sentence you want to decode: "))
    for i in sentence:
        sentence_split.append(i)
    print(decoder(sentence_split))