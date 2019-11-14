# 1. Use the randn function to create an array with a dimension of 5 X 5 and use a for loop to calculate the sum of all elements in the diagonal of the array

import numpy as np

arr = np.random.randn(5,5)
print("5 X 5 Array is: ", arr)

# Sum of all elements in the diagonal of the array
# sum = 0.0


# # for i in range(5):
# #     sum = sum + arr[i][i]
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             sum = sum + arr[i][j]

sum_1 = 0.0
sum_2 =0.0

for i in range(0,5):
    for j in range(0,5):
        if i == j:
            sum_1 += arr[i][j]


print("--------------------------------------")

for m in range(0,5):
    for n in range(0,5):
        if m + n == 5 -1 :
            sum_2 += arr[m][n]
            print(sum_2)

print("Sum of elements in the diagonals is: \n ",sum_1,sum_2)


# Output Snapshot:
# 5 X 5 Array is:  [[ 0.11723644  0.90324926 -1.67792276  0.39875787  0.32251246]
#  [ 0.76991654 -1.29404319 -0.7319089  -0.50427602  1.47777933]
#  [ 1.84364379 -1.1737907   1.39207689 -0.13568726 -0.38613942]
#  [-1.35156223 -0.25860577 -1.11475661 -0.08380443 -1.4561299 ]
#  [-1.74405339  0.45258536  0.85884452 -0.00939386  1.55339046]]
# --------------------------------------
# 0.3225124565109188
# -0.1817635661159987
# 1.2103133222078486
# 0.9517075502292096
# -0.7923458357666626
# Sum of elements in the diagonals is: 
#   1.6848561684771728 -0.7923458357666626