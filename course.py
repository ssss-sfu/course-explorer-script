from typing import List


class CourseName:
    def __init__(self, subject: str, number: str):
        self.subject = subject
        self.number = number

class CourseGroup:
    def __init__(self, name: str, courses: List[CourseName]):
        self.name = name
        self.courses = courses
