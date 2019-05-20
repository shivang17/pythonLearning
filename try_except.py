
try:
    number = int(input("Enter a Number: "))

    print(number)
except ZeroDivisionError:
    print("Can't divide by Zero")

except ValueError:
    print("You had a wrong input")

# It is always recommended to define specific error under except, just as we defined ZeroDivisionError and ValueError