print("Enter your height: ")
feet = int(input("Feet: "))
convertedfeet = int(feet) * 12 * 2.54
inches = int(input("Inches: "))
convertedinches = int(inches) * 2.54
print("Suggested board length ", (float(convertedfeet) + float(convertedinches)) * 88/100, "cm")