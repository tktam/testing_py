from ..main.BaseObjects import *
import pytest


@pytest.mark.parametrize('n',[3])
def test_input(n):
    student_list = []
    for i in range(n):
        student = STUDENT()
        student.set_asset('{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                          , '{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                          , '{},{}'.format(random.randrange(-100, 100), random.randrange(-100, 100))
                          )
        student_list.append(student)
    return student_list


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
    return
