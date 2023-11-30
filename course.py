from typing import List


class Course:
    def __init__(self, subject: str, number: str):
        self.subject = subject
        self.number = number

class CourseInfo:
    def __init__(self, course: Course, title: str, description: str):
        self.course = course
        self.title = title
        self.description = description

    def toJson(self):
        return {
            "subject": self.course.subject,
            "number": self.course.number,
            "title": self.title,
            "description": self.description
        }

class CourseGroup:
    def __init__(self, name: str, courses: List[Course]):
        self.name = name
        self.courses = courses
