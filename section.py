import json
from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class CourseSchedule:
    campus: str
    days: str
    sectionCode: str
    startTime: str
    endTime: str

    @staticmethod
    def from_dict(obj: Any) -> 'CourseSchedule':
        _campus = str(obj.get("campus"))
        _days = str(obj.get("days"))
        _sectionCode = str(obj.get("sectionCode"))
        _startTime = str(obj.get("startTime"))
        _endTime = str(obj.get("endTime"))
        return CourseSchedule(_campus, _days, _sectionCode, _startTime, _endTime)

@dataclass
class SectionInfo:
    section: str
    classNumber: str
    type: str

    @staticmethod
    def from_dict(obj: Any) -> 'Info':
        _section = str(obj.get("section"))
        _classNumber = str(obj.get("classNumber"))
        _type = str(obj.get("type"))
        return SectionInfo(_section, _classNumber, _type)

@dataclass
class CourseInfo:
    name: str
    title: str
    description: str
    term: str
    dept: str
    number: str
    prerequisites: str
    corequisites: str
    notes: str
    deliveryMethod: str
    units: str

    @staticmethod
    def from_dict(obj: Any) -> 'CourseInfo':
        _name = str(obj.get("name"))
        _title = str(obj.get("title"))
        _description = str(obj.get("description"))
        _term = str(obj.get("term"))
        _dept = str(obj.get("dept"))
        _number = str(obj.get("number"))
        _prerequisites = str(obj.get("prerequisites"))
        _corequisites = str(obj.get("corequisites"))
        _notes = str(obj.get("notes"))
        _deliveryMethod = str(obj.get("deliveryMethod"))
        _units = str(obj.get("units"))
        return CourseInfo(_name, _title, _description, _term, _dept, _number, _prerequisites, _corequisites, _notes, _deliveryMethod, _units)

@dataclass
class RequiredText:
    details: str

    @staticmethod
    def from_dict(obj: Any) -> 'RequiredText':
        _details = str(obj.get("details"))
        return RequiredText(_details)


@dataclass
class Section:
    info: SectionInfo
    instructorNames: List[str]
    courseSchedule: List[CourseSchedule]

    @staticmethod
    def from_dict(obj: Any) -> 'Section':
        _info = SectionInfo.from_dict(obj.get("info"))
        _instructorNames = [instructor.get("name") for instructor in obj.get(
            "instructor")] if obj.get("instructor") is not None else []
        _courseSchedule = [CourseSchedule.from_dict(y) for y in obj.get(
            "courseSchedule")] if obj.get("courseSchedule") is not None else []
        return Section(_info, _instructorNames, _courseSchedule)

@dataclass
class Course:
    info: CourseInfo
    sections: List[Section]
