from collections.abc import Iterable, Iterator

class Student:
    def __init__(self, name: str, m1: float, m2: float, m3: float):
        self.name = name
        self.grades = [m1, m2, m3]

    def __str__(self):
        return f"{self.name} (M1: {self.grades[0]}, M2: {self.grades[1]}, M3: {self.grades[2]})"

class Matter1Iterator(Iterator):
    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grades[0], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

class Matter2Iterator(Iterator):
    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grades[1], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

class Matter3Iterator(Iterator):
    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grades[2], reverse=True)
        self._index = 0

    def __next__(self):
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __iter__(self) -> Iterator:
        return Matter1Iterator(self.students)

    def iter_matter_2(self) -> Iterator:
        return Matter2Iterator(self.students)

    def iter_matter_3(self) -> Iterator:
        return Matter3Iterator(self.students)

if __name__ == '__main__':
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("Matière 1 (défaut) :")
    for s in school_class:
        print(s)

    print("\nMatière 2 :")
    for s in school_class.iter_matter_2():
        print(s)

    print("\nMatière 3 :")
    for s in school_class.iter_matter_3():
        print(s)
