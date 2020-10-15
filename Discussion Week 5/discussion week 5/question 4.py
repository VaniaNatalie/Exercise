def is_member(x, a):
    for i in range(len(a)):
        if x == a[i]:
            return True
    return False

def main():
    x = input("input character that want to be checked: ")
    list = input("input list ")
    a = list.split()
    print("the list is", a)
    print(is_member(x, a))

main()