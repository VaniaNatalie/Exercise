def counter(list1):
    list2 = []
    for i in range(len(list1)):
        list2.append(len(list1[i]))
    return list2

def main():
    list1 = [str(x) for x in input("Enter your words here: ").split()]
    print("The list of words is: ", list1)
    print("The number of words is: ", counter(list1))

main()
