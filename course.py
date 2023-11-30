from typing import List


class Course:
    def __init__(self, subject: str, number: str):
        self.subject = subject
        self.number = number

class CourseInfo:
    def __init__(self, course: Course, title: str):
        self.course = course
        self.title = title

    def toJson(self):
        return {
            "subject": self.course.subject,
            "number": self.course.number,
            "title": self.title
        }

class CourseGroup:
    def __init__(self, name: str, courses: List[Course]):
        self.name = name
        self.courses = courses
