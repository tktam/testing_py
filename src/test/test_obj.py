from src.main.BaseObjects import *
import pytest


@pytest.mark.parametrize('n', [3])
def test_input(n):
    #m = input("Please enter the total number of students: \n")
    student_list = []
    grade_list = []
    module_list = []
    for i in range(int(n)):
        student = STUDENT()
        student.set_asset('{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                          , '{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                          , '{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                          )
        student_list.append(student)
        grade_list.append(int(student.grade))
        tmp_module= student.max_complex().module
        module_list.append(tmp_module)
    max_grade_value = max(grade_list)
    max_module = max(module_list)
    print("The student with highest score is: {0}, score at {1}"
          .format(student_list[grade_list.index(max_grade_value)].id
                  , max_grade_value))
    print("The student has largest complex module is: {0}, its' value is {1}"
          .format(student_list[module_list.index(max_module)].id
                  , max_module))
    pass


def test_():
    a = STUDENT(name='TamT', id='10012574', room='216')
    a.set_asset('2,8', '0,3', '5,0')
    return a.max_complex()


def test_complex():
    a = COMPLEX.new_complex('-5,0')
    b = COMPLEX.new_complex('10,2')
    c = COMPLEX.new_complex('0,8')
    return a, b, c


def test_person():
    temp_student = STUDENT()
    temp_student.set_asset('{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                      , '{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                      , '{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                      )
    print('Max complex module is: {}'.format(temp_student.max_complex().module))
    return


@pytest.mark.parametrize('n', [3])
def test_random(n):
    for i in range(n):
        print("{0} number is: {1}\n".format(i + 1, random.randrange(0, 99)))
    pass
