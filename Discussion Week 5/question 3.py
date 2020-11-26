import calendar

def main():
    year = int(input("input year "))
    month = int(input("input month "))
    print(calendar.month(year, month, w=0, l=0 ))

main()
