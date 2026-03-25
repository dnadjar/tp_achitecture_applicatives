from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Grade:
    subject: str
    value: float

class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades: List[Grade] = []

    def add_grade(self, subject: str, value: float):
        self.grades.append(Grade(subject, value))

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(g.value for g in self.grades) / len(self.grades)

    def get_grade_for_subject(self, subject: str) -> float:
        for g in self.grades:
            if g.subject == subject:
                return g.value
        return 0.0
