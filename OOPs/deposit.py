class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

s1 = Student("Ravi", 85)

print(s1.get_marks())
s1.set_marks(95)
print(s1.get_marks())