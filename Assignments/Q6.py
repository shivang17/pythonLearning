                                # QUESTION 6

# Write a program that generates 100 random numbers and keeps a count of how many of those random numbers are even, and how many are odd.
 	



import random

def is_even(number):
    if number %2 ==0:
        return True
    else:
        return False


# Main Function

def main():
    even = 0
    odd = 0

    for i in range(100):
        number = random.randint(1,100)



        if is_even(number):
            even+=1
        else:
            odd +=1

    print("There are " + str(even) + " even numbers")
    print("There are " + str(odd) + " odd numbers")


main()