
# 2. Choose any three functions to apply to this array
import numpy as np
from Q1_1 import arr

# Logical condition


conditional = arr[np.logical_and(arr>0, arr <1)]
print("The elements which falls under the condition having value greather than 0 and less than 1 are: \n ",conditional)

# Filteration

filter_arr = arr[[1,2,3,4],[1,2,3,4]]
print("Values filtered are: \n ", filter_arr)

# Transpose

transpose = arr.T
print("The transposed matrix is: \n ", transpose)



# Output Snapshot

#   2.47978730959223
# The elements which falls under the condition having value greather than 0 and less than 1 are: 
#   [0.7245085  0.81130456 0.41085823 0.86372833 0.53891295 0.56044964
#  0.19769311 0.06400206]

# Values filtered are: 
#   [-0.9236885   0.41085823  0.53891295  1.72919613]

# The transposed matrix is: 
#   [[ 0.7245085  -0.19574689 -0.50216661  1.14890024  0.19769311]
#  [ 0.81130456 -0.9236885  -0.55373986 -1.57936906 -0.39635416]
#  [-1.39672901  1.28721558  0.41085823 -0.56780275  0.06400206]
#  [-0.026743    1.28858196 -0.48720508  0.53891295 -0.94935824]
#  [-0.72462981 -1.1997951   0.86372833  0.56044964  1.72919613]]