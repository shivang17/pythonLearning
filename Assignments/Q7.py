# QUESTION 7

# Design a recursive function that accepts two parameters x, and y. The function should return the values of x * y. Remember the multiplication can be performed as repeated addition as follows:


def recursive_multiply(x, y):
    if (x==0) or (y==0):
        return 0
    else:
        return y + recursive_multiply(x-1, y)

print(recursive_multiply(5,4))