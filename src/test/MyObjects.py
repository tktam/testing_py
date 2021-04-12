import math
import random


class PERSON(object):

    def __init__(self, name=None, age=None, gender=None):
        if name is not None:
            self._name = name
        else:
            self._name = "Student number 2021CLC0{}".format(random.randrange(1, 100))
        if age is not None:
            self._age = age
        else:
            self._age = random.randint(17, 26)
        if gender is not None:
            self._gender = gender
        else:
            self._gender = random.choice(['female', 'male'])

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @property
    def gender(self):
        return self._gender


class STUDENT(PERSON):

    def __init__(self, name=None, age=None, gender=None, id=None, grade=None, room=None):
        super().__init__(name, age, gender)
        #Using instance's attribute, not Class Attribute here
        self._complex_list = []
        if id is not None:
            self._id = id
        else:
            self._id = random.randint(0, 1000000)
        if room is not None:
            self._room = room
        else:
            self._room = random.randrange(1, 99)
        if grade is not None:
            self._grade = grade
        else:
            self._grade = random.randint(0, 10)

    @property
    def id(self):
        return self._id

    @property
    def room(self):
        return self._room

    @property
    def grade(self):
        return self._grade

    @property
    def complex_list(self):
        return self._complex_list

    def set_asset(self, complex_1, complex_2, complex_3):
        self.complex_list.append(COMPLEX.new_complex(complex_1))
        self.complex_list.append(COMPLEX.new_complex(complex_2))
        self.complex_list.append(COMPLEX.new_complex(complex_3))

    def max_complex(self):
        if self._complex_list is not None:
            a = self._complex_list[0]
            b = self._complex_list[1]
            c = self._complex_list[2]
            tmp = [a.module, b.module, c.module]
            max_value = max(tmp)
            return self._complex_list[tmp.index(max_value)]


class COMPLEX(object):
    _real = random.randrange(-500, 500)
    _image = random.randrange(-500, 500)

    def __init__(self, real_value=None, image_value=None):
        if real_value is not None:
            self._real = real_value
        if image_value is not None:
            self._image = image_value
        self.module = math.sqrt(self._real ** 2 + self._image ** 2)

    @classmethod
    def new_complex(cls, a):
        real_value = str(a).split(',')[0]
        image_value = str(a).split(',')[1]
        return COMPLEX(float(real_value), float(image_value))

    @property
    def image(self):
        return self._image

    @property
    def real(self):
        return self._real
