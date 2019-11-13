# QUESTION 3
# Write a class named Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.
# Once you have written the class, write a program that creates three Employee objects to hold the following data:




class Employee:
    def __init__(self,name,ID,department,job):
        self.__name=name
        self.__ID=ID
        self.__department=department
        self.__job=job

        
    def get_name(self):
        return self.__name
    def get_department(self):
        return self.__department
    def get_ID(self):
        return self.__ID
    def get_job(self):
        return self.__job
    def __str__(self):
        return 'Name:' + self.__name +'\n' + 'ID:' + str(self.__ID) +'\n' +\
               'Department:'+ self.__department + '\n' + \
               'Job:' + self.__job
def display(emp):
   # print(emp.get_name(),emp.get_ID(),emp.get_department(),emp.get_job())
    print(emp)
def main():
    Susan=Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    Mark= Employee('Mark Jones', '39119', 'IT', 'Programmer')
    Joy= Employee('Joy Rogers', '81774', 'Maufacturing', 'Engineer')
    display(Susan)
    display(Mark)
    display(Joy)

main()