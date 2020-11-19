import pathlib
pathlib.Path.cwd() #current working directory

def hapax(file_split, wordcounter):
    for words in file_split:
        if words not in wordcounter.keys():
            wordcounter[words] = 1
        elif words in wordcounter.keys():
            wordcounter[words] += 1
    return wordcounter

def hapax_filter(wordcounter):
    for key, val in wordcounter.items():
        if val == 1:
            print(key)

if __name__ == "__main__":
    file = open("ebook.txt")
    file = file.read().lower()
    wordcounter={}
    punctuations = ['.', ',', '?', '!', ';', ':', '"', '”', '-', '/', '(', ')', 'â€']
    for punctuation in punctuations:
        file = file.replace(punctuation, "")
    file_split = [str(x) for x in file.split()]
    hapax(file_split, wordcounter)
    hapax_filter(wordcounter)
