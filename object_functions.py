# In this tutorial, we will talk about class functions. It is a Function which can be used inside a class which can modify the object of the class or give specific information about objects


# For example, let us create a Student class again

class Student:
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
        # One can define function in this class, all of the student object can access it

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        # This function provides service to the object of the class