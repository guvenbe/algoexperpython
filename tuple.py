#tuples
# A tuple is very similar to a list, except for the fact that its contents cannot be changed.
# In other words, a tuple is immutable.
# However, it can contain mutable elements like a list. These elements can be altered.
import sys

car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])

print(sys.getrefcount(car))
