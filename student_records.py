class Student:
    def __init__(self, name: str, m1: float, m2: float, m3: float):
        self.name = name
        self.grades = [m1, m2, m3]

    def get_average(self) -> float:
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} (Moyenne: {self.get_average():.2f})"

class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))
