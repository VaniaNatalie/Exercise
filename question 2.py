student1 = input("the score of student 1 is ")
student2 = input("the score of student 2 is ")
student3 = input("the score of student 3 is ")
print("Student scores:", end="\n")
print(float(student1), end="\n")
print(float(student2), end="\n")
print(float(student3))
average = (float(student1)+float(student2)+float(student3))/3
print("Average: ", average)