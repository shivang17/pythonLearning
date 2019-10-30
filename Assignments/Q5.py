                            # QUESTION 5

# A prime number is a number that is only evenly divisible by itself and 	
# 1. Write a Boolean function named is_prime which takes an integer as an argument and returns true if the argument is a prime number or false otherwise. Use the function in a program that prompts the user to enter a number then displays the message whether the number of primes. Write another program that displays all of the prime numbers from 1 to 100. The program should have a loop that calls the is_prime() function.

number = int(input("Enter the number: "))

def is_prime(number):
    if number <2:
        return False
    elif number ==2:
        return True
    
    else:
        for i in range(2,number-1):
            if number% i ==0:
                return False
        return True

print(is_prime(number))

# 2nd part of the program
prime_numbers = []
for i in range(1,101):
    if is_prime(i):
        prime_numbers.append(i)
# This will display all prime numbers between 1 and 100 in the form of a list using the previous function is_prime
print(prime_numbers)