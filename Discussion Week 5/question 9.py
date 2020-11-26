def filter_long_words(lwords, n):
    filtered = []
    for i in range(len(lwords)):
        if len(lwords[i]) > n:
            filtered.append(lwords[i])
    return filtered

def main():
    lwords = [str(x) for x in input("Enter words here: ").split()]
    print(lwords)
    n = int(input("Input integer: "))
    print(filter_long_words(lwords, n))

main()
