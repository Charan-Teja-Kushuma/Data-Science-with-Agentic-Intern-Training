from numpy import random

x = random.randint(1,100, size=(2,3))
print(x)
data = x>50
print(x[data])
