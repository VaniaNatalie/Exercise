print("Total Students")
class1 = int(input("The number of students in Class A is "))
class2 = int(input("The number of students in Class B is "))
class3 = int(input("The number of students in Class C is "))

print("")
print("Total Groups")
group1 = int(input("The number of groups in Class A are "))
group2 = int(input("The number of groups in Class B are "))
group3 = int(input("The number of groups in Class C are "))

print("Number of students in each group:")
print("Class A:", class1 // group1)
print("Class B:", class2 // group2)
print("Class C:", class3 // group3)

print("")
print("Number of leftover students")
print("Class A: ", class1 % group1)
print("Class B: ", class2 % group2)
print("Class C: ", class3 % group3)