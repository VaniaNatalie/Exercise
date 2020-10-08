print("Image height calculator")
def calc_new_height():
    width = float(input("Enter current width: "))
    height = float(input("Enter current height: "))
    new_width = float(input("Enter desired width: "))
    new_height = float(new_width/width)*float(height)
    print("The corresponding height is", float(new_height))

calc_new_height()