# 3.3 Analyze mpg for cars with different gear, and show your findings
from Q3_1 import mtcars
import numpy as np
import pandas as pd

gear = pd.DataFrame(mtcars,columns=['mpg','gear'])
designer = gear.groupby('gear').describe()
print("mpg for cars with different gears are: \n",designer)

# Output Snapshot

# mpg for cars with different gears are: 
#         mpg                                                     
#      count       mean       std   min   25%   50%     75%   max
# gear                                                           
# 3     15.0  16.106667  3.371618  10.4  14.5  15.5  18.400  21.5
# 4     12.0  24.533333  5.276764  17.8  21.0  22.8  28.075  33.9
# 5      5.0  21.380000  6.658979  15.0  15.8  19.7  26.000  30.4