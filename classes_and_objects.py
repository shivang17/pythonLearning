# Classes and objects help you make your code more organized and powerful.
# Not all information or data can be represented just by using strings, numbers, or booleans

# There are many information in the real world out there which has relationship with other data and hence you need something else to represent those relationships and models. Eg: Phone or a Computer, you need multiple data about one thing 


# With classes and objects, we can't kind of like create our own data-type
# For example, create a phone Data-type which will represent a phone and have all the required information/property of a phone. We can create class for this.

# We will take an example of a STUDENT class in order to model it

class Student:
    def __init__(self,name,major,gpa,is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
