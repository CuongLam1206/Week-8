class Ward:
    __listPerson = []
    def __init__(self,name):
        self.__name = name
    def addPerson(self, person):
        self.__listPerson.append(person)
    def describe(self):
        print(f"Ward Name: {self.__name}")
        for i in self.__listPerson:
            i.describe()

class Students:
    def __init__(self, name, yob, grade):
        self.__name = name
        self.__yob = yob
        self.__grade = grade
    def describe(self):
        print(f"Student - Name: {self.__name} - Yob: {self.__yob} - Grade: {self.__grade}")

class Doctors:
    def __init__(self,name, yob, specialist):
        self.__name = name
        self.__yob = yob
        self.__specialist = specialist
    def describe(self):
        print(f"Doctor - Name: {self.__name} - YoB: {self.__yob} - Specialist: {self.__specialist}")

class Teachers:
    def __init__(self, name, yob, subject):
        self.__name = name
        self.__yob = yob
        self.__subject = subject
    def describe(self):
        print(f"Teacher - Name: {self.__name} - YoB: {self.__yob} - Subject: {self.__subject}")

student1 = Students("studentA", 2010, "7")
student1.describe()
teacher1 = Teachers("teacherA", 1969, "Math")
teacher1.describe()
doctor1 = Doctors("doctorA", 1945, "Endocrinologists")
doctor1.describe()

print()
teacher2 = Teachers("teacherB", 1995, "History")
doctor2 = Doctors("doctorB", 1975, "Cardiologists")
ward1 = Ward(name="Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1.addPerson(doctor2)
ward1.describe()