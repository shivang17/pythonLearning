#3.4 Analyze mpg for cars with different carb, and show your findings. 

from Q3_1 import mtcars

import numpy as np
import pandas as pd

carbs = pd.DataFrame(mtcars,columns=['mpg','carb'])
description = carbs.groupby('carb').describe()
print("mpg for different carb: \n",description)


# Output Snapshot
# mpg for different carb: 
#         mpg                                                       
#      count       mean       std   min     25%    50%    75%   max
# carb                                                             
# 1      7.0  25.342857  6.001349  18.1  21.450  22.80  29.85  33.9
# 2     10.0  22.400000  5.472152  15.2  18.825  22.10  25.60  30.4
# 3      3.0  16.300000  1.053565  15.2  15.800  16.40  16.85  17.3
# 4     10.0  15.790000  3.911081  10.4  13.550  15.25  18.85  21.0
# 6      1.0  19.700000       NaN  19.7  19.700  19.70  19.70  19.7
# 8      1.0  15.000000       NaN  15.0  15.000  15.00  15.00  15.0