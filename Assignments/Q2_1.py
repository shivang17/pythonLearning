# Perform the following actions:

# 1. Use x = np.random.randint(0, 1000, size = (10, 10)) to generate 10x10 array and use a for loop to find out how many even numbers are in it.

import numpy as np
x = np.random.randint(0,1000, size = (10,10))

print("The array generated is ", x)

even_numbers_count = 0
for arr in range(0,10):
    for i in range(0,10):
        if x[arr][i] % 2 ==0:
            even_numbers_count +=1 

print("The number of even numbers are ",even_numbers_count)


# Output Snapshot

# The array generated is  [[866 918 219 312 868 323   9 365 612 321]
#  [ 34 232 684 336 148 658 813 116 339 861]
#  [285 957 816 329 390  94 676 787 192 162]
#  [856 348 651  86 693  37 422  31  28 536]
#  [432 469 479 197 406  98 975 259 252 986]
#  [514 753 263 825 981 298 541 131 830  55]
#  [717 962 857 313 832 649 734   8 178 843]
#  [591 906 738 310  31 392 846 147 306  87]
#  [975 808 932 660 292 297 172 339 240 901]
#  [631 467 128 892 999 286  51 613 109 728]]

# The number of even numbers are  53