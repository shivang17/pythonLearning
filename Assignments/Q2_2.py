# 2. Randomly generate a 8x9 array from a normal distribute with mean = 1, sigma = 0.5. Calculate the mean of elements whose indexes have a relation of (i+j)%5 == 0  (i is row index and j is column index).
import numpy as np
array = np.random.normal(loc = 1, scale = 0.5,size = (8,9))
print("Mean of array is: \n ", array.mean())

sum = 0
count = 0
for i in range(8):
    for j in range(9):
        if ((i+j)%5)==0:
            count = count +1
            sum = sum + array[i][j]
mean = sum/count
print("Mean of the elements are: ",mean,"\n")

# Output Snapshot

# Mean of array is: 
#   1.0871226466739632
# Mean of the elements are:  1.1966495857892334 