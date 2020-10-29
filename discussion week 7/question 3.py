def findvalue(mydict, val):
    keys = []
    for key,value in mydict.items():
        for i in val:
            if i == value:
                keys.append(key)
    return keys

if __name__ == "__main__":
    mydict = {}
    key_mydict = input("Enter the keys for the dictionary (separated by space): ").split(" ")
    values_mydict = input("Enter the corresponding values for the keys (separated by space): ").split(" ")
    for i in range(len(key_mydict)):
        mydict[key_mydict[i]] = values_mydict[i]
    val = input("Enter the values you want to map out (separate by space if there are multiple values): ").split(" ")
    print(findvalue(mydict, val))