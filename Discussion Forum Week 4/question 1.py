print("Day Counter")
def get_days(second, minute, hour):
    q = (float(second/3600)+float(minute/60)+float(hour))/24
    return q
def convert_to_days():
    hour = int(input("Enter number of hours: "))
    minute = int(input("Enter number of minutes: "))
    second = int(input("Enter number of seconds: "))
    print(" ")
    print("It is", round(get_days(second, minute, hour), 4), "days")

convert_to_days()