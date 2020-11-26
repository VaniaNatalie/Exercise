def find_longest_words(lwords):
    lwords.sort(key= len)
    return lwords[-1]

def main():
    lwords = [str(x) for x in input("Enter words here: ").split()]
    print(lwords)
    print(find_longest_words(lwords))

main()
