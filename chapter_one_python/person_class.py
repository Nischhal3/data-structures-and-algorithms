# Exercise: Person Class
#
# Write a class Person that has a member function hello()
# which prints a greeting using the person's name.

class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, my name is {self.name}")