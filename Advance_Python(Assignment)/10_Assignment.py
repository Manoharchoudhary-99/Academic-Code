import numpy as np

numbers = np.arange(1, 11)

print("Numbers:", numbers)
print("First 5 elements:", numbers[:5])
print("Elements at even positions:", numbers[1::2])

total = np.sum(numbers)
average = np.mean(numbers)

print("Total:", total)
print("Average:", average)
print("Largest value:", np.max(numbers))
print("Smallest value:", np.min(numbers))

numbers = numbers + 5

print("Numbers after adding 5:", numbers)

# -------------------Output-------------------

# Numbers: [ 1  2  3  4  5  6  7  8  9 10]
# First 5 elements: [1 2 3 4 5]
# Elements at even positions: [ 2  4  6  8 10]
# Total: 55
# Average: 5.5
# Largest value: 10
# Smallest value: 1
# Numbers after adding 5: [ 6  7  8  9 10 11 12 13 14 15]