def kmers_counter (DNA, k):
    counter = {}
    #to determine how many times we go over the loop
    num_kmers = len(DNA) - k + 1
    for i in range(num_kmers):
        kmers = DNA[i:i+k]
        if kmers not in counter:
            counter[kmers] = 1
        elif kmers in counter:
            counter[kmers] += 1
    return counter

if __name__ == "__main__":
    DNA = str(input("Input your DNA here: "))
    k = int(input("Input the length of the substring (k): "))
    print(kmers_counter(DNA, k))