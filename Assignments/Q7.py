# Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold. Write another program that reads the random numbers from the file, displays the numbers, then displays the following data:


# The total of the numbers
 	
# The number of random numbers reads from the file
import random
file = open('random_numbers.txt','w')

number = int(input("How many random numbers do you want to write to the file? "))

for i in range(number):
    random_number = random.randint(1,500)
    random_number = str(random_number) + '\n'
    file.write(random_number)

file.close()

read_file = open('random_numbers.txt','r')
count =0
for line in read_file:
    print(line)
    count+=1

print(count)