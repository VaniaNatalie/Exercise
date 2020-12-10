class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = str(address)

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = str(address)

    def __str__(self):
        return self.name + "(" + self.address + ")"


class Student(Person):
    numOfCourses = 0
    grade = []
    course = []

    def __init(self, name, address):
        super().__init__(name, address)

    def addCourseGrade(self, courses: list, grades: list):
        for i in grades:
            self.grade.append(i)
        for i in courses:
            self.course.append(i)
            self.numOfCourses += 1

    def printGrades(self):
        for i in range(len(self.course)):
            for j in range(len(self.grade)):
                if i == j:
                    print(f'{self.course[i]} : {self.grade[j]}')

    def getAverageGrade(self):
        return sum(self.grade) / self.numOfCourses

    def __str__(self):
        return self.name + "(" + self.address + ")"


class Teacher(Person):
    numOfCourses = 0
    course = []

    def __init__(self, name, address):
        super().__init__(name, address)

    def addCourse(self, courses: list):
        for i in courses:
            if i not in self.course:
                self.course.append(i)
                self.numOfCourses += 1
            else:
                return False

    def removeCourse(self, courses: list):
        for i in courses:
            if i in self.course:
                self.course.remove(i)
            else:
                return False

    def printCourse(self):
        print(*self.course)

    def __str__(self):
        return self.name + "(" + self.address + ")"


def studentMenu():
    return int(input("What do you want to do?\n1. Add course and grades\n2. Print grades\n"
                     "3. Average grade\n4. Back\n>>> "))


def teacherMenu():
    return int(input("What do you want to do?\n1. Add course\n2. Remove course\n"
                     "3. Print course\n4. Back\n>>> "))


def main():
    ans = int(input("Are you a student or teacher? (1 or 2)\n1. Student\n2. Teacher\n3. Quit\n>>> "))
    while ans != 3:
        if ans == 1:
            name = str(input("Input your name: "))
            address = str(input("Input your address: "))
            student = Student(name, address)
            print(student)
            ansStudent = studentMenu()
            while 0 < ansStudent < 4:
                if ansStudent == 1:
                    course = [str(x) for x in input("Input your courses in order: ").split()]
                    grade = [int(x) for x in input("Input your grades in order: ").split()]
                    student.addCourseGrade(course, grade)
                    ansStudent = studentMenu()
                elif ansStudent == 2:
                    student.printGrades()
                    ansStudent = studentMenu()
                elif ansStudent == 3:
                    print(student.getAverageGrade())
                    ansStudent = studentMenu()
            ans = int(input("Are you a student or teacher? (1 or 2)\n1. Student\n2. Teacher\n3. Quit\n>>> "))
        elif ans == 2:
            name = str(input("Input your name: "))
            address = str(input("Input your address: "))
            teacher = Teacher(name, address)
            print(teacher)
            ansTeacher = teacherMenu()
            while 0 < ansTeacher < 4:
                if ansTeacher == 1:
                    course = [str(x) for x in input("Input courses: ").split()]
                    teacher.addCourse(course)
                    ansTeacher = teacherMenu()
                elif ansTeacher == 2:
                    course = [str(x) for x in input("Input courses to be removed: ").split()]
                    teacher.removeCourse(course)
                    ansTeacher = teacherMenu()
                elif ansTeacher == 3:
                    teacher.printCourse()
                    ansTeacher = teacherMenu()
            ans = int(input("Are you a student or a teacher? (1 or 2)?\n1. Student\n2. Teacher\n3. Quit\n>>> "))
    print("Thanks!")


if __name__ == "__main__":
    main()
