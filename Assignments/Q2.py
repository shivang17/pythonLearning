                                    # QUESTION 2

# A vineyard owner is planting several rows of grapevines and needs to know how many grapevines to plant in each row. She has determined that after measuring the length of a future row, she can use the following formula to create a number of vines that will fit in a 	row, along with the end-post assemblies that will need to be constructed at each end of the row:


# V = (R – 2E)/ S, V = the number of grapevines that will fit in the row, R = length of the row in ft, E = amount of space, in ft, used by an end-post assembly, S = space between vines in ft.
# Write a program that makes the calculation of the vineyard owner. The program should ask the user to input the following:
# The length of the row in ft
 	
# The amount of space used by the end-post assembly, in ft
 	
# The amount of space between the vines, in ft


# Once the input data has been entered, the program should calculate and display the number of grapevines that will fit in the row.

# Ask the user to enter few data required to perform calculation
row_in_ft = int(input("What is the length of row in ft?"))

space_by_end_post = int(input("What is the amount of space used by the end-post assembly?"))

space_between_vines = int(input("What is the amount of space between the vines,in ft?"))

# Calculation
number_of_grapevine = 0

number_of_grapevine += (row_in_ft- 2*space_by_end_post)/space_between_vines

# Display
print(str(number_of_grapevine) + " " +  "grapevines would fit in the row with a length of " + str(row_in_ft) + " " + "ft")
