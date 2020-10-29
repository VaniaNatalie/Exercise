def wordfrequencies(mylist):
    wordcounter = {}
    for word in mylist:
        if word not in wordcounter.keys():
            wordcounter[word] = 1
        elif word in wordcounter.keys():
            wordcounter[word] += 1
    return wordcounter

if __name__ == "__main__":
    mylist = [str(x) for x in input("Enter a sentence / words: ").split(" ")]
    print(wordfrequencies((mylist)))