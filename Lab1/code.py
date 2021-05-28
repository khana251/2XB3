# Checks if group sizes are valid, and that all students in studentNumbers are in groups
# We assume that studentNumbers is a list of strings of student numbers
# Groups is assumed to be a list of integers, but could easily be converted utilizing the int function
# String comparison could then be used instead
def are_valid_groups(studentNumbers, groups):
    studentList = []
    for student in studentNumbers:
        for group in groups:
            if len(group) >3 or len(group) < 2:
                return False
            if int(student) in group:
                if int(student) in studentList:
                    return False
                studentList.append(int(student))

    # If loop completes we then ensure that all students have been counted to be in groups
    return len(studentList) == len(studentNumbers)

