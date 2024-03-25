#!/usr/bin/env python

from user import User


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, new_information):
        self.knowledge.append(new_information)


# Run the tests
class TestStudent:
    '''Class "Student" in student.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert (issubclass(Student, User))

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_student = Student("My", "Student")
        assert ((my_student.first_name, my_student.last_name) == ("My", "Student"))

    def test_initializes_with_knowledge(self):
        '''initializes with empty list attribute "knowledge".'''
        my_student = Student("My", "Student")
        assert (hasattr(my_student, "knowledge"))

    def test_can_learn(self):
        '''learns from a string and adds to self.knowledge.'''
        my_student = Student("My", "Student")
        my_student.learn("New information")
        assert ("New information" in my_student.knowledge)
