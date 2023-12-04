from typing import List
from term import get_current_term
from course_group import CourseName
from sosy_requirements import software_systems_requirements
from course import Section, Course, CourseInfo, SectionsPerTerm
import requests
import json
import dataclasses

BASE_URL = "http://www.sfu.ca/bin/wcm/course-outlines"
RESULT_FILE_PATH = "../../public/jsons/courses.json"

def get_course_info(course: CourseName, term=get_current_term()) -> CourseInfo:
    season = term.season.value
    year = term.year
    course_url = f"{BASE_URL}?{year}/{season}/{course.subject}/{course.number}"
    course_res = requests.get(course_url)
    if (course_res.status_code == 404):
        # Recurse to previous season until we get info
        return get_course_info(course, term.previous_term())

    # Status Code here is 200 OK
    course_json: List[any] = json.loads(course_res.text)
    first_section_value = course_json[0]['value']
    first_section_url = f"{course_url}/{first_section_value}"
    first_section_res = requests.get(first_section_url)
    first_section_json = json.loads(first_section_res.text)
    return CourseInfo.from_dict(first_section_json['info'])


def get_sections_info(course: CourseName, term=get_current_term(), continue_searching=True) -> SectionsPerTerm:
    season = term.season.value
    year = term.year
    course_url = f"{BASE_URL}?{year}/{season}/{course.subject}/{course.number}"
    course_res = requests.get(course_url)
    if (course_res.status_code == 404):
        # Recurse to previous season until we get info
        return get_sections_info(course, term.previous_term()) if continue_searching else SectionsPerTerm(str(term), [])

    # Status Code here is 200 OK
    course_json: List[any] = json.loads(course_res.text)

    sections: List[Section] = []
    for section in course_json:
        section_value = section['value']
        section_url = f"{course_url}/{section_value}"
        section_res = requests.get(section_url)
        section_json = json.loads(section_res.text)
        sections.append(Section.from_dict(section_json))
    
    return SectionsPerTerm(str(term), sections)

def get_course(course: CourseName, term=get_current_term()) -> Course:
    course_info = get_course_info(course)
    future_sections = get_sections_info(course, term.next_term(), continue_searching=False)
    last_sections = get_sections_info(course, term)
    return Course(course_info, future_sections, last_sections)


json_result = []

for courseGroup in software_systems_requirements:
    courses = []
    for course in courseGroup.courses:
        print("Fetching - ", course.subject, course.number)
        course_info = get_course(course)
        courses.append(dataclasses.asdict(course_info))

    json_result.append(
        {
            "requirement": courseGroup.name,
            "courses": courses
        }
    )

print("Json result filled successfully!")

with open(RESULT_FILE_PATH, 'w') as f:
    json.dump(json_result, f, indent=4)

print(f"Successfully written to {RESULT_FILE_PATH}!")
