#encoding=utf-8
from __future__ import unicode_literals, print_function, division
from nbtest.future2to3 import *

from nbtest.assertpyx import AX

import abc


class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def say_hello(self):
        return 'Hello, %s!' % self.first_name

class Developer(Person):
    def say_hello(self):
        return '%s writes code.' % self.first_name

class AbstractAutomobile(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        pass

    @abc.abstractproperty
    def classification(self):
        raise NotImplementedError('This method must be overridden')

class Car(AbstractAutomobile):
    @property
    def classification(self):
        return 'car'

class Truck(AbstractAutomobile):
    @property
    def classification(self):
        return 'truck'


fred = Person('Fred','Smith')
joe = Developer('Joe','Coder')
people = [fred, joe]
car = Car()
truck = Truck()


def test_is_type_of():
    AX(fred).is_type_of(Person)
    AX(joe).is_type_of(Developer)
    AX(car).is_type_of(Car)
    AX(truck).is_type_of(Truck)

def test_is_type_of_class():
    AX(fred.__class__).is_type_of(Person.__class__)

def test_is_type_of_class_failure():
    try:
        AX(fred.__class__).is_type_of(Person)
        assert False, ('should have raised error')
    except AssertionError as ex:
        AX(str(ex)).contains('to be of type <Person>, but was not')

def test_is_instance_of():
    AX(fred).is_instance_of(Person)
    AX(fred).is_instance_of(object)

    AX(joe).is_instance_of(Developer)
    AX(joe).is_instance_of(Person)
    AX(joe).is_instance_of(object)

    AX(car).is_instance_of(Car)
    AX(car).is_instance_of(AbstractAutomobile)
    AX(car).is_instance_of(object)

    AX(truck).is_instance_of(Truck)
    AX(truck).is_instance_of(AbstractAutomobile)
    AX(truck).is_instance_of(object)

def test_is_instance_of_class():
    AX(fred.__class__).is_instance_of(Person.__class__)

def test_is_instance_of_class_failure():
    try:
        AX(fred.__class__).is_instance_of(Person)
        assert False, ('should have raised error')
    except AssertionError as ex:
        AX(str(ex)).contains('to be instance of class <Person>, but was not')

def test_extract_attribute():
    AX(people).extracting('first_name').is_equal_to(['Fred','Joe'])
    AX(people).extracting('first_name').contains('Fred','Joe')

def test_extract_property():
    AX(people).extracting('name').contains('Fred Smith','Joe Coder')

def test_extract_multiple():
    AX(people).extracting('first_name', 'name').contains(('Fred','Fred Smith'), ('Joe','Joe Coder'))

def test_extract_zero_arg_method():
    AX(people).extracting('say_hello').contains('Hello, Fred!', 'Joe writes code.')

