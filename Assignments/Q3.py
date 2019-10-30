                            # QUESTION 3

# The month of February normally has 28 days. But if it is a leap year, February has 29 days. Write a program that asks the user to enter a year. The program should then display the number of days in February that year. Use the following criterion to identify leap years:


# Determine whether the year is divisible by 100, if it is, then it is a leap year if and only if it is also divisible by 400.
 	
# If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4.

def is_leap_year(year):
    leap_year_message = " "
    if year %100 ==0:
        if year %400 ==0:
            leap_year_message += "is a leap year"
        else:
            leap_year_message += "is not a leap year"
        
            
    else :
        if year % 4 ==0:
            leap_year_message += "is a leap year"
        else:
            leap_year_message += "is not a leap year"
            
    
    return leap_year_message

user_input_leap_year = int(input("Please enter a year of your choice"))

print(str(user_input_leap_year) + is_leap_year(user_input_leap_year))
