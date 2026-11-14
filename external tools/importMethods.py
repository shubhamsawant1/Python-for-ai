#Import entire module
import math
result = math.sqrt(16)
print(result)

#Import specific function 
from math import sqrt, pi
radius = 0
result = sqrt(16)
circle_area = pi * radius ** 2

#Import with alias 
import pandas as pd
df = pd.DataFrame(data)

#Import everything (avoide this!)
from math import *

# ! - Avoide from module * as it can cause naming conflits and make code harder to understand.

