class Student:
    def __init__(self, name: str, m1: float, m2: float, m3: float):
        self.name = name
        self.grades = [m1, m2, m3]

    def get_average(self) -> float:
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} (M1: {self.grades[0]}, M2: {self.grades[1]}, M3: {self.grades[2]}, Moyenne: {self.get_average():.2f})"

class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def rank_matter_1(self):
        sorted_students = sorted(self.students, key=lambda s: s.grades[0], reverse=True)
        print("\nClassement Matière 1 :")
        for student in sorted_students:
            print(student)

    def rank_matter_2(self):
        sorted_students = sorted(self.students, key=lambda s: s.grades[1], reverse=True)
        print("\nClassement Matière 2 :")
        for student in sorted_students:
            print(student)

    def rank_matter_3(self):
        sorted_students = sorted(self.students, key=lambda s: s.grades[2], reverse=True)
        print("\nClassement Matière 3 :")
        for student in sorted_students:
            print(student)

if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    school_class.rank_matter_1()
    school_class.rank_matter_2()
    school_class.rank_matter_3()
