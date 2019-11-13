# QUESTION 6
# Write a recursive program to implement the Ackermann’s function. 	Ackermann’s function is a recursive mathematical algorithm that can be used to test how well a system optimizes its performance of recursion. Design a function Ackermann(m, 	n) with the following logic:
 	
# If m = 0, then return n+1
 		
# If n = 0, then 	Ackermann(m-1, n)
 		
# Otherwise, return Ackermann(m-1, Ackermann(m, n-1))
 	
def ackermann(m,n):
    if m==0:
        return n+1
    elif n==0:
        return ackermann(m-1,n)
    else:
        return ackermann(m-1, ackermann(m,n-1))
def main():
    print(ackermann(100,0))
main()