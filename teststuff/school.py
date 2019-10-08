class Student:
    classes = []
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def classInfo(self, dict, classname):
        return dict[classname].name

class Class:
    students = []
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def studentInfo(self, dict, studentname):
        return dict[studentname].name

calc = Class("AP Calculus AB", ["Jackson", "Jeff", "Winston"])
eng = Class("AP English", ["Jackson", "Jeff", "Winston"])

Jackson = Student("Jackson Zou", ["eng","calc"])
Jeff = Student("Jeff Lin", ["eng","calc"])
Winston = Student("Winston Peng", ["eng","calc"])

classdict = {"calc":calc, "eng":eng}
studentdict = {"Jackson":Jackson, "Jeff":Jeff, "Winston":Winston}

print(classdict,"\n")
print(studentdict,"\n")
print(studentdict["Jeff"].classInfo(classdict,"calc"))
print(classdict["eng"].studentInfo(studentdict,"Jackson"))
