def char_freq(character):
    freq = {}
    for i in character:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq

def main():
    character = str(input("Enter character here: "))
    print(char_freq())

main()