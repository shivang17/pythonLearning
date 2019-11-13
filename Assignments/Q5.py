# QUESTION 5
# Write an employee class with the data attributes defined in Problem 3. Next, write a class named ProductionWorker that is a subclass of the employee class, that should keep the data attributes for the following pieces of information:
 	
# Shift number (an integer, e.g., 1, 2, 3, etc.)
 		
# Hourly pay rate.

class Employee:
    def __init__(self,name,ID,department,job):
        self.__name=name
        self.__ID=ID
        self.__department=department
        self.__job=job
    def set_Name(self,name):
        self.__name=name
    def set_ID(self,ID):
        self.__ID=ID
    def set_department(self,department):
        self.__department=department
    def set_ID(self,job):
        self.__job=job
    def get_name(self):
        return self.__name
    def get_department(self):
        return self.__department
    def get_ID(self):
        return self.__ID
    def get_job(self):
        return self.__job
class ProductionWorker(Employee):
    def __init__(self,name,ID,department,job,shiftNumber,hourlyPayrate):
        Employee.__init__(self,name,ID,department,job)
        self.__shiftNumber=shiftNumber
        self.__hourlyPayrate=hourlyPayrate
    def set_shiftNumber(self,shiftNumber):
        self.__shiftNumber=shiftNumber
    def get_shiftNumber(self):
        return self.__shiftNumber
    def set_hourlyPayrate(self,hourlyPayrate):
        self.__hourlyPayrate=hourlyPayrate
    def get_hourlyPayrate(self):
        return self.__hourlyPayrate
    
def display(emp):
    print(emp.get_name(),emp.get_ID(),emp.get_department(),emp.get_job(), emp.get_shiftNumber(),emp.get_hourlyPayrate())
    
def main():
    answer='y'
    while answer=='y':
        name=input('Enter a Name:')
        ID=input('Enter an ID:')
        department=input('Enter a Department:')
        job=input('Enter a Job:')
        shiftNumber=int(input('Enter a shift number:'))
        hourlyPayRate=input('Enter hourly pay rate')
        if shiftNumber==1 or shiftNumber==2:
            Person=ProductionWorker(name,ID,department,job,shiftNumber,hourlyPayRate)
            display(Person)
            answer=input('enter y to continue the process')
        else:
            print('you input a wrong shift number')
            answer=input('enter y to continue the process')
main()