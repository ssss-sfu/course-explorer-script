from typing import List
from term import get_current_term
from course import Course
from sosy_requirements import software_systems_requirements
from section import Section
import requests
import json
import dataclasses

BASE_URL = "http://www.sfu.ca/bin/wcm/course-outlines"
RESULT_FILE_PATH = "result/courses.json"


def get_all_sections_info(course: Course, term=get_current_term()) -> List[Section]:
    season = term.season.value
    year = term.year
    course_url = f"{BASE_URL}?{year}/{season}/{course.subject}/{course.number}"
    course_res = requests.get(course_url)
    if (course_res.status_code == 404):
        # Recurse to previous season until we get info
        return get_all_sections_info(course, term.previous_term())

    # Status Code here is 200 OK
    course_json = json.loads(course_res.text)
    sections: List[Section] = []
    for section in course_json:
        section_value = section['value']
        section_url = f"{course_url}/{section_value}"
        section_res = requests.get(section_url)
        section_json = json.loads(section_res.text)
        sections.append(Section.from_dict(section_json))
    return sections


json_result = []

for courseGroup in software_systems_requirements:
    course_info_list = []
    for course in courseGroup.courses:
        print("Fetching - ", course.subject, course.number)
        sections = get_all_sections_info(course)
        print("Success! section length -", len(sections), "\n")
        course_info_list.append([dataclasses.asdict(section) for section in sections])
    
    # print("LENGTH" ,course.subject, course.number, course_info_list.length);

    json_result.append(
        {
            "requirement": courseGroup.name,
            "courses": course_info_list
        }
    )

print("Json result filled successfully!")

with open(RESULT_FILE_PATH, 'w') as f:
    json.dump(json_result, f, indent=4)

print(f"Successfully written to {RESULT_FILE_PATH}")