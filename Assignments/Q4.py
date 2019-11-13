# QUESTION 4
# Create a program that stores Employee objects in Problem 3 in a dictionary. 	Use the Employee ID number as the key. The program should present a menu 	that lets the user perform the following operations:
 	
# Look up an employee in the dictionary
 		
# Add a new employee in the dictionary
 		
# Change an existing employee’s name, department, and job title in the 	dictionary
 		
# Delete an employee from the dictionary
 		
# Quit the program

from Q3 import Employee
import pickle
lookUp=1
add=2
change=3
delete=4
quit=5
def main():
    employee=load_employee()
    choice=0
    while choice !=quit:
        choice=get_choice()
        if choice==lookUp:
            look_up(employee)
        elif choice==add:
            add(employee)
        elif choice==change:
            change(employee)
        elif choice==delete:
            delete(employee)
    save_employee(employee)
def load_employee():
    try:
        input_file=open('employee55.dat','rb')
        employee_doc=pickle.load(input_file)
        input_file.close()
    except:
        employee_doc={}
    return employee_doc
def get_choice():
    print('Menu')
    print('1. Look up a employee')
    print('2. Add a new employee')
    print('3. Change an existing employee info')
    print('4. Delete an employee info')
    print('5. Quit the program')
    print()
    choice=int(input('enter your choice:'))
    while choice<1 or choice>5:
        choice=int(input('Please enter a valid choice:'))
    return choice
def look_up(employee):
    ID=input('Enter an ID:')
    print(employee.get(ID,'That ID does not exist'))
def add(employee):
    name=input('Name:')
    ID=input('ID:')
    department=input('Department:')
    job=input('Job:')
    new=Employee.Employee(name,ID,department,job)
    if name not in employee:
        employee[ID]=new
        print('New Employee Created')
    else:
        print('The name already exists')
def change(employee):
    ID=input('Enter an ID:')
    if ID in employee:
        name=input('Enter a new name:')
        department=input('Enter a new department')
        job=input('Enter a new job')
        new=Employee.Employee(name,ID,department,job)
        employee[id]=new
        print('Info updated')
    else:
        print('That ID is not found')
def delete(employee):
    ID=input('enter an id')
    if ID in employee:
        del employee[ID]
        print('Entry deleted')
    else:
        print('That ID is not found')

def save_employee(employee):
    output_file=open('employee55.dat','wb')
    pickle.dump(employee,output_file)
    output_file.close()
main()
