from collections.abc import Iterable, Iterator

def add_fourth_matter(cls):
    original_init = cls.__init__
    def new_init(self, name, m1, m2, m3, m4=0):
        original_init(self, name, m1, m2, m3)
        self.grades.append(m4)
    cls.__init__ = new_init
    return cls

def add_matter4_iterator(cls):
    def iter_matter_4(self) -> Iterator:
        return Matter4Iterator(self.students)
    cls.iter_matter_4 = iter_matter_4
    return cls

@add_fourth_matter
class Student:
    def __init__(self, name: str, m1: float, m2: float, m3: float):
        self.name = name
        self.grades = [m1, m2, m3]

    def __str__(self):
        return f"{self.name} (Notes: {self.grades})"

class Matter1Iterator(Iterator):
    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grades[0], reverse=True)
        self._index = 0
    def __next__(self):
        if self._index >= len(self._students): raise StopIteration
        student = self._students[self._index]; self._index += 1
        return student

class Matter2Iterator(Iterator):
    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grades[1], reverse=True)
        self._index = 0
    def __next__(self):
        if self._index >= len(self._students): raise StopIteration
        student = self._students[self._index]; self._index += 1
        return student

class Matter3Iterator(Iterator):
    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grades[2], reverse=True)
        self._index = 0
    def __next__(self):
        if self._index >= len(self._students): raise StopIteration
        student = self._students[self._index]; self._index += 1
        return student

class Matter4Iterator(Iterator):
    def __init__(self, students: list):
        self._students = sorted(students, key=lambda s: s.grades[3], reverse=True)
        self._index = 0
    def __next__(self):
        if self._index >= len(self._students): raise StopIteration
        student = self._students[self._index]; self._index += 1
        return student

@add_matter4_iterator
class SchoolClass(Iterable):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SchoolClass, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'students'):
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
    s1 = SchoolClass()
    s2 = SchoolClass()

    print(f"Id instance 1: {id(s1)}")
    print(f"Id instance 2: {id(s2)}")
    
    s1.add_student(Student('J', 10, 12, 13, 15))
    s2.add_student(Student('A', 8, 2, 17, 11))
    s1.add_student(Student('V', 9, 14, 14, 18))

    print(f"\nNombre d'étudiants via s2: {len(s2.students)}")
    
    print("\nClassement Matière 4 via l'instance s2 :")
    for student in s2.iter_matter_4():
        print(student)
