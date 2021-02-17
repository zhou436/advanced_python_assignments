

class Person(object):
    def __init__(self, First_name, Last_name):
        self.First_name = First_name
        self.Last_name = Last_name

    def fullName(self):
        self.full_name = self.First_name + ' ' + self.Last_name
        return self.full_name

class Student(Person):
    def __init__(self, First_name, Last_name, subject):
        Person.__init__(self, First_name, Last_name)
        self.subject = subject

    def printNameSubject(self):
        print(Person.fullName(self) + ', ' + self.subject)

class Teacher(Person):
    def __init__(self, First_name, Last_name, course):
        Person.__init__(self, First_name, Last_name)
        self.course = course

    def printNameCourse(self):
        print(Person.fullName(self) + ', ' + self.course)
    