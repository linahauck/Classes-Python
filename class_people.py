class Person:
#Constructor:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#method1 - changing name:
    def change_name(self, new_name):
        self.name = new_name

#method2 - changing age:
    def change_age(self, new_age):
        self.age = new_age

#method3 - change gender
    def change_gender(self, new_gender):
        self.gender = new_gender

#method3 - str
    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}"

J=Person(name="John", age=55, gender="Male")
print(J)

J.change_age(23)
J.change_gender("Female")
print(J)

"""
Terminal> python3 class_people.py
John, 55, Male
John, 23, Female
"""
