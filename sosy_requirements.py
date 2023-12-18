from course_group import CourseName, CourseGroup

# List of lower-division cores
lower_division_core = CourseGroup("Lower Divison Core", [
    CourseName("CMPT", "105W"),
    CourseName("CMPT", "130"),
    CourseName("CMPT", "135"),
    CourseName("CMPT", "210"),
    CourseName("CMPT", "213"),
    CourseName("CMPT", "225"),
    CourseName("CMPT", "276"),
    CourseName("CMPT", "295"),
    CourseName("MACM", "101"),
    CourseName("MSE", "110"),
    CourseName("STAT", "271"),
    CourseName("MATH", "150"),
    CourseName("MATH", "151"),
    CourseName("MATH", "152"),
    CourseName("MATH", "232"),
]
)
# Upper Division Core Requirements
upper_division_core = CourseGroup("Upper Divison Core", [
    CourseName("CMPT", "307"),
    CourseName("CMPT", "376W"),
]
)

# Systems Requirements
systems_requirements = CourseGroup("Systems Requirements", [
    CourseName("CMPT", "300"),
    CourseName("CMPT", "354"),
    CourseName("CMPT", "371"),
    CourseName("CMPT", "372"),
    CourseName("CMPT", "431"),
    CourseName("CMPT", "433"),
    CourseName("CMPT", "454"),
    CourseName("CMPT", "471"),
])

# Software Engineering Requirements
software_engineering_requirements = CourseGroup("Software Engineering Requirements", [
    CourseName("CMPT", "373"),
    CourseName("CMPT", "473"),
    CourseName("CMPT", "379"),
    CourseName("CMPT", "383"),
    CourseName("CMPT", "384"),
    CourseName("CMPT", "474"),
    CourseName("CMPT", "477"),
])

# Capstone Project Requirement
capstone_project = CourseGroup("Capstone Project Requirements", [
    CourseName("CMPT", "494"),
    CourseName("CMPT", "495"),
])

other_cmpt_courses = CourseGroup("Other CMPT Courses", [
    CourseName("CMPT", "120"),
    CourseName("CMPT", "125"),
    # CourseName("CMPT", "263"),
    CourseName("CMPT", "276"),
    CourseName("CMPT", "305"),
    CourseName("CMPT", "308"),
    CourseName("CMPT", "310"),
    CourseName("CMPT", "340"),
    CourseName("CMPT", "353"),
    CourseName("CMPT", "361"),
    CourseName("CMPT", "362"),
    CourseName("CMPT", "363"),
    CourseName("CMPT", "365"),
    CourseName("CMPT", "403"),
    CourseName("CMPT", "404"),
    CourseName("CMPT", "405"),
    CourseName("CMPT", "410"),
    CourseName("CMPT", "411"),
    CourseName("CMPT", "412"),
    CourseName("CMPT", "413"),
    CourseName("CMPT", "417"),
    # CourseName("CMPT", "420"),
    CourseName("CMPT", "441"),
    CourseName("CMPT", "450"),
    CourseName("CMPT", "461"),
    CourseName("CMPT", "464"),
    CourseName("CMPT", "466"),
    # CourseName("CMPT", "467"),
    CourseName("CMPT", "475"),
    # CourseName("CMPT", "476")
    ])

software_systems_requirements = [lower_division_core, upper_division_core,
                                 systems_requirements, software_engineering_requirements, capstone_project, other_cmpt_courses]
