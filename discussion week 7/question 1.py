def removekeys(mydict, keylist):
    for i in keylist:
        if i in mydict:
            del mydict[i]
    return mydict

if __name__ == "__main__":
    key = input("Enter keys here (separated by space if many): ").split(" ")
    value = input("Enter values here (separated by space, make sure it is in order as the key): ").split(" ")
    mydict = {}
    for i in range(len(key)):
        mydict[key[i]] = value[i]
    keylist = input("Insert the keys you want to remove: ").split(" ")
    print(removekeys(mydict, keylist))