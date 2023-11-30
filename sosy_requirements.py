from course import Course, CourseInfo, CourseGroup

# List of lower-division cores
lower_division_core = CourseGroup("Lower Divison Core", [
    Course("CMPT", "105W"),
    Course("CMPT", "130"),
    Course("CMPT", "135"),
    Course("CMPT", "210"),
    Course("CMPT", "213"),
    Course("CMPT", "225"),
    Course("CMPT", "276"),
    Course("CMPT", "295"),
    Course("MACM", "101"),
    Course("MSE", "110"),
    Course("STAT", "271"),
    Course("MATH", "150"),
    Course("MATH", "151"),
    Course("MATH", "152"),
    Course("MATH", "232"),
]
)
# Upper Division Core Requirements
upper_division_core = CourseGroup("Upper Divison Core", [
    Course("CMPT", "307"),
    Course("CMPT", "376W"),
]
)

# Systems Requirements
systems_requirements = CourseGroup("Systems Requirements", [
    Course("CMPT", "300"),
    Course("CMPT", "354"),
    Course("CMPT", "371"),
    Course("CMPT", "372"),
    Course("CMPT", "431"),
    Course("CMPT", "433"),
    Course("CMPT", "454"),
    Course("CMPT", "471"),
])

# Software Engineering Requirements
software_engineering_requirements = CourseGroup("Software Engineering Requirements", [
    Course("CMPT", "373"),
    Course("CMPT", "473"),
    Course("CMPT", "379"),
    Course("CMPT", "383"),
    Course("CMPT", "384"),
    Course("CMPT", "474"),
    Course("CMPT", "477"),
])

# Capstone Project Requirement
capstone_project = CourseGroup("Capstone Project Requirements", [
    Course("CMPT", "494"),
    Course("CMPT", "495"),
])

software_systems_requirements = [lower_division_core, upper_division_core, systems_requirements, software_engineering_requirements, capstone_project]