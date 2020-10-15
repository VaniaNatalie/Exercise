def convert(args):
    x = args.split(",")
    y = tuple(x)
    print("list: ",x)
    print("tuple: ",y)
    return x, y

def main(*args):
    args = input("input numbers separated by comma without space ")
    print(convert(args))

main()