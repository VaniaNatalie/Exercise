def check(list1, list2):
    for i in list1:
        for v in list2:
            if i==v:
                return True
    return False

def main():
    a = input("input numbers for list 1: ")
    list1 = a.split()
    print("list 1:", list1)
    b = input("input number for list 2: ")
    list2 = b.split()
    print("list 2: ", list2)
    print(check(list1,list2))

main()