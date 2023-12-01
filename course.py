from typing import List


class Course:
    def __init__(self, subject: str, number: str):
        self.subject = subject
        self.number = number

class CourseGroup:
    def __init__(self, name: str, courses: List[Course]):
        self.name = name
        self.courses = courses
