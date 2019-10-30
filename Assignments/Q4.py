# Write a program that predicts the approximate size of a population of organisms. The application allows the user to enter the starting number of organisms, the average daily population increase (as a percentage), and the number of days the organisms will be left to multiply. Assume the user enters the following values:


# Starting number of organisms: 2
 	
# Average daily increase: 30%
 	
# Number of days to multiply: 10


# The program should display the output in the  form of the table


starting_number_of_population = int(input("Enter the starting population of the organisms: "))

population_increase_in_percentage = int(input("Enter the daily average population increase in terms of percentage"))

num_days = int(input("Enter the number of days the population that will multiply: "))

print('\n' + '\033[4m' + 'Day            Population' + '\033[0m')

for day in range(1,num_days+1):
    if day ==1:
        population = starting_number_of_population
    else:
        population *= (1+population_increase_in_percentage/100)
    print(format(day, '<5d') , format(population,'12.2f'))