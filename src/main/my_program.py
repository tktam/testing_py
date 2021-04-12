

def main_prog():
    m = input("Please enter the total number of students: \n")
    student_list = []
    grade_list = []
    module_list = []
    for i in range(int(m)):
        student = STUDENT()
        student.set_asset('{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                          , '{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                          , '{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                          )
        student_list.append(student)
        grade_list.append(int(student.grade))
        tmp_module = student.max_complex().module
        module_list.append(tmp_module)
    max_grade_value = max(grade_list)
    max_module = max(module_list)
    print("The student with highest score is: {0}, score at {1}"
          .format(student_list[grade_list.index(max_grade_value)].id
                  , max_grade_value))
    print("The student has largest complex module is: {0}, its' value is {1}"
          .format(student_list[module_list.index(max_module)].id
                  , max_module))
