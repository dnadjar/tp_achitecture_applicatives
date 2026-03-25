from collections.abc import Iterable, Iterator

class Student:
    def __init__(self, name: str, m1: float, m2: float, m3: float):
        self.name = name
        self.grades = [m1, m2, m3]

    def __str__(self):
        return f"{self.name} (M1: {self.grades[0]})"

class Matter1Iterator(Iterator):
    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grades[0], reverse=True)
        self._index = 0

    def __next__(self):
        try:
            student = self._students[self._index]
        except IndexError:
            raise StopIteration
        self._index += 1
        return student

class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __iter__(self) -> Iterator:
        return Matter1Iterator(self.students)

if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("Parcours:")
    for student in school_class:
        print(student)
