import numpy as np
import pandas as pd

values = pd.Series(np.random.randint(1, 101, size=10))

print("Generated Series:")
print(values)

print("\nValue at index 0:", values.iloc[0])
print("Values between index 2 and 5:")
print(values.iloc[2:6])

above_50 = values[values > 50]
print("\nValues above 50:")
print(above_50)

print("\nAverage:", values.mean())
print("Middle value (Median):", values.median())
print("Lowest:", values.min())
print("Highest:", values.max())


# --------------------Output-------------------

# Generated Series:
# 0    11
# 1    57
# 2    31
# 3     4
# 4    49
# 5    90
# 6    81
# 7    62
# 8    14
# 9    77
# dtype: int32

# Value at index 0: 11
# Values between index 2 and 5:
# 2    31
# 3     4
# 4    49
# 5    90
# dtype: int32

# Values above 50:
# 1    57
# 5    90
# 6    81
# 7    62
# 9    77
# dtype: int32

# Average: 47.6
# Middle value (Median): 53.0
# Lowest: 4
# Highest: 90