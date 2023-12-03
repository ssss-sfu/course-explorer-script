import json
from typing import List
from typing import Any
from dataclasses import dataclass

def convert_to_cleaned_days_list(day_str: str) -> dict[str, str]: 
    day_map = {
        "Mo": "Monday",
        "Tu": "Tuesday",
        "We": "Wednesday",
        "Th": "Thursday",
        "Fr": "Friday"
    }
    raw_day_list = day_str.split(", ")
    day_list = raw_day_list if raw_day_list[0] != "" else []
    days_mapped = list(map(lambda str: day_map[str], day_list))
    return days_mapped

@dataclass
class CourseSchedule:
    days: List[str]
    sectionCode: str
    startTime: str
    endTime: str

    @staticmethod
    def from_dict(obj: Any) -> 'CourseSchedule':
        _days = convert_to_cleaned_days_list(str(obj.get("days")))
        _sectionCode = str(obj.get("sectionCode"))
        _startTime = str(obj.get("startTime"))
        _endTime = str(obj.get("endTime"))
        return CourseSchedule(_days, _sectionCode, _startTime, _endTime)

@dataclass
class SectionInfo:
    section: str
    classNumber: str
    type: str
    campus: str
    instructorNames: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'SectionInfo':
        info = obj.get("info")
        _section = str(info.get("section")) if info is not None else ""
        _classNumber = str(info.get("classNumber")) if info is not None else ""
        _type = str(info.get("type")) if info is not None else ""

        course_schedule = obj.get("courseSchedule")[0] if isinstance(obj.get("courseSchedule"), list) else None
        _campus = str(course_schedule.get("campus")) if course_schedule is not None else "" 
        ## campus on 1 section is always the same, so move it to sectionInfo from ClassSchedule

        instructors = obj.get("instructor")
        _instructorNames = [str(instructor.get("name")) for instructor in instructors] if instructors is not None else []
        return SectionInfo(_section, _classNumber, _type, _campus, _instructorNames)

@dataclass
class CourseInfo:
    dept: str
    number: str
    title: str
    description: str
    prerequisites: str
    corequisites: str
    notes: str
    deliveryMethod: str
    units: str

    @staticmethod
    def from_dict(obj: Any) -> 'CourseInfo':
        _dept = str(obj.get("dept"))
        _number = str(obj.get("number"))
        _title = str(obj.get("title"))
        _description = str(obj.get("description"))
        _prerequisites = str(obj.get("prerequisites"))
        _corequisites = str(obj.get("corequisites"))
        _notes = str(obj.get("notes"))
        _deliveryMethod = str(obj.get("deliveryMethod"))
        _units = str(obj.get("units"))
        return CourseInfo( _dept, _number, _title, _description, _prerequisites, _corequisites, _notes, _deliveryMethod, _units)

@dataclass
class Section:
    info: SectionInfo
    courseSchedule: List[CourseSchedule]

    @staticmethod
    def from_dict(obj: Any) -> 'Section':
        _info = SectionInfo.from_dict(obj)
        _courseSchedule = [CourseSchedule.from_dict(y) for y in obj.get(
            "courseSchedule")] if obj.get("courseSchedule") is not None else []
        return Section(_info, _courseSchedule)

@dataclass
class SectionsPerTerm:
    term: str
    sections: List[Section]

@dataclass
class Course:
    info: CourseInfo
    future_sections: SectionsPerTerm
    last_sections: SectionsPerTerm
