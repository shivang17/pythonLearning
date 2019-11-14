# Find out which attribute has the most impact on mpg. 

from Q3_1 import mtcars
import numpy as np
import pandas as pd

correlation = mtcars.corr()
sub = correlation.iloc[0,:]
sortcorrelation = sub.sort_values()

print("Correlation table: ", correlation)
print("Impact of variables on mpg: \n",sortcorrelation)

position = sub >0

position_coordinate = sub[position]
negative_coordinate = sub[~position]

print("Positively correlated: \n",position_coordinate.sort_values())
print("Negatively correlated: \n",negative_coordinate.sort_values())

# Output Snapshot

# 31           Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.60   1   1     4     2
# Correlation table:             mpg       cyl      disp        hp    ...           vs        am      gear      carb
# mpg   1.000000 -0.852162 -0.847551 -0.776168    ...     0.664039  0.599832  0.480285 -0.550925
# cyl  -0.852162  1.000000  0.902033  0.832447    ...    -0.810812 -0.522607 -0.492687  0.526988
# disp -0.847551  0.902033  1.000000  0.790949    ...    -0.710416 -0.591227 -0.555569  0.394977
# hp   -0.776168  0.832447  0.790949  1.000000    ...    -0.723097 -0.243204 -0.125704  0.749812
# drat  0.681172 -0.699938 -0.710214 -0.448759    ...     0.440278  0.712711  0.699610 -0.090790
# wt   -0.867659  0.782496  0.887980  0.658748    ...    -0.554916 -0.692495 -0.583287  0.427606
# qsec  0.418684 -0.591242 -0.433698 -0.708223    ...     0.744535 -0.229861 -0.212682 -0.656249
# vs    0.664039 -0.810812 -0.710416 -0.723097    ...     1.000000  0.168345  0.206023 -0.569607
# am    0.599832 -0.522607 -0.591227 -0.243204    ...     0.168345  1.000000  0.794059  0.057534
# gear  0.480285 -0.492687 -0.555569 -0.125704    ...     0.206023  0.794059  1.000000  0.274073
# carb -0.550925  0.526988  0.394977  0.749812    ...    -0.569607  0.057534  0.274073  1.000000

# mpact of variables on mpg: 
#  wt     -0.867659
# cyl    -0.852162
# disp   -0.847551
# hp     -0.776168
# carb   -0.550925
# qsec    0.418684
# gear    0.480285
# am      0.599832
# vs      0.664039
# drat    0.681172
# mpg     1.000000
# Name: mpg, dtype: float64


# Name: mpg, dtype: float64
# Negatively correlated: 
#  wt     -0.867659
# cyl    -0.852162
# disp   -0.847551
# hp     -0.776168
# carb   -0.550925
# Name: mpg, dtype: float64