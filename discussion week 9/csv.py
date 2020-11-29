import datetime


def StepsPerDate(dict, NAlist, Intervaldict):
    for line in range(1, len(file)):
        temp = file[line].split(",")
        if len(temp) == 1: break
        if temp[1] in dict:
            if temp[0] != "NA":
                dict[temp[1]][0] += int(temp[0])
        else:
            if temp[0] != "NA":
                dict[temp[1]] = [0]
                dict[temp[1]][0] = int(temp[0])
            elif temp[0] == "NA":
                if temp[1] not in NAlist:
                    NAlist.append(temp[1])
        if temp[1] in Intervaldict:
            Intervaldict[temp[1]] += 1
        else:
            Intervaldict[temp[1]] = 1
    print("Dates with steps:", dict)
    print("Dates with no steps:", NAlist)
    print("Number of rows: ", Intervaldict)
    print("The number of rows are all the same")


def MeanMedian(dict, days, steps):
    dictKeys_list = list(dict)
    for i in dict.keys():
        days += 1
    for i in dict.values():
        num = i[0]
        steps += int(num)
    print("The total mean is:", steps / days)
    if days % 2 == 0:
        median = days // 2
        print("The median is:", dictKeys_list[median - 1])  # -1 because index starts from 0
    else:
        median = (days + 1) // 2
        print("The median is:", dictKeys_list[median - 1])


def date():
    dict = {}
    dict2 = {'Weekend': '', 'Weekday': ''}
    for line in range(1, len(file)):
        temp = file[line].split(",")
        if len(temp) == 1: break
        if temp[1] in dict:
            date = [int(x) for x in temp[1].split("-")]
            dates = datetime.date(date[0], date[1], date[2])
            dict[temp[1]] = dates.weekday()
        elif temp[1] not in dict:
            dict[temp[1]] = 0
    for key, val in dict.items():
        if val <= 5:
            dict2['Weekday'] += ', ' + key
        elif val > 5:
            dict2['Weekend'] += ', ' + key
    print(dict2)


def replace(NAlist):
    NAdict = {}
    for i in NAlist:
        NAdict[i] = 0
    print("NA:", NAdict)
    y = str(input("Do you want to replace any value (y/n)? "))
    while y == "y":
        index = int(input("Which date do you want to replace (0-7)? "))
        value = int(input("What is the number of steps? "))
        key = NAlist[index]
        NAdict[key] = value
        print("New NA:", NAdict)
        y = str(input("Do you want to replace any other value (y/n)? "))


if __name__ == "__main__":
    with open("csvexercise.csv", "r") as f:
        file = f.read()
    file = file.split("\n")
    dict = {}
    Intervaldict = {}
    NAlist = []
    totalDays = 0
    totalSteps = 0
    print("Total steps per date and list of dates with no steps:")
    StepsPerDate(dict, NAlist, Intervaldict)
    print("")
    print("Mean and median:")
    MeanMedian(dict, totalDays, totalSteps)
    print("")
    print("Weekend or weekdays:")
    date()
    print("")
    print("Replacing NA values:")
    replace(NAlist)
