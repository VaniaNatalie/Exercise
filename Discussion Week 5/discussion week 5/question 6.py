def converter(histogram):
    for i in histogram:
        a = print('*' * i)
    return a

def main():
    histogram = [int(x) for x in input("Input numbers: ").split()]
    print(histogram)
    converter(histogram)

main()