from typing import List
from typing import Any
from dataclasses import dataclass
import json


@dataclass
class CourseSchedule:
    endDate: str
    campus: str
    days: str
    sectionCode: str
    startTime: str
    isExam: bool
    endTime: str
    startDate: str

    @staticmethod
    def from_dict(obj: Any) -> 'CourseSchedule':
        _endDate = str(obj.get("endDate"))
        _campus = str(obj.get("campus"))
        _days = str(obj.get("days"))
        _sectionCode = str(obj.get("sectionCode"))
        _startTime = str(obj.get("startTime"))
        _isExam = bool(obj.get("isExam"))
        _endTime = str(obj.get("endTime"))
        _startDate = str(obj.get("startDate"))
        return CourseSchedule(_endDate, _campus, _days, _sectionCode, _startTime, _isExam, _endTime, _startDate)


@dataclass
class Info:
    educationalGoals: str
    notes: str
    deliveryMethod: str
    description: str
    section: str
    units: str
    title: str
    type: str
    classNumber: str
    departmentalUgradNotes: str
    prerequisites: str
    number: str
    requiredReadingNotes: str
    registrarNotes: str
    outlinePath: str
    term: str
    requirements: str
    gradingNotes: str
    corequisites: str
    dept: str
    degreeLevel: str
    specialTopic: str
    courseDetails: str
    materials: str
    name: str
    designation: str

    @staticmethod
    def from_dict(obj: Any) -> 'Info':
        _educationalGoals = str(obj.get("educationalGoals"))
        _notes = str(obj.get("notes"))
        _deliveryMethod = str(obj.get("deliveryMethod"))
        _description = str(obj.get("description"))
        _section = str(obj.get("section"))
        _units = str(obj.get("units"))
        _title = str(obj.get("title"))
        _type = str(obj.get("type"))
        _classNumber = str(obj.get("classNumber"))
        _departmentalUgradNotes = str(obj.get("departmentalUgradNotes"))
        _prerequisites = str(obj.get("prerequisites"))
        _number = str(obj.get("number"))
        _requiredReadingNotes = str(obj.get("requiredReadingNotes"))
        _registrarNotes = str(obj.get("registrarNotes"))
        _outlinePath = str(obj.get("outlinePath"))
        _term = str(obj.get("term"))
        _requirements = str(obj.get("requirements"))
        _gradingNotes = str(obj.get("gradingNotes"))
        _corequisites = str(obj.get("corequisites"))
        _dept = str(obj.get("dept"))
        _degreeLevel = str(obj.get("degreeLevel"))
        _specialTopic = str(obj.get("specialTopic"))
        _courseDetails = str(obj.get("courseDetails"))
        _materials = str(obj.get("materials"))
        _name = str(obj.get("name"))
        _designation = str(obj.get("designation"))
        return Info(_educationalGoals, _notes, _deliveryMethod, _description, _section, _units, _title, _type, _classNumber, _departmentalUgradNotes, _prerequisites, _number, _requiredReadingNotes, _registrarNotes, _outlinePath, _term, _requirements, _gradingNotes, _corequisites, _dept, _degreeLevel, _specialTopic, _courseDetails, _materials, _name, _designation)


@dataclass
class Instructor:
    profileUrl: str
    commonName: str
    firstName: str
    lastName: str
    phone: str
    roleCode: str
    name: str
    officeHours: str
    office: str
    email: str

    @staticmethod
    def from_dict(obj: Any) -> 'Instructor':
        _profileUrl = str(obj.get("profileUrl"))
        _commonName = str(obj.get("commonName"))
        _firstName = str(obj.get("firstName"))
        _lastName = str(obj.get("lastName"))
        _phone = str(obj.get("phone"))
        _roleCode = str(obj.get("roleCode"))
        _name = str(obj.get("name"))
        _officeHours = str(obj.get("officeHours"))
        _office = str(obj.get("office"))
        _email = str(obj.get("email"))
        return Instructor(_profileUrl, _commonName, _firstName, _lastName, _phone, _roleCode, _name, _officeHours, _office, _email)


@dataclass
class RequiredText:
    details: str

    @staticmethod
    def from_dict(obj: Any) -> 'RequiredText':
        _details = str(obj.get("details"))
        return RequiredText(_details)


@dataclass
class Section:
    info: Info
    instructor: List[Instructor]
    courseSchedule: List[CourseSchedule]
    requiredText: List[RequiredText]

    @staticmethod
    def from_dict(obj: Any) -> 'Section':
        _info = Info.from_dict(obj.get("info"))
        _instructor = [Instructor.from_dict(y) for y in obj.get(
            "instructor")] if obj.get("instructor") is not None else []
        _courseSchedule = [CourseSchedule.from_dict(y) for y in obj.get(
            "courseSchedule")] if obj.get("courseSchedule") is not None else []
        _requiredText = [RequiredText.from_dict(y) for y in obj.get(
            "requiredText")] if obj.get("requiredText") is not None else []
        return Section(_info, _instructor, _courseSchedule, _requiredText)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
