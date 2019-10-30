                                    # QUESTION 1

# A cookie recipe calls for the following ingredients:
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour
# The recipe produces 48 cookies with this amount of ingredients. Write a program that asks the user how many cookies he/she wants to make, then displays the number of cups of each ingredient needed for the specified number of cookies.

# SOLUTION 1
# Global variables
cups_of_sugar = 1.5
cups_of_butter = 1
cups_of_flour = 2.75
cookies = 48

number_of_cookies = int(input("How many cookies you want to make?"))

cups_of_sugar_required = (number_of_cookies * cups_of_sugar)/cookies
cups_of_butter_required = (number_of_cookies * cups_of_butter)/cookies
cups_of_flour_required = (number_of_cookies * cups_of_flour)/cookies

print("For the specified number of cookies, you will need " + " " + str(format(cups_of_sugar_required, '.2f')) + "cups of sugar " + str(format(cups_of_butter_required,'.2f')) + ""  + "cups of butter " + str(format(cups_of_flour_required,'.2f')) + " " +  "cups of flour")

