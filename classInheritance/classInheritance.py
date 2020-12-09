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
        print(*self.course, *self.grade)  # print content of list

    def getAverageGrade(self):
        return sum(self.grade) / self.numOfCourses

    def __str__(self):
        return self.name + "(" + self.address + ")"


class Teacher(Person):
    numOfCourses = 0
    course = []

    def __init__(self, name, address):
        super().__init__(name, address)

    def addCourse(self, courses):
        for i in courses:
            if i not in self.course:
                self.course.append(i)
                self.numOfCourses += 1
            else:
                return False

    def removeCourse(self, courses):
        for i in courses:
            if i in self.course:
                self.course.pop(i)
            else:
                return False

    def __str__(self):
        return self.name + "(" + self.address + ")"
